# ✅ ĐÁP ÁN CHI TIẾT & PHÂN TÍCH BẢN CHẤT — W01-D1 (NGÀY 01)

> **Chủ đề:** Cơ chế Namespace, Quy tắc LEGB & Quản lý Cấu hình Thí nghiệm bằng `dataclasses`  
> **Mục tiêu tự đánh giá:** Đối chiếu kết quả, đọc kỹ phân tích lý do **tại sao đúng** và **điểm sai của từng phương án nhiễu** để vá triệt để lỗ hổng nhận thức.

---

### Bài 1: Phân Tích Cơ Chế Scoping & Quy Tắc LEGB

* **Đáp án đúng:** **C** (`UnboundLocalError` tại dòng `lr = lr * decay`)

#### 🔬 Giải thích bản chất
Trong trình biên dịch CPython, **phạm vi của biến (Variable Scope) được xác định tĩnh tại thời điểm biên dịch hàm thành bytecode (Compile-time)**, chứ không phải tại thời điểm thực thi từng dòng (Runtime).

Khi Python biên dịch thân hàm `run_step`, trình phân tích cú pháp phát hiện câu lệnh gán `lr = lr * decay`. Theo quy tắc ngôn ngữ của Python, bất kỳ tên biến nào được gán giá trị (nằm ở vế trái dấu `=`) bên trong một hàm mà không có khai báo `global` hay `nonlocal` đều bị đánh dấu là **Biến Cục Bộ (Local Variable)** trên toàn bộ thân hàm đó.

Do đó, ở vế phải của `lr = lr * decay`, trình biên dịch sinh mã bytecode `LOAD_FAST_CHECK` (đọc biến cục bộ `lr`) thay vì `LOAD_GLOBAL`. Tại thời điểm biểu thức vế phải `lr * decay` được định giá, biến cục bộ `lr` chưa từng được khởi tạo bất kỳ giá trị nào, dẫn đến ngoại lệ:
```text
UnboundLocalError: cannot access local variable 'lr' where it is not associated with a value
```

#### ❌ Phân tích điểm sai của các phương án còn lại
* **Phương án A (Sai):** Lầm tưởng Python thực thi kiểu "vừa đọc vừa dò scope từng dòng" (đọc `lr` ở Global rồi mới tạo `lr` mới ở Local). Thực tế, sự tồn tại của phép gán trong hàm đã "chiếm quyền" tên `lr` cho Local Namespace ngay từ bước biên dịch, che khuất hoàn toàn biến Global `lr = 0.01`.
* **Phương án B (Sai):** Dù đúng là `lr` trong hàm là biến cục bộ không làm thay đổi biến Global, nhưng biểu thức `lr * decay` ở vế phải buộc phải đọc giá trị của `lr` cục bộ trước khi gán lại; vì chưa có giá trị nên chương trình sập chứ không thể trả về `0.01`.
* **Phương án D (Sai):** Python không ném `NameError` bởi vì tên `lr` *có tồn tại* trong bảng ký hiệu cục bộ (Local symbol table) của hàm; lỗi ở đây là biến đã được khai báo trong phạm vi cục bộ nhưng *chưa được ràng buộc với giá trị nào* (`UnboundLocalError`, một lớp con chuyên biệt của `NameError`).

---

### Bài 2: Phạm Vi Bao Ngoài (Enclosing Scope) & Closure Trong Theo Dõi Huấn Luyện

* **Đáp án đúng:** **A** (In ra `[False, False, False, True]` và `nonlocal` là bắt buộc)

#### 🔬 Giải thích bản chất
Đây là cấu trúc **Closure (Bao đóng)** kinh điển trong Python:
1. Khi `make_early_stopper(patience=2)` chạy xong và trả về hàm `check`, các biến trong phạm vi Enclosing (`best_loss`, `counter`, `patience`) **không bị giải phóng**, vì hàm `check` vẫn giữ tham chiếu (cell reference) tới chúng thông qua thuộc tính `__closure__`.
2. Theo dõi dấu vết từng lần gọi `stopper`:
   - `stopper(0.5)`: `0.5 < inf` $\rightarrow$ `best_loss = 0.5`, `counter = 0`. Trả về `0 >= 2` $\rightarrow$ `False`.
   - `stopper(0.4)`: `0.4 < 0.5` $\rightarrow$ `best_loss = 0.4`, `counter = 0`. Trả về `0 >= 2` $\rightarrow$ `False`.
   - `stopper(0.45)`: `0.45 < 0.4` là Sai $\rightarrow$ `counter = 1`. Trả về `1 >= 2` $\rightarrow$ `False`.
   - `stopper(0.48)`: `0.48 < 0.4` là Sai $\rightarrow$ `counter = 2`. Trả về `2 >= 2` $\rightarrow$ `True` (kích hoạt dừng sớm).
3. Từ khóa `nonlocal best_loss, counter` là bắt buộc vì bên trong `check` có phép gán `best_loss = ...` và `counter += 1`. Nếu thiếu `nonlocal`, Python sẽ coi chúng là biến Local của `check` và ném `UnboundLocalError` tại câu lệnh `counter += 1` (tương tự cơ chế ở Bài 1).

#### ❌ Phân tích điểm sai của các phương án còn lại
* **Phương án B (Sai):** Sai về cơ chế vòng đời Closure. Chỉ các biến cục bộ không bị hàm con nào tham chiếu mới bị hủy sau khi hàm cha kết thúc; ở đây `check` đóng gói trạng thái của `make_early_stopper` lại để tái sử dụng qua nhiều lần gọi.
* **Phương án C (Sai):** Tính nhầm bước đầu tiên. Ở lần gọi đầu tiên (`0.5`), vì `best_loss` khởi tạo là `float("inf")` (dương vô cực), điều kiện `0.5 < float("inf")` là Đúng nên `counter` giữ ở `0`, không phải `1`.
* **Phương án D (Sai):** Nếu thay `nonlocal` bằng `global`, Python sẽ bỏ qua Enclosing Scope và nhảy thẳng lên tìm `best_loss`, `counter` ở cấp Module (Global). Vì cấp Module không hề định nghĩa hai biến này, chương trình sẽ báo lỗi `NameError: name 'best_loss' is not defined`.

---

### Bài 3: Bẫy Mutable Fields & Tính Bất Biến Trong `dataclasses`

* **Đáp án đúng:** **C** (Lệnh 1 thực thi thành công làm thay đổi `hp.layers` thành `[64, 32, 16]`; Lệnh 2 ném `FrozenInstanceError`)

#### 🔬 Giải thích bản chất
Tham số `frozen=True` trong `@dataclass` chỉ tạo ra **Tính bất biến nông (Shallow Immutability)**. Cơ chế bên dưới của `frozen=True` là ghi đè hai phương thức đặc biệt `__setattr__` và `__delattr__` của class để ném ngoại lệ `dataclasses.FrozenInstanceError` bất cứ khi nào có thao tác **gán lại tên thuộc tính** (ví dụ `hp.lr = 0.001` hoặc `hp.layers = [128]`).

Tuy nhiên, trong **Lệnh 1 (`hp.layers.append(16)`)**, chúng ta **không gán lại thuộc tính `hp.layers`**. Python chỉ đọc tham chiếu của đối tượng `list` đang gắn với `hp.layers`, sau đó gọi phương thức `.append(16)` làm biến đổi nội dung ngay tại chỗ (in-place mutation) trên vùng nhớ của danh sách đó. `hp.__setattr__` hoàn toàn không được kích hoạt, nên danh sách bị thay đổi âm thầm thành `[64, 32, 16]`.

> 💡 **Bài học R&D:** Để đạt **bất biến sâu (Deep Immutability)** cho cấu hình thí nghiệm, hãy luôn dùng kiểu bất biến `tuple[int, ...] = (64, 32)` thay vì `list[int]`.

#### ❌ Phân tích điểm sai của các phương án còn lại
* **Phương án A (Sai):** Ngộ nhận `frozen=True` khóa toàn bộ mọi đối tượng bên trong nó (Deep Immutability). Thực tế `frozen=True` chỉ chặn việc tái gắn nhãn thuộc tính trên chính instance đó.
* **Phương án B (Sai):** `dataclasses` chỉ ném `ValueError` khi bạn gán giá trị mặc định là đối tượng khả biến **trực tiếp** (`layers: list[int] = [64, 32]`). Ở đây đề bài đã dùng `field(default_factory=lambda: [64, 32])` hợp lệ theo đúng chuẩn PEP 557 nên định nghĩa class không hề báo lỗi.
* **Phương án D (Sai):** Ngược hoàn toàn về bản chất: `list` là kiểu khả biến (mutable) nên `.append(16)` không ném `AttributeError`; còn `hp.lr = 0.001` chắc chắn bị `__setattr__` của `frozen=True` chặn đứng bằng `FrozenInstanceError`.

---

### Bài 4: Thực Hành Refactoring — Khử Biến Toàn Cục & Rò Rỉ Trạng Thái

#### 1. Phân tích 2 nguyên nhân gây sai lệch ở đoạn mã gốc
Khi chạy thực tế đoạn mã lỗi ban đầu, kết quả thu được là:
* **Run 1:** `loss = 0.833625` | `LOSS_HISTORY = [0.9, 0.855, 0.833625]`
* **Run 2:** `loss = 0.9782614746093751` | `LOSS_HISTORY = [0.9, 0.855, 0.833625, 0.9875, 0.981328, 0.978261]`

Hai nguyên nhân gốc rễ:
1. **Đột biến biến toàn cục `LEARNING_RATE` (Silent Global Mutation):** Từ khóa `global LEARNING_RATE` khiến mỗi vòng lặp trong Run 1 nhân giảm `LEARNING_RATE` đi một nửa ($0.1 \to 0.05 \to 0.025 \to 0.0125$). Khi Run 2 bắt đầu, thay vì chạy với `0.1`, nó lại khởi chạy với giá trị tàn dư `0.0125` của Run 1, khiến loss giảm rất ít.
2. **Tích lũy trạng thái trong danh sách toàn cục `LOSS_HISTORY`:** Dù không khai báo `global LOSS_HISTORY`, lệnh `.append(...)` vẫn thay đổi trực tiếp đối tượng list toàn cục, làm lịch sử của Run 2 bị nối đuôi vào kết quả của Run 1 (lên tới 6 phần tử thay vì 3).

#### 2. Mã nguồn Refactor chuẩn R&D (Đã kiểm chứng trên Python 3.14)

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingRunConfig:
    """Cấu hình bất biến cho một lượt mô phỏng huấn luyện."""

    learning_rate: float = 0.01
    epochs: int = 3
    decay_rate: float = 0.5


def train_simulation(config: TrainingRunConfig) -> dict[str, object]:
    """
    Hàm thuần khiết (Pure Function) mô phỏng quá trình giảm loss.
    Không đọc hay làm thay đổi bất kỳ biến toàn cục nào.
    """
    lr = config.learning_rate  # Tạo biến cục bộ độc lập hoàn toàn với config
    losses: list[float] = []
    current_loss = 1.0

    for _ in range(config.epochs):
        current_loss = current_loss * (1.0 - lr)
        losses.append(round(current_loss, 6))
        lr = lr * config.decay_rate

    return {
        "final_lr": lr,
        "loss_history": tuple(losses),  # Trả về tuple bất biến
    }


if __name__ == "__main__":
    cfg = TrainingRunConfig(learning_rate=0.1, epochs=3, decay_rate=0.5)

    res1 = train_simulation(cfg)
    res2 = train_simulation(cfg)

    print("Run 1:", res1)
    print("Run 2:", res2)
    assert res1 == res2, "Lỗi: Hai lần chạy cùng cấu hình cho kết quả khác nhau!"
    print("Kiểm chứng tái lập (Reproducibility) thành công 100%.")
```

* **Kết quả chạy thực tế:**
  `{'final_lr': 0.0125, 'loss_history': (0.9, 0.855, 0.833625)}` cho cả hai lần chạy, `assert res1 == res2` vượt qua tuyệt đối.

---

### Bài 5: Thiết Kế Hệ Thống Cấu Hình Nghiên Cứu Chuẩn R&D

#### Mã nguồn chuẩn mực (`config.py`)

```python
from dataclasses import asdict, dataclass, field
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    dataset_name: str
    split_ratios: tuple[float, float, float] = (0.7, 0.15, 0.15)

    def __post_init__(self) -> None:
        cleaned_name = self.dataset_name.strip()
        object.__setattr__(self, "dataset_name", cleaned_name)
        if not cleaned_name:
            raise ValueError("dataset_name không được để trống.")
        if len(self.split_ratios) != 3 or any(r <= 0.0 for r in self.split_ratios):
            raise ValueError("split_ratios phải gồm đúng 3 số thực lớn hơn 0.")
        if not math.isclose(sum(self.split_ratios), 1.0, rel_tol=1e-9, abs_tol=1e-9):
            raise ValueError(
                f"Tổng split_ratios phải bằng 1.0, hiện tại là {sum(self.split_ratios)}."
            )


@dataclass(frozen=True)
class ModelConfig:
    optimizer: str = "adam"
    learning_rate: float = 1e-3
    hidden_dims: tuple[int, ...] = (128, 64)

    def __post_init__(self) -> None:
        norm_opt = self.optimizer.strip().lower()
        object.__setattr__(self, "optimizer", norm_opt)
        if norm_opt not in {"sgd", "adam", "adamw"}:
            raise ValueError(f"Optimizer '{norm_opt}' không được hỗ trợ.")
        if self.learning_rate <= 0.0:
            raise ValueError("learning_rate phải lớn hơn 0.")
        if not self.hidden_dims or any(d <= 0 for d in self.hidden_dims):
            raise ValueError("hidden_dims phải chứa ít nhất 1 số nguyên dương.")


@dataclass(frozen=True)
class ExperimentConfig:
    experiment_id: str
    seed: int = 42
    batch_size: int = 32
    data: DataConfig = field(default_factory=lambda: DataConfig(dataset_name="iris"))
    model: ModelConfig = field(default_factory=ModelConfig)

    def __post_init__(self) -> None:
        if not self.experiment_id.strip():
            raise ValueError("experiment_id không được để trống.")
        if self.seed < 0:
            raise ValueError("seed phải >= 0.")
        if self.batch_size <= 0:
            raise ValueError("batch_size phải > 0.")

    def save_json(self, filepath: str | Path) -> None:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=2, ensure_ascii=False)

    @classmethod
    def load_json(cls, filepath: str | Path) -> "ExperimentConfig":
        path = Path(filepath)
        with path.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        data_dict = raw.pop("data")
        data_dict["split_ratios"] = tuple(data_dict["split_ratios"])
        model_dict = raw.pop("model")
        model_dict["hidden_dims"] = tuple(model_dict["hidden_dims"])

        return cls(
            **raw,
            data=DataConfig(**data_dict),
            model=ModelConfig(**model_dict),
        )


if __name__ == "__main__":
    # 1. Kiểm tra chuẩn hóa chuỗi trong frozen dataclass
    exp = ExperimentConfig(
        experiment_id="exp_w01_d1",
        data=DataConfig(dataset_name="  housing  ", split_ratios=(0.6, 0.2, 0.2)),
        model=ModelConfig(optimizer=" AdamW ", hidden_dims=(256, 128, 64)),
    )
    assert exp.data.dataset_name == "housing"
    assert exp.model.optimizer == "adamw"

    # 2. Kiểm tra fail-fast validation
    for bad_call in [
        lambda: DataConfig(dataset_name="iris", split_ratios=(0.7, 0.2, 0.2)),
        lambda: ModelConfig(optimizer="rmsprop"),
    ]:
        try:
            bad_call()
            raise AssertionError("Lẽ ra phải ném ValueError!")
        except ValueError as err:
            print("Đã chặn thành công cấu hình sai:", err)

    # 3. Kiểm tra lưu & khôi phục JSON bảo toàn 100%
    temp_path = Path("configs/test_exp_01.json")
    exp.save_json(temp_path)
    exp_loaded = ExperimentConfig.load_json(temp_path)
    assert exp == exp_loaded, "Cấu hình đọc lại từ JSON không khớp với bản gốc!"
    print("Kiểm chứng lưu/đọc JSON thành công:", exp_loaded)
```

#### 🔍 Các lỗi sai phổ biến học viên hay gặp ở Bài 5
1. **Gán trực tiếp `self.optimizer = norm_opt` trong `__post_init__`:** Khi `frozen=True`, thao tác gán thông thường sẽ bị chặn bởi `FrozenInstanceError`. Bắt buộc dùng `object.__setattr__(self, "optimizer", norm_opt)`.
2. **Dùng phép so sánh `sum(self.split_ratios) == 1.0`:** Trong biểu diễn số thực dấu phẩy động (IEEE 754), tổng của 3 số float đôi khi ra `0.9999999999999999` hoặc `1.0000000000000002`, dẫn đến báo lỗi giả. Bắt buộc dùng `math.isclose(..., rel_tol=1e-9, abs_tol=1e-9)`.
3. **Quên ép kiểu `tuple` khi `load_json`:** Định dạng JSON không có kiểu `tuple` mà chuyển hết thành JSON array (`list` khi đọc lại vào Python). Nếu không chuyển `split_ratios` và `hidden_dims` từ `list` về `tuple` trước khi truyền vào `DataConfig` / `ModelConfig`, phép kiểm tra `exp == exp_loaded` sẽ trả về `False` (vì `(0.6, 0.2, 0.2) != [0.6, 0.2, 0.2]`).
4. **Dùng `default_factory` sai cho `DataConfig`:** Vì `DataConfig` có tham số bắt buộc `dataset_name` (không có giá trị mặc định), nếu viết `field(default_factory=DataConfig)` sẽ lỗi `TypeError`, phải dùng `field(default_factory=lambda: DataConfig(dataset_name="iris"))`.
