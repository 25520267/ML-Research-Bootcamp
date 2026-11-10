# 🚀 Machine Learning Research Bootcamp: Lộ Trình 18 Tuần (The Beginner's Path to AI Research)

> **Tác giả lộ trình gốc:** Nguyen Minh Nhut – Chief R&D Engineer  
> **Định hướng phát triển:** Đào tạo tư duy nghiên cứu (Research Mindset), tính minh bạch toán học (Mathematical Rigor), khoa học đánh giá (Evaluation Science) và tính tái lập (Reproducibility).  
> **Nguyên tắc cốt lõi:** *"Fundamentals over Complexity"* (Nền tảng vững chắc luôn đánh bại sự phức tạp bề ngoài).

---

## 📌 MỤC LỤC
1. [Tại Sao Học Lý Thuyết ML Lại Cần GitHub?](#1-tại-sao-học-lý-thuyết-ml-lại-cần-github)
2. [Cấu Trúc Thư Mục GitHub Repository Chuẩn R&D](#2-cấu-trúc-thư-mục-github-repository-chuẩn-rd)
3. [Quy Tắc Học Tập Hàng Ngày (Khung Thời Gian 30 - 50 - 20)](#3-quy-tắc-học-tập-hàng-ngày-khung-thời-gian-30---50---20)
4. [Bảng Liên Hệ Đồng Bộ Với Sách Hands-On Machine Learning](#4-bảng-liên-hệ-đồng-bộ-với-sách-hands-on-machine-learning)
5. [Lộ Trình Chi Tiết Từng Tuần, Từng Ngày & Checklist](#5-lộ-trình-chi-tiết-từng-tuần-từng-ngày--checklist)
   - [Phase I: The Language & The Math Engine (Tuần 1 – Tuần 4)](#phase-i-the-language--the-math-engine-tuần-1--tuần-4)
   - [Phase II: Statistical Rigor & Foundations (Tuần 5 – Tuần 7)](#phase-ii-statistical-rigor--foundations-tuần-5--tuần-7)
   - [Phase III: The Machine Learning Core (Tuần 8 – Tuần 10)](#phase-iii-the-machine-learning-core-tuần-8--tuần-10)
   - [Phase IV: Rigorous Evaluation & Data Pathologies (Tuần 11 – Tuần 13)](#phase-iv-rigorous-evaluation--data-pathologies-tuần-11--tuần-13)
   - [Phase V: Synthesis & Advanced Basics (Tuần 14 – Tuần 18)](#phase-v-synthesis--advanced-basics-tuần-14--tuần-18)
6. [Bảng Cảnh Báo Cạm Bẫy Phổ Biến & Tâm Lý Nghiên Cứu](#6-bảng-cảnh-báo-cạm-bẫy-phổ-biến--tâm-lý-nghiên-cứu)

---

## 1. TẠI SAO HỌC LÝ THUYẾT ML LẠI CẦN GITHUB?

Nhiều người nghĩ GitHub chỉ dành cho lập trình viên phần mềm (Software Engineers). Nhưng trong **Nghiên cứu Machine Learning (ML Research)**, GitHub đóng vai trò là **"Phòng thí nghiệm kỹ thuật số" (Digital Lab Notebook)**:

1. **Hiện thực hóa công thức toán (Code as Mathematical Proof):**
   * Đọc công thức đạo hàm $\frac{\partial \mathcal{L}}{\partial \mathbf{w}}$ trên giấy bạn chỉ hiểu được 30%. Nhưng khi chuyển thành mã NumPy `grad = (X.T @ (y_pred - y)) / m`, bạn buộc phải hiểu đúng số chiều (shapes), ma trận chuyển vị, và sự ổn định số học (tránh chia cho 0 hoặc tràn số). GitHub là nơi lưu giữ các chứng minh bằng mã nguồn này.
2. **Tính tái lập (Reproducibility) – Bản chất của khoa học:**
   * Trong nghiên cứu, kết quả sẽ vô giá trị nếu người khác (hoặc chính bạn sau vài tháng) chạy lại mà không ra đúng con số đó. Git giúp bạn "đóng băng" trạng thái code, siêu tham số và phiên bản thư viện tại thời điểm đạt kết quả.
3. **Nhật ký phòng thí nghiệm (Research Lab Notebook):**
   * Các tệp Markdown trong repo không dùng để quảng bá phần mềm, mà để ghi chép giả thuyết (Hypothesis), vẽ đồ thị phân tích lỗi (Failure Analysis), và ghi lại lý do tại sao một thử nghiệm thất bại.
4. **Hồ sơ năng lực học thuật giao tiếp với Mentor:**
   * Mentor (Chief R&D Engineer) không đánh giá bạn qua lời nói, mà đánh giá qua lịch sử commit đều đặn, cấu trúc code module hóa, và tư duy phản biện thể hiện trong các file log thí nghiệm.

---

## 2. CẤU TRÚC THƯ MỤC GITHUB REPOSITORY CHUẨN R&D

Tạo thư mục dự án trên máy và đẩy lên GitHub theo đúng cấu trúc sau:

```text
ml-research-foundations/
├── README.md                      # Bảng điều khiển tiến độ (Dashboard checklist 18 tuần)
├── requirements.txt               # Danh sách thư viện và phiên bản chính xác (Reproducibility)
├── .gitignore                     # Bỏ qua các file rác, cache (.ipynb_checkpoints, __pycache__)
├── docs/                          # Ghi chú lý thuyết & toán học chuyên sâu
│   ├── math_notes/                # Chứng minh công thức, giải tích, đại số tuyến tính
│   └── book_summaries/            # Báo cáo tóm tắt các chương sách Hands-On ML
├── src/                           # Thư viện thuật toán tự code từ đầu (Scratch Implementation)
│   ├── __init__.py
│   ├── linear_algebra.py          # Vector, Matrix operations
│   ├── optimizers.py              # Gradient Descent, Adam (tự viết bằng NumPy)
│   ├── losses.py                  # MSE, Cross-Entropy, Huber Loss (tự viết)
│   └── models/                    # KNN, Logistic Regression, K-Means (tự viết)
├── experiments/                   # Jupyter Notebooks thực nghiệm & kiểm chứng
│   ├── week_01_generators_benchmark.ipynb
│   ├── week_03_gradient_descent_surface.ipynb
│   └── ...
└── lab_logs/                      # Nhật ký thí nghiệm (Failure analysis & Insights)
    ├── week_01_log.md
    └── ...
```

---

## 3. QUY TẮC HỌC TẬP HÀNG NGÀY (KHUNG THỜI GIAN 30 - 50 - 20)

Mỗi buổi học duy trì đều đặn **2 tiếng/ngày**, 5 ngày/tuần:

* **30% Thời gian (36 phút) – Đọc & Chứng minh Toán (Math & Concept):**
  * Đọc giáo trình, hiểu bản chất trực quan hình học, tự tay phái sinh/chứng minh công thức ra giấy nháp trước khi chạm vào bàn phím.
* **50% Thời gian (60 phút) – Code Thực Hành (Scratch Code & Pipeline):**
  * Tự viết mã nguồn bằng NumPy thuần (không gọi thư viện black-box) lưu vào `src/` hoặc xây dựng notebook thực nghiệm trong `experiments/`.
* **20% Thời gian (24 phút) – Tự Kiểm Tra & Ghi Chép (Active Recall & Lab Log):**
  * Trả lời câu hỏi phản biện, vẽ biểu đồ trực quan hóa, commit code lên GitHub và ghi lại 3 bài học/lỗi sai quan trọng vào `lab_logs/`.

---

## 4. BẢNG LIÊN HỆ ĐỒNG BỘ VỚI SÁCH HANDS-ON MACHINE LEARNING

Tận dụng việc làm báo cáo trên lớp để học song song, tiết kiệm thời gian:

| Tuần Lộ Trình | Nội Dung Nghiên Cứu | Chương Tương Ứng Trong Sách Géron |
| :--- | :--- | :--- |
| **Tuần 1, 2** | Pythonic Logic, Memory & Data Structures | Nền tảng lập trình hỗ trợ toàn bộ sách |
| **Tuần 3, 4** | Gradient Descent, Ma trận, Calculus | **Chương 4:** Training Models (Linear, Polynomial, GD) |
| **Tuần 5** | Phân tích phân phối, EDA, Skewness | **Chương 2:** End-to-End Machine Learning Project |
| **Tuần 8** | Loss Engineering (Log-Loss, Softmax, Hinge) | **Chương 4:** Logistic Regression, Softmax Regression |
| **Tuần 9** | Discriminative Modeling (Logistic, KNN, Trees) | **Chương 3:** Classification & **Chương 6:** Decision Trees |
| **Tuần 10** | Unsupervised Discovery (K-Means, PCA) | **Chương 8:** Dimensionality Reduction & **Chương 9:** Unsupervised |
| **Tuần 11** | Metrics Deep-Dive (Precision, Recall, ROC, PR) | **Chương 3:** Classification (Performance Measures) |
| **Tuần 12, 13** | Validation, Target Leakage, Pipeline, SMOTE | **Chương 2:** Data Preparation & Pipeline |
| **Tuần 14** | Bias-Variance Tradeoff, Learning Curves | **Chương 4:** Learning Curves & Regularization |

---

## 5. LỘ TRÌNH CHI TIẾT TỪNG TUẦN, TỪNG NGÀY & CHECKLIST

---

### PHASE I: THE LANGUAGE & THE MATH ENGINE (Tuần 1 – Tuần 4)
> **Mục tiêu chặng:** Xây dựng cỗ máy tính toán hiệu năng cao bằng Python/NumPy và làm chủ ngôn ngữ giải tích/đại số của dữ liệu.

#### 🎯 Tuần 1: Pythonic Logic & Kiến Trúc Module Cho Nghiên Cứu
* **Mục tiêu:** Thoát khỏi tư duy viết script lộn xộn trong notebook; làm chủ Decorators, Generators và cấu trúc code DRY (*Don't Repeat Yourself*).
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Cơ chế Namespace & Scoping (LEGB rule) trong Python.
  * *50% Thực hành:* Viết module quản lý cấu trúc tham số thí nghiệm dùng `dataclasses`.
  * *20% Lab Log:* Giải thích: Tại sao biến toàn cục (global variables) là nguyên nhân gây sai lệch kết quả thí nghiệm?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Hiểu Closure và cú pháp Decorator `@wraps`.
  * *50% Thực hành:* Viết decorator `@time_it` (đo thời gian huấn luyện) và `@catch_oom` (bắt lỗi tràn RAM).
  * *20% Lab Log:* Chạy test decorator trên 3 hàm và lưu kết quả đo đạc vào `lab_logs/week_01_log.md`.
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Cơ chế Generator & từ khóa `yield` vs `return`. Quản lý bộ nhớ RAM.
  * *50% Thực hành:* Viết hàm `data_batch_streamer(file_path, batch_size)` đọc file CSV lớn từng batch.
  * *20% Lab Log:* Đo dung lượng RAM tiêu thụ khi dùng Generator vs load toàn bộ List vào RAM (`sys.getsizeof`).
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Tư duy OOP: Class cơ sở, magic methods `__call__`, `__repr__`.
  * *50% Thực hành:* Xây dựng class `BaseEstimator` mô phỏng Scikit-learn có 2 phương thức trừu tượng `fit()` và `predict()`.
  * *20% Lab Log:* Active Recall: Sự khác nhau giữa method thông thường, classmethod và staticmethod trong ML Pipeline?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Type hints (`typing`) và Docstrings chuẩn Google.
  * *50% Thực hành:* Refactor toàn bộ code tuần này vào `src/`, kiểm tra định dạng bằng `flake8`/`black`.
  * *20% Lab Log:* **Milestone Test 1:** Commit repo sạch lên GitHub, chứng minh hàm stream dữ liệu hoạt động ổn định.
* ⚠️ **Bẫy phổ biến:** Sa đà vào các framework web hoặc cú pháp metaprogramming quá sâu. Chỉ tập trung vào decorator đo lường và generator tiết kiệm RAM.

---

#### 🎯 Tuần 2: Độ Phức Tạp Tính Toán & Cấu Trúc Dữ Liệu Trong ML
* **Mục tiêu:** Làm chủ Big-O (Time/Space Complexity); hiểu cấu trúc bảng băm, cây quyết định và bố cục bộ nhớ của NumPy.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Big-O Notation: Phân tích độ phức tạp $O(1), O(\log N), O(N), O(N^2)$.
  * *50% Thực hành:* Đo thời gian thực tế của các thao tác trên Python `list`, `dict`, `set`.
  * *20% Lab Log:* Vẽ đồ thị thời gian tìm kiếm phần tử giữa `list` và `set` khi $N$ tăng từ $10^2 \to 10^6$.
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Bảng băm (Hash Tables): Hàm băm và cách xử lý xung đột (Chaining vs Open Addressing).
  * *50% Thực hành:* Viết một cấu trúc Hash Map mini từ đầu bằng Python thuần.
  * *20% Lab Log:* Ghi chú: Tại sao thao tác tra cứu nhãn trong tập dữ liệu lớn bắt buộc phải đạt độ phức tạp $O(1)$?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Cấu trúc Cây (Trees): Binary Trees, phép duyệt cây đệ quy.
  * *50% Thực hành:* Viết class `Node` biểu diễn một nút rẽ nhánh và hàm duyệt cây tìm kiếm.
  * *20% Lab Log:* Vẽ sơ đồ một cây quyết định 2 tầng trên giấy nháp và ánh xạ thành code.
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Bố cục bộ nhớ của NumPy: Mảng C-contiguous vs Fortran-contiguous, khái niệm Strides.
  * *50% Thực hành:* Đo tốc độ tính tổng ma trận theo hàng vs theo cột để thấy rõ ảnh hưởng của CPU Cache.
  * *20% Lab Log:* Giải thích: Tại sao mảng NumPy nhanh hơn danh sách Python từ 50 đến 100 lần?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Bài toán tìm kiếm láng giềng: Brute-force $O(N)$ vs Spatial Trees ($KD-Tree$).
  * *50% Thực hành:* Viết thuật toán tìm điểm gần nhất dạng Brute-force và đo sự bùng nổ thời gian khi dữ liệu tăng.
  * *20% Lab Log:* **Milestone Test 2:** Viết báo cáo ngắn về Big-O của các thuật toán ML cơ bản nộp vào `docs/math_notes/`.
* ⚠️ **Bẫy phổ biến:** Học cấu trúc dữ liệu theo kiểu luyện thi thuật toán đánh đố. Hãy tập trung vào: *Dữ liệu nằm trên RAM thế nào và chi phí truy cập ra sao*.

---

#### 🎯 Tuần 3: Đại Số Tuyến Tính & Trực Quan Hóa Không Gian Vector
* **Mục tiêu:** Vector hóa 100% (xóa sổ vòng lặp `for`); hiểu hình học của ma trận, trị riêng và SVD.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Vector, Dot Product, Chuẩn $L_1, L_2$, Ý nghĩa hình học của Cosine Similarity.
  * *50% Thực hành:* Tự code hàm tính $L_1, L_2$ norm và Cosine Similarity bằng NumPy trong `src/linear_algebra.py`.
  * *20% Lab Log:* Chứng minh hình học: Tại sao Dot Product đo lường mức độ đồng hướng của 2 vector đặc trưng?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Ma trận như một phép biến đổi không gian (Linear Transformation), Ma trận nghịch đảo.
  * *50% Thực hành:* Dùng NumPy biến đổi một lưới điểm 2D (xoay, co giãn) và vẽ đồ thị trước/sau biến đổi.
  * *20% Lab Log:* Khi nào ma trận không khả nghịch (Singular Matrix) và điều đó gây lỗi gì trong hồi quy tuyến tính?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Vectorization: Nguyên lý thay thế vòng lặp bằng ma trận hóa.
  * *50% Thực hành:* Chuyển đổi hàm tính khoảng cách Euclid giữa $N$ điểm từ vòng lặp 2 tầng `for` thành 1 dòng code ma trận.
  * *20% Lab Log:* Đo benchmark: So sánh tốc độ giữa vòng lặp `for` và mã đã vector hóa trên ma trận $1000 \times 100$.
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Eigenvalues & Eigenvectors: Ý nghĩa các trục không bị thay đổi hướng khi biến đổi ma trận.
  * *50% Thực hành:* Tính trị riêng và vector riêng bằng `np.linalg.eig`, vẽ các vector riêng đè lên đám mây điểm 2D.
  * *20% Lab Log:* Trả lời: Trục vector riêng có trị riêng lớn nhất nói lên điều gì về phương sai dữ liệu?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Phân rã giá trị suy biến SVD ($A = U \Sigma V^T$).
  * *50% Thực hành:* Viết code dùng SVD để nén một bức ảnh xám (giữ lại top $k$ giá trị suy biến lớn nhất).
  * *20% Lab Log:* **Milestone Test 3:** Hoàn thành bài toán nén ảnh SVD, hiển thị trực quan các mức nén $k=5, 20, 50$.
* ⚠️ **Bẫy phổ biến:** Nhìn ma trận như một bảng số tĩnh vô hồn. Hãy luôn tưởng tượng: *Ma trận là một hành động bẻ cong hoặc kéo dãn không gian*.

---

#### 🎯 Tuần 4 (Tuần đệm): Giải Tích Đa Biến & Tối Ưu Hóa (Calculus & Optimization)
* **Mục tiêu:** Hiểu sâu sắc cách máy tính học thông qua việc trượt dốc trên bề mặt hàm mất mát (Gradient Descent). *(Đọc song song Chương 4 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Đạo hàm riêng (Partial Derivatives) và Vector Gradient $\nabla f$.
  * *50% Thực hành:* Tính tay đạo hàm riêng của $f(x, y) = x^2 + 3xy + y^2$ trên giấy; viết code kiểm tra lại bằng sai phân hữu hạn (Finite Difference).
  * *20% Lab Log:* Active Recall: Tại sao Gradient luôn chỉ về hướng hàm số tăng nhanh nhất?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Đạo hàm chuỗi (Chain Rule) đa biến. Ma trận Jacobian.
  * *50% Thực hành:* Vẽ Computation Graph của hàm $L = (wx + b - y)^2$ và tính tay $\frac{\partial L}{\partial w}, \frac{\partial L}{\partial b}$.
  * *20% Lab Log:* Ghi chú: Tại sao Chain Rule là xương sống của thuật toán Lan truyền ngược (Backpropagation)?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Thuật toán Gradient Descent: Learning rate $\eta$, cơ chế cập nhật trọng số.
  * *50% Thực hành:* Tự viết thuật toán Gradient Descent 1D tìm cực tiểu của $f(x) = (x-3)^2 + 2$.
  * *20% Lab Log:* Vẽ đồ thị các bước nhảy hội tụ khi $\eta$ quá nhỏ, vừa vặn, và quá lớn (phân kỳ).
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Bề mặt mất mát (Loss Landscape): Điểm cực tiểu cục bộ (Local Minima) và Điểm yên ngựa (Saddle Points).
  * *50% Thực hành:* Viết Gradient Descent đa biến cho bài toán Linear Regression bằng NumPy trong `src/optimizers.py`.
  * *20% Lab Log:* Dùng Matplotlib vẽ 3D Contour Plot bề mặt mất mát dạng cái bát và vẽ đường trượt dốc của thuật toán.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Đối chiếu lý thuyết với Chương 4 sách *Hands-On Machine Learning*.
  * *50% Thực hành:* Xây dựng class `MyLinearRegression` hoàn chỉnh fit dữ liệu tổng hợp bằng Gradient Descent tự viết.
  * *20% Lab Log:* **Milestone Phase I:** So sánh hệ số trọng số tự tìm được với `sklearn.linear_model.LinearRegression`. Kết quả phải khớp nhau đến chữ số thập phân thứ 4.

---

### PHASE II: STATISTICAL RIGOR & FOUNDATIONS (Tuần 5 – Tuần 7)
> **Mục tiêu chặng:** Đọc và hiểu dữ liệu dưới góc nhìn xác suất; kiểm định xem mô hình tốt thật hay chỉ là ăn may do nhiễu.

#### 🎯 Tuần 5: Phân Tích Phân Phối Dữ Liệu & Nghiêm Ngặt EDA
* **Mục tiêu:** Hiểu hình dạng phân phối thực tế của dữ liệu; nhận diện nhiễu và kiểm tra giả định chuẩn tắc. *(Đọc song song Chương 2 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Thước đo trung tâm & phân tán: Mean, Median, Mode, Variance, Standard Deviation.
  * *50% Thực hành:* Viết code thêm 1 outlier cực lớn vào mảng dữ liệu và so sánh độ trôi của Mean vs Median.
  * *20% Lab Log:* Phân tích: Tại sao báo cáo mức lương trung bình (Mean) thường gây hiểu lầm so với trung vị (Median)?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Hình dạng phân phối: Skewness (độ lệch) & Kurtosis (độ nhọn/đuôi dày).
  * *50% Thực hành:* Dùng `scipy.stats` tính Skewness và Kurtosis trên dataset California Housing.
  * *20% Lab Log:* Nhận diện 2 đặc trưng bị lệch phải (Right-skewed) nặng trong tập dữ liệu nhà đất.
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Hàm mật độ xác suất (PDF) & Hàm phân phối tích lũy (CDF). Phân phối Gaussian.
  * *50% Thực hành:* Vẽ đồ thị PDF và CDF của phân phối chuẩn bằng Seaborn; tính xác suất trong khoảng $\mu \pm 2\sigma$.
  * *20% Lab Log:* Active Recall: Tại sao nhiều mô hình tuyến tính hoạt động kém khi dữ liệu bị lệch đuôi dày?
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Kiểm tra tính chuẩn tắc (Normality Test) bằng Q-Q Plot. Các phép biến đổi dữ liệu.
  * *50% Thực hành:* Áp dụng Log-transform và Box-Cox để nắn biến bị lệch về dạng phân phối chuẩn; vẽ lại Q-Q plot.
  * *20% Lab Log:* Lưu biểu đồ trước và sau khi biến đổi vào `lab_logs/week_05_log.md`.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Cấu trúc một bản báo cáo EDA chuẩn mực trong nghiên cứu.
  * *50% Thực hành:* Hoàn thiện notebook EDA chuyên sâu cho 1 dataset thực tế: thống kê, kiểm tra missing, vẽ ma trận tương quan.
  * *20% Lab Log:* **Milestone Test 5:** Trình bày 3 phát hiện bất thường về dữ liệu từ bài EDA trong file markdown.
* ⚠️ **Bẫy phổ biến:** Coi EDA chỉ là gọi `df.describe()` rồi vẽ vài biểu đồ màu mè. EDA của nghiên cứu là tìm xem: *Dữ liệu có vi phạm các giả định toán học của mô hình không*.

---

#### 🎯 Tuần 6: Thống Kê Suy Diễn & Tính Hợp Lệ Khoa Học (Statistical Inference)
* **Mục tiêu:** Phân biệt "nhiễu ngẫu nhiên" và "hiệu ứng thực sự"; làm chủ p-value và cạm bẫy p-hacking.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Quần thể (Population) vs Mẫu (Sample). Sai số chuẩn (Standard Error: $SE = \frac{\sigma}{\sqrt{n}}$).
  * *50% Thực hành:* Mô phỏng rút 1000 mẫu ngẫu nhiên từ quần thể và tính độ biến thiên của trung bình mẫu.
  * *20% Lab Log:* Chứng minh bằng thực nghiệm: Khi kích thước mẫu $n$ tăng gấp 4 thì sai số chuẩn $SE$ giảm đi một nửa.
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Định lý Giới hạn Trung tâm (Central Limit Theorem - CLT).
  * *50% Thực hành:* Code mô phỏng CLT: Lấy mẫu từ phân phối xúc xắc (đều) và chứng minh phân phối trung bình mẫu tiệm cận chuẩn.
  * *20% Lab Log:* Ghi chú: Tại sao CLT cho phép áp dụng các kiểm định tham số ngay cả khi dữ liệu gốc không chuẩn?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Kiểm định giả thuyết ($H_0, H_1$), Mức ý nghĩa $\alpha=0.05$, Bản chất của p-value.
  * *50% Thực hành:* Thực hiện kiểm định t-test 2 mẫu độc lập bằng `scipy.stats.ttest_ind`.
  * *20% Lab Log:* Phản biện: Câu nói *"p-value = 0.03 nghĩa là khả năng giả thuyết vô hiệu $H_0$ đúng là 3%"* đúng hay sai? Tại sao?
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Sai lầm loại I ($\alpha$), Sai lầm loại II ($\beta$), Power Analysis. Gian lận p-hacking.
  * *50% Thực hành:* Viết code mô phỏng p-hacking: Chạy 100 phép thử ngẫu nhiên vô nghĩa cho đến khi "bắt gặp" 1 lần có $p < 0.05$.
  * *20% Lab Log:* Ghi lại cảnh báo vào lab log: Nhà nghiên cứu gian lận thế nào khi liên tục lọc bỏ dữ liệu để ép $p < 0.05$?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Phương pháp so sánh hiệu năng 2 mô hình ML có ý nghĩa thống kê.
  * *50% Thực hành:* Chạy mô hình A và B trên 10 fold CV khác nhau, thực hiện Paired Student's t-test để so sánh.
  * *20% Lab Log:* **Milestone Test 6:** Viết kết luận khoa học: Mô hình A vượt trội hơn B là do thuật toán hay chỉ là ngẫu nhiên?

---

#### 🎯 Tuần 7: Xác Suất & Ước Lượng Tham Số (Bayesian vs Frequentist)
* **Mục tiêu:** Hiểu cơ chế mô hình đoán nhận tham số thông qua Likelihood và cập nhật niềm tin bằng Định lý Bayes.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Xác suất có điều kiện $P(A|B)$, Quy tắc nhân xác suất, Giả định độc lập.
  * *50% Thực hành:* Giải bài toán xét nghiệm bệnh y tế kinh điển trên giấy và kiểm tra lại bằng Python.
  * *20% Lab Log:* Giải thích: Tại sao giả định độc lập có điều kiện lại là nền tảng của bộ phân loại Naive Bayes?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Định lý Bayes: Prior, Likelihood, Marginal Probability, Posterior.
  * *50% Thực hành:* Viết code cập nhật phân phối xác suất khi quan sát thêm từng mẫu dữ liệu mới.
  * *20% Lab Log:* Vẽ sơ đồ trực quan hóa: Niềm tin ban đầu (Prior) được dữ liệu mới (Evidence) uốn nắn thành Posterior ra sao.
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Hàm hợp lý (Likelihood Function) vs Hàm xác suất (Probability Function).
  * *50% Thực hành:* Viết code vẽ đồ thị hàm Likelihood của bài toán tung đồng xu có xác suất ngửa $p$ chưa biết.
  * *20% Lab Log:* Phân biệt: Xác suất là tính dữ liệu khi đã biết tham số; Likelihood là đánh giá tham số khi đã nhìn thấy dữ liệu.
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Ước lượng hợp lý cực đại (Maximum Likelihood Estimation - MLE). Negative Log-Likelihood.
  * *50% Thực hành:* Tính tay đạo hàm của Log-Likelihood cho phân phối Bernoulli để tìm tham số tối ưu $p = \frac{k}{n}$.
  * *20% Lab Log:* Chứng minh: Cực đại hóa Likelihood tương đương hoàn toàn với cực tiểu hóa hàm mất mát Binary Cross-Entropy.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* So sánh tư duy Frequentist (Tần suất) vs Bayesian (Bayes).
  * *50% Thực hành:* Viết tài liệu so sánh ước lượng MLE (Frequentist) và MAP (Maximum A Posteriori - Bayesian).
  * *20% Lab Log:* **Milestone Phase II:** Hoàn thành tài liệu tổng kết 3 trang về Thống kê & Xác suất trong `docs/math_notes/`.

---

### PHASE III: THE MACHINE LEARNING CORE (Tuần 8 – Tuần 10)
> **Mục tiêu chặng:** Hiểu bản chất các thuật toán học máy cổ điển từ góc nhìn hàm mất mát và ranh giới quyết định.

#### 🎯 Tuần 8: Kỹ Thuật Thiết Kế Hàm Mất Mát (Loss Engineering)
* **Mục tiêu:** Hiểu cơ chế thưởng phạt của mô hình; tự tay hiện thực 5 hàm mất mát cốt lõi. *(Đọc song song Chương 4 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Empirical Risk Minimization (ERM). Khái niệm hàm mất mát (Loss Function) và hàm mục tiêu (Cost Function).
  * *50% Thực hành:* Viết hàm tính MSE và MAE bằng NumPy trong `src/losses.py`.
  * *20% Lab Log:* Chứng minh toán học: Tại sao đạo hàm của MSE nhạy cảm với outlier hơn nhiều so với MAE?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Robust Loss: Bản chất của Huber Loss (kết hợp vùng tuyến tính của MAE và parabol của MSE).
  * *50% Thực hành:* Viết class `HuberLoss` hỗ trợ tính cả giá trị loss và gradient tương ứng.
  * *20% Lab Log:* Vẽ đồ thị so sánh hình dạng và đạo hàm của MSE, MAE, Huber Loss trên cùng một hệ trục tọa độ.
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Binary Cross-Entropy (Log-Loss) cho bài toán phân loại nhị phân.
  * *50% Thực hành:* Tự code hàm Binary Cross-Entropy có kẹp chặn giá trị (`eps=1e-15`) để triệt tiêu lỗi $\log(0)$.
  * *20% Lab Log:* Vẽ đồ thị: Khi nhãn thực là 1, hình phạt của hàm Cross-Entropy tăng vọt theo cấp số nhân thế nào khi dự đoán giảm về 0?
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Categorical Cross-Entropy & Hàm Softmax cho bài toán phân loại đa lớp.
  * *50% Thực hành:* Viết hàm Softmax ổn định số học (Numeric Stable Softmax bằng cách trừ đi giá trị max).
  * *20% Lab Log:* Active Recall: Tại sao hàm Softmax được gọi là "bản làm mềm" (soft) của phép lấy argmax?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Hinge Loss và nguyên lý khoảng cách lề cực đại (Max-Margin) trong SVM.
  * *50% Thực hành:* Viết code tính Hinge Loss: $\max(0, 1 - y \cdot \hat{y})$ với $y \in \{-1, 1\}$.
  * *20% Lab Log:* **Milestone Test 8:** Hoàn thành file `src/losses.py` với đầy đủ unit tests kiểm tra tính đúng đắn của gradient.

---

#### 🎯 Tuần 9: Mô Hình Phân Loại & Ranh Giới Quyết Định (Discriminative Modeling)
* **Mục tiêu:** Hiểu cách các bộ phân loại chia cắt không gian đặc trưng và định kiến quy nạp (Inductive Biases) của chúng. *(Đọc song song Chương 3 & 4 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Logistic Regression: Hàm Logit, Hàm Sigmoid, Xác suất phân loại.
  * *50% Thực hành:* Tự viết class `MyLogisticRegression` từ đầu bằng NumPy kế thừa `BaseEstimator` trong `src/models/`.
  * *20% Lab Log:* Huấn luyện mô hình tự viết trên tập Iris (2 thuộc tính) và in ra các trọng số hội tụ.
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Ranh giới quyết định (Decision Boundary) của mô hình tuyến tính.
  * *50% Thực hành:* Viết hàm vẽ Decision Boundary 2D dùng `np.meshgrid` và `plt.contourf`.
  * *20% Lab Log:* Giải thích toán học: Tại sao ranh giới của Logistic Regression luôn là một đường siêu phẳng (đường thẳng trong 2D)?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* K-Nearest Neighbors (KNN): Thuật toán học không tham số (Non-parametric).
  * *50% Thực hành:* Tự viết class `MyKNNClassifier` từ đầu bằng NumPy (tính khoảng cách, lấy top $k$, bầu chọn đa số).
  * *20% Lab Log:* Vẽ ranh giới quyết định của KNN với $K=1, K=5, K=30$. Rút ra kết luận về độ mượt của ranh giới khi $K$ thay đổi.
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Naive Bayes Classifier: Phân loại dựa trên xác suất hậu nghiệm Gaussian.
  * *50% Thực hành:* Dùng Scikit-learn huấn luyện Gaussian Naive Bayes và trực quan hóa ranh giới quyết định của nó.
  * *20% Lab Log:* Đặt 3 đồ thị ranh giới (Logistic vs KNN vs Naive Bayes) cạnh nhau để so sánh trực quan.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Khái niệm Định kiến quy nạp (Inductive Bias).
  * *50% Thực hành:* Thử thách cả 3 mô hình trên tập dữ liệu hình mặt trăng phi tuyến (Moons dataset).
  * *20% Lab Log:* **Milestone Test 9:** Phân tích: Tại sao Logistic Regression thất bại thảm hại trên Moons dataset trong khi KNN lại giải quyết dễ dàng?

---

#### 🎯 Tuần 10: Khám Phá Dữ Liệu Không Giám Sát (Unsupervised Discovery)
* **Mục tiêu:** Trích xuất đặc trưng ẩn và tìm kiếm cấu trúc từ dữ liệu không nhãn. *(Đọc song song Chương 8 & 9 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Thuật toán K-Means: Khởi tạo tâm cụm, Gán nhãn, Cập nhật tâm cụm.
  * *50% Thực hành:* Tự viết thuật toán K-Means từ đầu bằng NumPy trong `src/models/kmeans.py`.
  * *20% Lab Log:* Chạy thuật toán trên dữ liệu 2D và vẽ hình mũi tên dịch chuyển của các tâm cụm qua từng vòng lặp.
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Đánh giá phân cụm: Hàm quán tính (Inertia/Elbow Method) và Điểm Silhouette.
  * *50% Thực hành:* Viết code vẽ đường cong Elbow và biểu đồ Silhouette Analysis để chọn số cụm $K$ tối ưu.
  * *20% Lab Log:* Ghi chú: K-Means sẽ gặp thất bại khi các cụm dữ liệu có hình dạng như thế nào?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Phân cụm phân cấp (Hierarchical Clustering) & Biểu đồ Dendrograms.
  * *50% Thực hành:* Dùng `scipy.cluster.hierarchy` vẽ Dendrogram trên một tập dữ liệu nhỏ; cắt cây ở các độ cao khác nhau.
  * *20% Lab Log:* Giải thích ưu thế của Hierarchical Clustering so với K-Means khi không biết trước số cụm.
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Principal Component Analysis (PCA): Giảm số chiều, Tối đa hóa phương sai dữ liệu.
  * *50% Thực hành:* Tự code PCA bằng cách tính Ma trận Hiệp phương sai (Covariance Matrix) và phân rã trị riêng.
  * *20% Lab Log:* So sánh kết quả chiếu chiều của code tự viết với `sklearn.decomposition.PCA`.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Khái niệm Không gian tiềm ẩn (Latent Space).
  * *50% Thực hành:* Dùng PCA nén ảnh khuôn mặt Olivetti Faces (Eigenfaces) từ hàng nghìn chiều về 2 chiều và trực quan hóa.
  * *20% Lab Log:* **Milestone Phase III:** Hoàn thành notebook phân tích nén ảnh bằng PCA và phân cụm K-Means, commit lên GitHub.

---

### PHASE IV: RIGOROUS EVALUATION & DATA PATHOLOGIES (Tuần 11 – Tuần 13)
> **Mục tiêu chặng:** Khoa học đánh giá – Nhận diện gian lận thuật toán, rò rỉ dữ liệu và đánh giá độ tin cậy của mô hình.

#### 🎯 Tuần 11: Đánh Giá Độ Đo Chuyên Sâu (Metrics Deep-Dive)
* **Mục tiêu:** Vượt qua sự ngây thơ của Accuracy; làm chủ Precision-Recall, ROC-AUC và hiệu chuẩn xác suất. *(Đọc song song Chương 3 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Confusion Matrix: TP, FP, TN, FN. Accuracy vs Precision vs Recall.
  * *50% Thực hành:* Tự viết các hàm tính Accuracy, Precision, Recall từ Confusion Matrix bằng NumPy thuần.
  * *20% Lab Log:* Giải bài toán: Trên tập dữ liệu có 99% ca âm tính, một mô hình luôn đoán là "Âm tính" có Accuracy bao nhiêu? Tại sao nó nguy hiểm?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* F1-Score & Sự đánh đổi giữa Precision và Recall (PR Trade-off).
  * *50% Thực hành:* Viết code thay đổi ngưỡng quyết định (Threshold từ 0.0 đến 1.0) và vẽ đường cong Precision-Recall Curve.
  * *20% Lab Log:* Chứng minh toán học: Tại sao F1-score dùng trung bình điều hòa (Harmonic Mean) thay vì trung bình cộng?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Đường cong ROC (Receiver Operating Characteristic) & Chỉ số AUC.
  * *50% Thực hành:* Dùng Scikit-learn vẽ đường cong ROC Curve và tính ROC-AUC.
  * *20% Lab Log:* Phân tích chuyên sâu: Khi nào bắt buộc phải dùng đường cong PR thay cho đường cong ROC? (Khi dữ liệu mất cân bằng nặng).
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Hiệu chuẩn mô hình (Model Calibration): Độ tự tin vs Xác suất thực tế. Brier Score.
  * *50% Thực hành:* Dùng `CalibrationDisplay` vẽ Reliability Diagram của Logistic Regression vs Gaussian Naive Bayes.
  * *20% Lab Log:* Phân tích: Tại sao Naive Bayes thường cho xác suất cực đoan (quá gần 0 hoặc 1) và cần được hiệu chuẩn?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Cấu trúc một module đánh giá toàn diện trong nghiên cứu.
  * *50% Thực hành:* Viết hàm `evaluate_classifier(model, X, y)` tự động xuất ra Confusion Matrix, ROC, PR-Curve và Brier score.
  * *20% Lab Log:* **Milestone Test 11:** Chạy module đánh giá trên một bài toán phân loại và commit code vào thư mục `src/`.

---

#### 🎯 Tuần 12: Chiến Lược Kiểm Định & Kiểm Tra Ngoài Phân Phối (Cross-Dataset Validation)
* **Mục tiêu:** Đo lường khả năng tổng quát hóa và độ bền vững của mô hình trên dữ liệu chưa từng thấy.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* K-Fold Cross-Validation vs Hold-out Validation.
  * *50% Thực hành:* Tự viết hàm chia K-Fold thủ công bằng Python để hiểu rõ cơ chế xoay vòng dữ liệu.
  * *20% Lab Log:* Giải thích: Tại sao Cross-Validation cung cấp ước lượng phương sai của mô hình đáng tin cậy hơn chia 1 lần Train-Test?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Stratified K-Fold: Cơ chế bảo toàn tỷ lệ phân bố nhãn.
  * *50% Thực hành:* So sánh phân bố nhãn giữa các fold khi dùng K-Fold thông thường vs Stratified K-Fold trên dữ liệu tỷ lệ 95:5.
  * *20% Lab Log:* Ghi chú quy tắc: Luôn dùng Stratified K-Fold cho mọi bài toán phân loại có nhãn mất cân bằng.
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Cạm bẫy dữ liệu chuỗi thời gian: Data Snooping & Lấy tương lai đoán quá khứ.
  * *50% Thực hành:* Viết code chứng minh chia K-Fold ngẫu nhiên trên dữ liệu chuỗi thời gian làm điểm số cao ảo; chuyển sang dùng `TimeSeriesSplit`.
  * *20% Lab Log:* Ghi chép phân tích vào lab log: Tại sao dữ liệu time-series không được phép tráo ngẫu nhiên (shuffle)?
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Out-of-Distribution (OOD) Testing: Khả năng chống chịu khi môi trường dữ liệu thay đổi.
  * *50% Thực hành:* Huấn luyện mô hình trên dữ liệu gốc, sau đó đánh giá trên tập dữ liệu bị trôi dạt (Data Drift - thêm nhiễu hoặc đổi miền giá trị).
  * *20% Lab Log:* Đo lường độ sụt giảm hiệu năng và rút ra bài học về tính mong manh của các mô hình ML.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Thiết lập chuẩn mực thực nghiệm tái lập (Reproducibility Standards).
  * *50% Thực hành:* Viết script tự động chạy 5-Fold Stratified CV, tính giá trị trung bình kèm khoảng tin cậy 95%.
  * *20% Lab Log:* **Milestone Test 12:** Đóng gói module Cross-Validation chuẩn vào repo dùng làm khuôn mẫu cho các nghiên cứu tiếp theo.

---

#### 🎯 Tuần 13: Bệnh Lý Dữ Liệu & Gian Lận Thuật Toán (Data Pathologies)
* **Mục tiêu:** Triệt tiêu hoàn toàn lỗi rò rỉ dữ liệu (Target Leakage) và xử lý dữ liệu mất cân bằng một cách khoa học.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Target Leakage: Hiện tượng các đặc trưng mang thông tin của nhãn tương lai lọt vào tập train.
  * *50% Thực hành:* Tạo một bài toán giả lập có chứa cột bị leak; huấn luyện mô hình và quan sát điểm số cao ảo $99.9\%$.
  * *20% Lab Log:* Liệt kê 3 cách nhận diện Target Leakage khi đọc mô tả dữ liệu thực tế.
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Preprocessing Leakage: Chuẩn hóa dữ liệu sai vị trí.
  * *50% Thực hành:* Viết code tái hiện lỗi kinh điển: Gọi `scaler.fit_transform(X)` trên toàn bộ tập dữ liệu trước khi train_test_split.
  * *20% Lab Log:* Chứng minh thông tin của tập kiểm tra (mean, std) đã bị rò rỉ sang tập huấn luyện như thế nào.
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Giải pháp chống rò rỉ triệt để: Scikit-Learn Pipeline (`sklearn.pipeline.Pipeline`).
  * *50% Thực hành:* Đóng gói Scaler, Imputer và Model vào một Pipeline thống nhất; chạy kiểm tra chéo với Cross-Validation.
  * *20% Lab Log:* Ghi chú: Tại sao dùng Pipeline đảm bảo 100% dữ liệu validation không bao giờ bị dính thông tin tiền xử lý?
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Mất cân bằng dữ liệu: Oversampling, Undersampling và thuật toán SMOTE.
  * *50% Thực hành:* Dùng `imblearn.pipeline.Pipeline` kết hợp SMOTE với mô hình phân loại.
  * *20% Lab Log:* Cảnh báo sống còn: Tại sao thực hiện SMOTE trước khi chia Cross-Validation là hành vi gian lận dữ liệu nghiêm trọng?
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Cost-Sensitive Learning: Điều chỉnh trọng số hàm mất mát (`class_weight='balanced'`).
  * *50% Thực hành:* So sánh phương pháp SMOTE với giải pháp điều chỉnh trọng số hàm mất mát trên cùng một dataset thực tế.
  * *20% Lab Log:* **Milestone Phase IV:** Xây dựng thành công một pipeline phân loại dữ liệu mất cân bằng chuẩn mực, không rò rỉ 1 byte dữ liệu.
* ⚠️ **Bẫy phổ biến:** Tự mãn khi thấy mô hình đạt độ chính xác $99\%$. Hãy nhớ: Trong nghiên cứu, *điểm số cao bất thường là dấu hiệu đầu tiên của Data Leakage*.

---

### PHASE V: SYNTHESIS & ADVANCED BASICS (Tuần 14 – Tuần 18)
> **Mục tiêu chặng:** Chẩn đoán lỗi mô hình, xây dựng pipeline nghiên cứu hoàn chỉnh tái lập 100% và viết báo cáo khoa học.

#### 🎯 Tuần 14: Khung Chẩn Đoán Lỗi Mô Hình (Diagnostic Frameworks)
* **Mục tiêu:** Biết chính xác tại sao mô hình thất bại để sửa chữa có phương pháp, thay vì mò mẫm tham số một cách vô vọng. *(Đọc song song Chương 4 sách Géron)*.
* [ ] **Day 1:** 
  * *30% Lý thuyết:* Bias-Variance Tradeoff: High Bias (Underfitting) vs High Variance (Overfitting).
  * *50% Thực hành:* Tự vẽ đồ thị lý thuyết phân tích lỗi tổng quát thành: $\text{Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$.
  * *20% Lab Log:* Phân tích: Mô hình có train error cao và val error cao là bị gì? Train error cực thấp nhưng val error cao vọt là bị gì?
* [ ] **Day 2:** 
  * *30% Lý thuyết:* Đường cong học tập (Learning Curves): Đọc vị mô hình qua kích thước dữ liệu.
  * *50% Thực hành:* Dùng `sklearn.model_selection.learning_curve` vẽ đồ thị lỗi huấn luyện và xác thực theo số lượng mẫu $m$.
  * *20% Lab Log:* Chẩn đoán biểu đồ: Nếu 2 đường train và val đã chụm vào nhau ở mức lỗi cao, việc thu thập thêm dữ liệu có giải quyết được vấn đề không?
* [ ] **Day 3:** 
  * *30% Lý thuyết:* Lời nguyền số chiều (Curse of Dimensionality) và Regularization ($L_1$ Lasso, $L_2$ Ridge).
  * *50% Thực hành:* Đo khoảng cách trung bình giữa các điểm ngẫu nhiên khi số chiều tăng từ 2 lên 1000; thử nghiệm hiệu quả co trọng số của $L_2$.
  * *20% Lab Log:* Ghi chú: Tại sao không gian nhiều chiều khiến mọi điểm dữ liệu đều trở thành ngoại lai cô lập?
* [ ] **Day 4:** 
  * *30% Lý thuyết:* Đánh giá tầm quan trọng của đặc trưng: Permutation Feature Importance.
  * *50% Thực hành:* Dùng `sklearn.inspection.permutation_importance` đánh giá mức độ đóng góp thực sự của từng cột dữ liệu.
  * *20% Lab Log:* So sánh Permutation Importance với việc nhìn vào hệ số trọng số thô của mô hình.
* [ ] **Day 5:** 
  * *30% Lý thuyết:* Xây dựng Cẩm nang chẩn đoán lỗi (Diagnostic Playbook).
  * *50% Thực hành:* Lập lưu đồ xử lý: Nếu High Bias $\to$ Tăng đặc trưng, chọn mô hình phức tạp hơn; Nếu High Variance $\to$ Thêm dữ liệu, thêm Regularization, giảm bớt đặc trưng.
  * *20% Lab Log:* **Milestone Test 14:** Chẩn đoán chính xác một mô hình bị Overfitting và thực hiện can thiệp giảm Overfitting thành công.

---

#### 🎯 Tuần 15 & Tuần 16: Dự Án Mô Phỏng Nghiên Cứu Hoàn Chỉnh (Beginner Research Simulation)
* **Mục tiêu:** Áp dụng toàn bộ kiến thức vào một bài toán thực tế; xây dựng quy trình khép kín, tự động hóa và tái lập 100%.

* [ ] **Tuần 15 – Giai đoạn Khám phá Dữ liệu, Baseline & Pipeline Chống Rò Rỉ:**
  * Chọn một bộ dữ liệu từ UCI ML Repository (ví dụ: *Heart Disease*, *Credit Card Fraud*, hoặc *Adult Census*).
  * Thực hiện EDA nghiêm ngặt: Kiểm tra phân phối, skewness, outliers, và tương quan đặc trưng.
  * Xây dựng mô hình Baseline đơn giản (DummyClassifier hoặc Logistic Regression thô) để làm chuẩn quy chiếu.
  * Thiết kế `Pipeline` tiền xử lý tự động: Imputation $\to$ Scaling $\to$ One-Hot Encoding không rò rỉ thông tin.
* [ ] **Tuần 16 – Giai đoạn Thử Nghiệm Mô Hình, Đánh Giá & Phân Tích Lỗi:**
  * Thử nghiệm có hệ thống: Logistic Regression (L1/L2) vs KNN vs Random Forest.
  * Đánh giá qua Stratified 5-Fold Cross-Validation cố định `random_state`.
  * Đo lường đa chỉ số: F1-score, PR-AUC, Brier score (Calibration).
  * Thực hiện kiểm định Paired t-test chứng minh mô hình đề xuất tốt hơn Baseline có ý nghĩa thống kê ($p < 0.05$).
  * **Failure Analysis:** Tìm ra 5 trường hợp mô hình dự đoán sai nghiêm trọng nhất và lý giải nguyên nhân thất bại.
* [ ] **Milestone Hoàn Thành Tuần 15-16:** Pipeline chạy tự động từ đầu đến cuối chỉ bằng lệnh `python run_experiments.py`; kết quả hoàn toàn tái lập được.

---

#### 🎯 Tuần 17 & Tuần 18: Tổng Kết Kỹ Thuật, Viết Báo Cáo & Hoàn Thiện Tư Duy Nghiên Cứu
* **Mục tiêu:** Rèn luyện kỹ năng truyền đạt khoa học, phản biện mã nguồn và hoàn tất portfolio học thuật gửi Mentor.

* [ ] **Tuần 17 – Soạn Thảo Báo Cáo Kỹ Thuật (Technical Research Report):**
  * Soạn file `docs/RESEARCH_REPORT.md` (hoặc mẫu bài báo khoa học 4-5 trang) gồm các phần chuẩn mực:
    1. **Abstract:** Tóm tắt bài toán, phương pháp và kết quả cốt lõi trong 150 từ.
    2. **Introduction & Related Work:** Bối cảnh và lý do chọn đề tài.
    3. **Methodology & Data Pathology:** Chi tiết phân phối dữ liệu, cách phòng ngừa Leakage và kiến trúc Pipeline.
    4. **Experimental Setup & Results:** Bảng kết quả, biểu đồ ROC/PR, Learning Curve, kết quả kiểm định t-test.
    5. **Failure Analysis & Limitations:** Thừa nhận trung thực các điểm mô hình chưa làm được.
    6. **Conclusion & Future Work:** Kết luận về tính hiệu quả của phương pháp.
* [ ] **Tuần 18 – Hoàn Thiện Repo, Viết Blog & Báo Cáo Với Mentor:**
  * Refactor toàn bộ code trong repo: format chuẩn PEP8, bổ sung docstrings đầy đủ.
  * Hoàn thiện file `README.md` đóng vai trò là một trang giới thiệu portfolio chuyên nghiệp.
  * Viết một bài blog kỹ thuật (chia sẻ trên Medium/LinkedIn/Substack): *"Hành trình 18 Tuần Luyện Tư Duy Nghiên Cứu Machine Learning: Tại Sao Nền Tảng Luôn Đánh Bại Sự Phức Tạp?"*.
  * **Milestone Cuối Cùng:** Gửi link GitHub repo và bài báo cáo cho Mentor để tiến hành buổi Review 1-1.

---

## 6. BẢNG CẢNH BÁO CẠM BẪY PHỔ BIẾN & TÂM LÝ NGHIÊN CỨU

| Giai Đoạn | Cạm Bẫy Phổ Biến Hay Làm Nản Lòng | Chiến Lược Khắc Phục Chuẩn R&D |
| :--- | :--- | :--- |
| **Phase I (Tuần 1–4)** | Thấy các công thức đạo hàm, ma trận, SVD quá nặng lý thuyết. Muốn nhảy ngay vào gọi hàm `model.fit()` cho nhanh. | Đừng học vẹt công thức. Hãy gắn toán với hình học (không gian vector, trượt dốc). Thử nghiệm code với ma trận nhỏ $2 \times 2$ trước. |
| **Phase II (Tuần 5–7)** | Cảm thấy thống kê suy diễn và p-value khô khan, trừu tượng. | Luôn đặt câu hỏi thực tế: *"Làm sao chứng minh thuật toán của mình tốt thật hay chỉ do ăn may?"*. Xem các video mô phỏng trực quan của kênh StatQuest hoặc 3Blue1Brown. |
| **Phase III (Tuần 8–10)** | Mải mê tìm kiếm các thuật toán phức tạp hơn thay vì hiểu sâu định kiến quy nạp (Inductive Bias). | Luôn tự hỏi: *"Thuật toán này giả định điều gì về dữ liệu?"*. Vẽ biểu đồ Decision Boundary để tận mắt thấy thuật toán phân chia không gian ra sao. |
| **Phase IV (Tuần 11–13)** | Thất vọng vì sau khi sửa lỗi Data Leakage, độ chính xác của mô hình tụt từ $99\%$ xuống $82\%$. | Hãy ăn mừng! Bạn vừa cứu một dự án thực tế khỏi sự sụp đổ. Một kết quả khiêm tốn nhưng trung thực có giá trị gấp trăm lần một kết quả cao do gian lận dữ liệu. |
| **Phase V (Tuần 14–18)** | Ngại viết báo cáo và phân tích lỗi; muốn nhảy ngay sang học Deep Learning hoặc Large Language Models (LLMs). | Khả năng viết báo cáo và phân tích lỗi (Failure Analysis) là ranh giới duy nhất phân biệt **Nhà nghiên cứu (Researcher)** với **Thợ bấm code (Script Kiddie)**. |

---

> 💡 **Lời khuyên từ Mentor:** *"Đừng đo lường sự tiến bộ bằng số dòng code bạn viết hay số mô hình bạn thử. Hãy đo lường bằng mức độ bạn hiểu rõ tại sao mô hình của mình hoạt động, và quan trọng hơn cả: tại sao nó thất bại."*
