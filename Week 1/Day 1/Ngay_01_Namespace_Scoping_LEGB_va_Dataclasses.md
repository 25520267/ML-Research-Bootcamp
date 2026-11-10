# 📘 GIÁO ÁN THAM KHẢO — W01-D1 (NGÀY 01)

> **Giai đoạn:** Phase I – The Language & The Math Engine  
> **Tuần 1 – Ngày 1:** Cơ chế Namespace, Phạm vi biến (Scoping - Quy tắc LEGB) & Quản lý Cấu hình Thí nghiệm bằng `dataclasses`  
> **Thời lượng tiêu chuẩn:** 120 phút (36 phút Lý thuyết | 60 phút Thực hành | 24 phút Active Recall & Lab Log)  
> **Chuẩn đầu ra R&D:** Viết mã nguồn Python module hóa, không phụ thuộc trạng thái toàn cục (Global State), đảm bảo tính tái lập (Reproducibility) cho thí nghiệm Machine Learning.

---

## 🎯 MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)

Sau buổi học hôm nay, bạn phải làm chủ được:
1. Giải thích chính xác bản chất của **Namespace** (Không gian tên) và thứ tự phân giải biến theo **Quy tắc LEGB** trong CPython.
2. Lý giải được ở tầng biên dịch bytecode nguyên nhân sinh ra lỗi kinh điển `UnboundLocalError` và phân biệt rành mạch từ khóa `global` với `nonlocal`.
3. Phân tích được cơ chế gây sai lệch kết quả (State Leakage & Silent Corruption) khi dùng biến toàn cục trong quy trình nghiên cứu ML và Jupyter Notebook.
4. Thiết kế thành thạo module quản lý siêu tham số (Hyperparameters) bất biến bằng `@dataclass(frozen=True)`, kiểm tra tính hợp lệ (`__post_init__`), tránh bẫy Mutable Default, và tuần tự hóa ra JSON để lưu trữ thí nghiệm.

---

## 📖 PHẦN 1: LÝ THUYẾT CỐT LÕI (30% — 36 PHÚT)

### 1.1. Bản Chất Của Namespace Trong Python
Trong Python, **mọi thứ đều là đối tượng (Object)** nằm trên bộ nhớ Heap, còn tên biến (Identifier) thực chất chỉ là nhãn dán (reference) trỏ tới đối tượng đó.

**Namespace (Không gian tên)** là một cấu trúc ánh xạ (mapping) từ **Tên định danh** $\rightarrow$ **Đối tượng**, hoạt động bên dưới gần như tương đương với một `dict` của Python (`{name: object_reference}`).

Python quản lý 4 loại Namespace theo vòng đời thực thi:
1. **Built-in Namespace:** Chứa các hàm và ngoại lệ có sẵn của ngôn ngữ (`len`, `print`, `sum`, `ValueError`, ...). Được tạo khi trình thông dịch Python khởi động và tồn tại đến khi tắt.
2. **Global (Module) Namespace:** Chứa các biến, hàm, class được định nghĩa ở cấp cao nhất của một tệp `.py` (hoặc toàn bộ session của một Jupyter Notebook). Có thể truy cập từ điển này qua hàm `globals()`.
3. **Enclosing Namespace:** Không gian tên của hàm bao ngoài (Outer Function) đối với các hàm lồng nhau (Nested Functions).
4. **Local Namespace:** Được tạo mới mỗi khi một hàm được gọi và bị hủy ngay khi hàm kết thúc (`return` hoặc ném ngoại lệ). Có thể kiểm tra qua `locals()`.

> 💡 **Góc nhìn R&D:** Vì Local Namespace bị hủy sau khi hàm kết thúc, các biến cục bộ bên trong hàm đảm bảo **tính cô lập (Isolation)**: lần chạy thử nghiệm số 2 sẽ không bao giờ bị "dính" rác bộ nhớ của lần chạy số 1. Ngược lại, Global Namespace tồn tại xuyên suốt vòng đời module.

---

### 1.2. Scoping & Quy Tắc LEGB (Name Resolution Order)
**Scope (Phạm vi)** là vùng văn bản mã nguồn nơi một Namespace có thể được truy cập trực tiếp mà không cần tiền tố (prefix). Khi Python bắt gặp một tên biến `x`, nó tìm kiếm tuần tự từ trong ra ngoài theo **Quy tắc LEGB**:

```text
  [ L ] Local      (Bên trong hàm hiện tại)
    │
    ▼ (Nếu không thấy)
  [ E ] Enclosing  (Bên trong các hàm bao ngoài, từ trong ra ngoài)
    │
    ▼ (Nếu không thấy)
  [ G ] Global     (Cấp module / top-level)
    │
    ▼ (Nếu không thấy)
  [ B ] Built-in   (Tầng định nghĩa sẵn của Python)
    │
    ▼ (Nếu không thấy)
  NameError: name 'x' is not defined
```

#### ⚠️ Cơ chế Compile-Time Binding & Bẫy `UnboundLocalError`
Một hiểu lầm cực kỳ phổ biến của người mới là cho rằng Python quyết định biến thuộc Local hay Global *tại thời điểm chạy từng dòng*. **Thực tế không phải vậy!**

Trong CPython, trình biên dịch xác định phạm vi của toàn bộ biến **tại thời điểm biên dịch hàm thành bytecode (Compile-time)**:
* Bất kỳ tên biến nào xuất hiện ở **vế trái của phép gán (`=`)**, trong định nghĩa `def`, `class`, `import`, hoặc vòng `for`, đều bị đánh dấu là **Biến Cục Bộ (Local Variable)** cho toàn bộ thân hàm đó.

Hãy xét ví dụ sau:
```python
lr = 0.01  # Biến Global

def update_lr():
    print("Current lr:", lr)  # Dòng này nằm TRƯỚC phép gán
    lr = lr * 0.5             # Có phép gán -> Python coi 'lr' là LOCAL cho cả hàm!

update_lr()
```
Khi biên dịch `update_lr`, CPython sinh mã bytecode `LOAD_FAST_CHECK` (tìm biến cục bộ `lr`) cho dòng `print(...)` thay vì `LOAD_GLOBAL`. Khi chạy đến dòng `print`, biến cục bộ `lr` chưa được gán giá trị, dẫn đến lỗi:
```text
UnboundLocalError: cannot access local variable 'lr' where it is not associated with a value
```

#### Từ khóa `global` và `nonlocal`
* **`global var`:** Báo cho trình biên dịch biết `var` không phải là Local mà trỏ thẳng tới biến ở cấp Module. *(Khuyến cáo: Tuyệt đối hạn chế dùng trong code nghiên cứu).*
* **`nonlocal var`:** Dùng bên trong hàm lồng nhau (Closure) để thông báo `var` thuộc phạm vi Enclosing (hàm cha gần nhất), cho phép hàm con cập nhật lại giá trị của hàm cha mà không làm ô nhiễm Global Namespace.

Ví dụ chuẩn khi viết bộ theo dõi Metric (Early Stopping / Best Loss Tracker) dùng `nonlocal`:
```python
def make_loss_tracker():
    best_loss = float("inf")  # Enclosing scope

    def update(current_loss: float) -> float:
        nonlocal best_loss
        if current_loss < best_loss:
            best_loss = current_loss
        return best_loss

    return update
```

---

### 1.3. Quản Lý Cấu Hình Thí Nghiệm Bằng `dataclasses` (PEP 557)

Trong mã nguồn nghiên cứu sơ cấp, người mới thường khai báo siêu tham số theo 2 cách tai hại:
1. **Khai báo biến Global rời rạc:** `LR = 0.01`, `EPOCHS = 50`, `SEED = 42`. Khi chạy vòng lặp thử nghiệm 10 cấu hình khác nhau, dễ quên reset biến.
2. **Dùng từ điển (`dict`) lỏng lẻo:** `config = {"lr": 0.01, "epcohs": 50}`. Khi gõ nhầm chính tả `"epcohs"` hoặc truy cập thiếu key, lỗi chỉ nổ ra ở giờ huấn luyện thứ 5 thay vì ngay lúc khởi động!

Giải pháp chuẩn mực của Python hiện đại (từ Python 3.7+, PEP 557) là sử dụng **`dataclasses`**.

#### Các cơ chế cốt lõi cần nắm trong `dataclasses`:

1. **Sinh mã tự động (Boilerplate Reduction):**
   Decorator `@dataclass` tự động tạo các phương thức `__init__`, `__repr__` (in cấu hình đẹp mắt để log), và `__eq__` (so sánh 2 cấu hình thí nghiệm có giống hệt nhau không).

2. **Tính bất biến với `frozen=True` (Immutability):**
   Khi thiết lập `@dataclass(frozen=True)`, mọi hành vi gán lại thuộc tính sau khi khởi tạo (`cfg.seed = 100`) sẽ bị chặn đứng ngay lập tức bằng ngoại lệ `FrozenInstanceError`.
   * *Ý nghĩa R&D:* Đảm bảo siêu tham số cấu hình là **hằng số bất biến** trong suốt quá trình chạy một thí nghiệm. Nếu muốn tạo cấu hình mới biến đổi từ cấu hình cũ, dùng hàm `dataclasses.replace(cfg, seed=100)` để tạo một bản sao sạch.

3. **Bẫy Mutable Default Arguments & `field(default_factory=...)`:**
   Trong Python, nếu viết `layers: list[int] = [64, 32]`, tất cả các instance của class sẽ dùng chung **một danh sách duy nhất trong bộ nhớ**. `dataclasses` chủ động chặn lỗi này bằng `ValueError: mutable default ... is not allowed: use default_factory`.
   * *Cách sửa:* Dùng `field(default_factory=lambda: [64, 32])`, hoặc **tốt hơn hết là dùng kiểu bất biến `tuple[int, ...] = (64, 32)`** khi kết hợp với `frozen=True`.
   * *Lưu ý sâu (Shallow vs Deep Immutability):* `frozen=True` chỉ khóa việc gán lại tên thuộc tính (`cfg.tags = ...`), không khóa việc sửa nội dung bên trong một `list` (`cfg.tags.append(...)`). Vì vậy, cấu hình nghiên cứu bất biến nên ưu tiên dùng `tuple` thay cho `list`.

4. **Kiểm tra ràng buộc sớm với `__post_init__` (Fail-Fast Validation):**
   Phương thức `__post_init__` tự động chạy ngay sau `__init__`. Đây là nơi đặt các điều kiện kiểm tra miền giá trị (ví dụ: `learning_rate > 0`, `0 <= dropout < 1`, tổng tỷ lệ `train + val + test == 1.0`).
   * *Kỹ thuật chuẩn hóa trong frozen dataclass:* Bên trong `__post_init__` của lớp `frozen=True`, bạn không thể viết `self.name = self.name.lower()` vì sẽ dính `FrozenInstanceError`. Thay vào đó, phải dùng `object.__setattr__(self, "name", self.name.lower())`.

5. **Tuần tự hóa (Serialization) với `asdict()`:**
   Hàm `dataclasses.asdict(cfg)` chuyển đổi đệ quy toàn bộ cấu hình (kể cả các dataclass lồng nhau) thành `dict` thuần túy của Python, sẵn sàng ghi thành file `.json` lưu cùng kết quả thí nghiệm để tái lập 100% về sau.

---

## 💻 PHẦN 2: HƯỚNG DẪN THỰC HÀNH CHUẨN R&D (50% — 60 PHÚT)

Trong phần này, bạn sẽ xây dựng tệp `Week 1/Day 1/config.py` cho repository `ML-Research-Bootcamp` theo đúng kiến trúc module hóa.

### Bước 1: Thiết kế cấu trúc cấu hình phân tầng (Nested Configs)
Thay vì nhét 20 tham số vào 1 class khổng lồ, hãy chia theo chức năng:
* `DataConfig`: Quản lý tên tập dữ liệu, tỷ lệ chia tập (`split_ratios`), có tráo dữ liệu hay không (`shuffle`).
* `ModelConfig`: Quản lý loại mô hình, kích thước các lớp ẩn (`hidden_dims`), tốc độ học (`learning_rate`), tỷ lệ dropout.
* `ExperimentConfig`: Cấu hình tổng hợp chứa `experiment_id`, `seed`, `epochs`, `batch_size`, lồng ghép `DataConfig` và `ModelConfig`.

### Bước 2: Hiện thực mã nguồn `Week 1/Day 1/config.py`
Tạo tệp `Week 1/Day 1/config.py` với nội dung chuẩn mực (có Type Hints, Docstrings, Validation bằng `math.isclose` cho số thực dấu phẩy động, và hỗ trợ lưu/đọc JSON):

```python
"""
Module quản lý cấu hình thí nghiệm chuẩn R&D.
Đảm bảo tính bất biến (Immutability), kiểm tra ràng buộc sớm (Fail-fast)
và khả năng tuần tự hóa để tái lập thí nghiệm (Reproducibility).
"""

from dataclasses import asdict, dataclass, field
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    """Cấu hình dữ liệu đầu vào và tỷ lệ phân chia tập dữ liệu."""

    dataset_name: str = "california_housing"
    split_ratios: tuple[float, float, float] = (0.7, 0.15, 0.15)
    shuffle: bool = True

    def __post_init__(self) -> None:
        cleaned_name = self.dataset_name.strip()
        object.__setattr__(self, "dataset_name", cleaned_name)
        if not cleaned_name:
            raise ValueError("dataset_name không được để trống.")
        if len(self.split_ratios) != 3:
            raise ValueError("split_ratios phải chứa đúng 3 phần tử (train, val, test).")
        if any(r <= 0.0 for r in self.split_ratios):
            raise ValueError("Mọi tỷ lệ phân chia phải lớn hơn 0.")
        if not math.isclose(sum(self.split_ratios), 1.0, rel_tol=1e-9, abs_tol=1e-9):
            raise ValueError(
                f"Tổng split_ratios phải bằng 1.0, nhận được {sum(self.split_ratios)}."
            )


@dataclass(frozen=True)
class ModelConfig:
    """Cấu hình kiến trúc mô hình và tham số tối ưu hóa."""

    model_type: str = "mlp"
    hidden_dims: tuple[int, ...] = (64, 32)
    learning_rate: float = 1e-3
    dropout: float = 0.1

    def __post_init__(self) -> None:
        normalized_type = self.model_type.strip().lower()
        object.__setattr__(self, "model_type", normalized_type)
        if normalized_type not in {"linear", "logistic", "mlp"}:
            raise ValueError(f"Không hỗ trợ model_type: '{self.model_type}'.")
        if not self.hidden_dims or any(dim <= 0 for dim in self.hidden_dims):
            raise ValueError("hidden_dims phải chứa ít nhất 1 số nguyên dương.")
        if self.learning_rate <= 0.0:
            raise ValueError("learning_rate phải là số dương.")
        if not (0.0 <= self.dropout < 1.0):
            raise ValueError("dropout phải nằm trong nửa khoảng [0.0, 1.0).")


@dataclass(frozen=True)
class ExperimentConfig:
    """Cấu hình tổng thể của một lượt chạy thí nghiệm."""

    experiment_id: str
    seed: int = 42
    epochs: int = 100
    batch_size: int = 32
    data: DataConfig = field(default_factory=DataConfig)
    model: ModelConfig = field(default_factory=ModelConfig)

    def __post_init__(self) -> None:
        if not self.experiment_id.strip():
            raise ValueError("experiment_id không được để trống.")
        if self.seed < 0:
            raise ValueError("seed phải là số nguyên không âm.")
        if self.epochs <= 0:
            raise ValueError("epochs phải lớn hơn 0.")
        if self.batch_size <= 0:
            raise ValueError("batch_size phải lớn hơn 0.")

    def to_json(self, path: str | Path) -> None:
        """Xuất cấu hình thí nghiệm ra tệp JSON để lưu trữ vết nghiên cứu."""
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=2, ensure_ascii=False)

    @classmethod
    def from_json(cls, path: str | Path) -> "ExperimentConfig":
        """Khôi phục nguyên trạng ExperimentConfig từ tệp JSON đã lưu."""
        source = Path(path)
        with source.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        data_raw = raw.pop("data")
        data_raw["split_ratios"] = tuple(data_raw["split_ratios"])
        model_raw = raw.pop("model")
        model_raw["hidden_dims"] = tuple(model_raw["hidden_dims"])

        return cls(
            **raw,
            data=DataConfig(**data_raw),
            model=ModelConfig(**model_raw),
        )
```

### Bước 3: Kiểm thử Pure Function & Tái lập JSON
Trong `Week 1/Day 1/test_config.py` (hoặc notebook trong `Week 1/Day 1/`):
1. Khởi tạo `cfg = ExperimentConfig(experiment_id="baseline_01")`.
2. Kiểm chứng tính bất biến: thử gán `cfg.seed = 99` và xác nhận `FrozenInstanceError` được kích hoạt.
3. Kiểm chứng Validation: thử tạo `DataConfig(split_ratios=(0.7, 0.2, 0.2))` (tổng 1.1) và xác nhận `ValueError` chặn ngay lập tức.
4. Xuất `cfg.to_json("configs/baseline_01.json")`, đọc lại bằng `ExperimentConfig.from_json(...)` và kiểm tra `assert cfg == cfg_loaded`.

---

## 🧠 PHẦN 3: ACTIVE RECALL & RESEARCH LAB LOG (20% — 24 PHÚT)

### 3.1. Câu hỏi tự kiểm tra (Active Recall)
Không nhìn lại giáo án, hãy tự trả lời ra giấy hoặc file log:
1. **Tại sao biến toàn cục (Global Variables) là nguyên nhân gây sai lệch kết quả thí nghiệm trong ML Research?**
   * *Điểm cốt lõi cần đạt:*
     - **Silent State Mutation (Đột biến trạng thái ngầm):** Một hàm phụ có thể âm thầm sửa giá trị biến toàn cục (ví dụ `learning_rate` bị nhân hệ số decay hoặc danh sách `losses` bị append nối tiếp từ thí nghiệm cũ sang thí nghiệm mới).
     - **Out-of-order Execution trong Jupyter Notebook:** Khi chạy Cell 4 $\rightarrow$ Cell 2 $\rightarrow$ Cell 4, biến toàn cục giữ trạng thái từ lần chạy trước, khiến kết quả hoàn toàn không thể tái lập khi chạy lại từ đầu (`Restart & Run All`).
     - **Hidden Dependencies (Phụ thuộc ẩn):** Hàm không khai báo tham số đầu vào rõ ràng trong chữ ký hàm (function signature), khiến người đọc và unit test không thể cô lập được hành vi của hàm.
     - **Xung đột khi chạy song song (Cross-Fold / Multi-seed Contamination):** Khi chạy 5-Fold Cross-Validation hoặc thử nhiều hạt giống ngẫu nhiên (seeds), các tiến trình dùng chung trạng thái toàn cục sẽ ghi đè lẫn nhau.

### 3.2. Mẫu ghi nhật ký `Week 1/Day 1/lab_log.md`
Mở tệp nhật ký ngày 1 và ghi chép theo mẫu sau:
```markdown
## W01-D1: Namespace, LEGB & Experiment Config
- **Khái niệm cốt lõi đã nắm:** Python xác định scope ở thời điểm biên dịch bytecode (compile-time), không phải runtime. Dùng `frozen=True` + `tuple` để đạt bất biến thực sự.
- **Thử nghiệm đã chạy:** Đã thiết kế `Week 1/Day 1/config.py`, test thành công vòng lặp lưu/đọc JSON (`cfg == cfg_loaded`) và bắt lỗi `FrozenInstanceError`, `ValueError`.
- **Bài học rút ra:** Tuyệt đối dùng `math.isclose()` thay cho `==` khi kiểm tra tổng các tỷ lệ số thực (`0.7 + 0.15 + 0.15`), tránh lỗi dấu phẩy động IEEE 754.
```

### 3.3. Lệnh Git Commit cuối buổi học
```bash
git add "Week 1/Day 1/"
git commit -m "feat(w01-d1): add immutable ExperimentConfig with validation and JSON serialization"
git push
```

---

## 📚 TÀI LIỆU THAM KHẢO CHUẨN XÁC
1. **Python Official Documentation:** *Execution model — Naming and binding* ([docs.python.org/3/reference/executionmodel.html](https://docs.python.org/3/reference/executionmodel.html)).
2. **PEP 557 – Data Classes:** Tài liệu thiết kế chuẩn mực của `dataclasses` trong Python ([peps.python.org/pep-0557](https://peps.python.org/pep-0557/)).
3. **Python `dataclasses` Module Reference:** ([docs.python.org/3/library/dataclasses.html](https://docs.python.org/3/library/dataclasses.html)).
