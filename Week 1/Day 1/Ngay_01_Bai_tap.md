# 📝 BÀI TẬP RÈN LUYỆN — W01-D1 (NGÀY 01)

> **Chủ đề:** Cơ chế Namespace, Quy tắc LEGB & Quản lý Cấu hình Thí nghiệm bằng `dataclasses`  
> **Yêu cầu:** Hoàn thành độc lập cả 5 bài tập dưới đây trước khi mở tệp đáp án chi tiết.

---

### Bài 1: Phân Tích Cơ Chế Scoping & Quy Tắc LEGB

Cho đoạn mã Python sau:

```python
lr = 0.01

def run_step(decay: float) -> float:
    if decay > 0:
        lr = lr * decay
    return lr

print(run_step(0.5))
```

Khi thực thi đoạn mã trên bằng trình thông dịch Python 3, kết quả nào sau đây xảy ra?

* **A.** In ra giá trị `0.005` vì `lr` được tìm thấy ở phạm vi Global theo quy tắc LEGB trước khi tính `lr * decay`.
* **B.** In ra giá trị `0.01` vì `lr` trong hàm chỉ là bản sao cục bộ và không ảnh hưởng tới biến toàn cục bên ngoài.
* **C.** Chương trình ném ngoại lệ `UnboundLocalError` tại dòng `lr = lr * decay`.
* **D.** Chương trình ném ngoại lệ `NameError: name 'lr' is not defined` vì thiếu từ khóa `global lr`.

---

### Bài 2: Phạm Vi Bao Ngoài (Enclosing Scope) & Closure Trong Theo Dõi Huấn Luyện

Một kỹ sư ML viết hàm tạo bộ theo dõi dừng sớm (Early Stopping Tracker) cho quá trình huấn luyện mô hình như sau:

```python
def make_early_stopper(patience: int):
    best_loss = float("inf")
    counter = 0

    def check(val_loss: float) -> bool:
        nonlocal best_loss, counter
        if val_loss < best_loss:
            best_loss = val_loss
            counter = 0
        else:
            counter += 1
        return counter >= patience

    return check

stopper = make_early_stopper(patience=2)
results = [stopper(v) for v in [0.5, 0.4, 0.45, 0.48]]
print(results)
```

Phát biểu nào sau đây mô tả **CHÍNH XÁC** kết quả đầu ra và cơ chế vận hành của đoạn mã trên?

* **A.** Kết quả in ra `[False, False, False, True]`, và từ khóa `nonlocal` là bắt buộc để hàm `check` có thể gán lại giá trị mới cho `best_loss` và `counter` ở phạm vi Enclosing.
* **B.** Chương trình ném ngoại lệ `UnboundLocalError` vì `best_loss` và `counter` bị hủy ngay sau khi hàm `make_early_stopper` thực thi xong lệnh `return check`.
* **C.** Kết quả in ra `[False, False, True, True]` vì biến `counter` được tăng lên `1` ngay ở lần gọi đầu tiên với `0.5`.
* **D.** Nếu thay từ khóa `nonlocal` bằng `global`, chương trình vẫn chạy ra đúng kết quả `[False, False, False, True]` mà không gặp lỗi gì.

---

### Bài 3: Bẫy Mutable Fields & Tính Bất Biến Trong `dataclasses`

Xét đoạn định nghĩa cấu hình siêu tham số bằng `dataclasses` dưới đây:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class HyperParams:
    lr: float = 0.01
    layers: list[int] = field(default_factory=lambda: [64, 32])

hp = HyperParams()
```

Sau khi khởi tạo đối tượng `hp`, điều gì xảy ra nếu trong quá trình chạy thí nghiệm có một hàm vô tình thực hiện lần lượt hai câu lệnh sau:
1. Lệnh 1: `hp.layers.append(16)`
2. Lệnh 2: `hp.lr = 0.001`

Hãy chọn nhận định đúng nhất:

* **A.** Cả Lệnh 1 và Lệnh 2 đều ném ngoại lệ `FrozenInstanceError` vì class được khai báo với tham số `frozen=True`.
* **B.** Ngay tại thời điểm định nghĩa class `HyperParams`, Python đã ném ngoại lệ `ValueError` vì `frozen=True` không cho phép sử dụng kiểu dữ liệu `list` làm thuộc tính.
* **C.** Lệnh 1 thực thi thành công và làm thay đổi thuộc tính `hp.layers` thành `[64, 32, 16]`; Lệnh 2 ném ngoại lệ `FrozenInstanceError`.
* **D.** Lệnh 1 ném ngoại lệ `AttributeError` vì `layers` là đối tượng bất biến; Lệnh 2 thực thi thành công nhưng chỉ thay đổi bản sao cục bộ.

---

### Bài 4: Thực Hành Refactoring — Khử Biến Toàn Cục & Rò Rỉ Trạng Thái

Đoạn mã dưới đây mô phỏng một kịch bản thí nghiệm Machine Learning mắc nhiều lỗi thiết kế nghiêm trọng về quản lý biến toàn cục (Global State Contamination):

```python
LEARNING_RATE = 0.1
EPOCHS = 3
DECAY_RATE = 0.5
LOSS_HISTORY = []

def run_training_experiment():
    global LEARNING_RATE
    current_loss = 1.0
    for _ in range(EPOCHS):
        current_loss = current_loss * (1.0 - LEARNING_RATE)
        LOSS_HISTORY.append(round(current_loss, 6))
        LEARNING_RATE = LEARNING_RATE * DECAY_RATE
    return current_loss

# Lần chạy thí nghiệm 1
loss_run_1 = run_training_experiment()
print("Run 1:", loss_run_1, "History:", LOSS_HISTORY)

# Lần chạy thí nghiệm 2 (Kỳ vọng chạy lại độc lập với cùng cấu hình ban đầu)
loss_run_2 = run_training_experiment()
print("Run 2:", loss_run_2, "History:", LOSS_HISTORY)
```

**Yêu cầu thực hành:**
1. Chỉ rõ 2 nguyên nhân cụ thể trong đoạn mã trên khiến `loss_run_2` và `LOSS_HISTORY` ở Lần chạy 2 bị sai lệch hoàn toàn so với Lần chạy 1.
2. Viết lại toàn bộ đoạn mã trên theo kiến trúc module sạch:
   - Định nghĩa một lớp cấu hình bất biến `TrainingRunConfig` bằng `@dataclass(frozen=True)` chứa các tham số `learning_rate`, `epochs`, `decay_rate`.
   - Viết lại hàm `train_simulation(config: TrainingRunConfig) -> dict[str, object]` hoạt động như một hàm thuần khiết (Pure Function): không đọc hay sửa bất kỳ biến toàn cục nào, trả về từ điển chứa `"final_lr"` và `"loss_history"` (dạng `tuple`).
   - Chứng minh tính tái lập: khi gọi `train_simulation(cfg)` hai lần liên tiếp với cùng một `cfg`, hai kết quả trả về phải bằng nhau tuyệt đối (`res1 == res2`).

---

### Bài 5: Thiết Kế Hệ Thống Cấu Hình Nghiên Cứu Chuẩn R&D

Hãy xây dựng một module Python hoàn chỉnh (đặt tên logic là `config.py`) bao gồm 3 lớp `@dataclass(frozen=True)` lồng nhau để quản lý cấu hình cho một pipeline huấn luyện ML thực tế:

1. **`DataConfig`:**
   - `dataset_name: str`: Bắt buộc không được rỗng sau khi cắt khoảng trắng hai đầu (`strip()`), đồng thời phải tự động lưu giá trị đã cắt khoảng trắng.
   - `split_ratios: tuple[float, float, float]`: Mặc định `(0.7, 0.15, 0.15)`. Bắt buộc gồm đúng 3 số thực lớn hơn `0`, và tổng của chúng bằng `1.0` (chấp nhận sai số dấu phẩy động ở mức `1e-9`).

2. **`ModelConfig`:**
   - `optimizer: str`: Mặc định `"adam"`. Tự động chuẩn hóa thành chữ thường và cắt khoảng trắng hai đầu. Chỉ chấp nhận các giá trị trong tập `{"sgd", "adam", "adamw"}`.
   - `learning_rate: float`: Mặc định `1e-3`. Bắt buộc lớn hơn `0`.
   - `hidden_dims: tuple[int, ...]`: Mặc định `(128, 64)`. Bắt buộc chứa ít nhất 1 phần tử và mọi phần tử đều là số nguyên dương.

3. **`ExperimentConfig`:**
   - `experiment_id: str`: Bắt buộc không được rỗng.
   - `seed: int`: Mặc định `42`. Bắt buộc $\ge 0$.
   - `batch_size: int`: Mặc định `32`. Bắt buộc $> 0$.
   - `data: DataConfig` và `model: ModelConfig`: Tham số lồng nhau có giá trị mặc định khởi tạo an toàn.
   - Phương thức `save_json(self, filepath: str | Path) -> None`: Tự động tạo thư mục cha nếu chưa tồn tại và xuất toàn bộ cấu hình ra tệp JSON.
   - Phương thức lớp `load_json(cls, filepath: str | Path) -> "ExperimentConfig"`: Đọc tệp JSON và khôi phục lại đúng đối tượng `ExperimentConfig` (đảm bảo kiểm tra `exp == exp_loaded` trả về `True`).

4. Viết đoạn mã kiểm thử ở khối `if __name__ == "__main__":` để chứng minh:
   - Chuẩn hóa chuỗi (`"  housing  "`, `" AdamW "`) hoạt động chính xác bên trong frozen dataclass.
   - Các ràng buộc sai (như tổng `split_ratios` khác `1.0` hoặc `optimizer="rmsprop"`) bị chặn lại bằng `ValueError`.
   - Lưu và nạp JSON bảo toàn 100% tính bình đẳng đối tượng (`exp == exp_loaded`).
