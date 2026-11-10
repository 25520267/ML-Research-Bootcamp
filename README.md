# 🚀 Machine Learning Research Bootcamp (18-Week Study & Lab Repo)

> **Tác giả thực hành:** Dylis (`ledat270406@gmail.com`)  
> **Lộ trình gốc:** *Machine Learning Research Bootcamp: The Beginner's Path* (Nguyen Minh Nhut – Chief R&D Engineer)  
> **Triết lý:** *"Fundamentals over Complexity"* — Ưu tiên nền tảng toán học, khoa học đánh giá (Evaluation Science) và tính tái lập (Reproducibility).

---

## 📂 Cấu Trúc Repository

Mỗi ngày học được tổ chức khép kín theo thư mục `Week X/Day Y/` gồm đầy đủ: Giáo án lý thuyết, Đề bài tập, Đáp án chi tiết, Mã nguồn thực hành (`*.py` / `*.ipynb`) và Nhật ký thí nghiệm (`lab_log.md`).

```text
ML-Research-Bootcamp/
├── README.md                  # Bảng điều khiển tiến độ & tổng quan repository
├── ROADMAP.md                 # Lộ trình chi tiết 18 tuần (từng ngày theo khung 30-50-20)
├── requirements.txt           # Danh sách thư viện & phiên bản tái lập môi trường
├── .gitignore                 # Loại bỏ file rác, cache Python/Jupyter/VS Code
└── Week 1/
    └── Day 1/
        ├── Ngay_01_Namespace_Scoping_LEGB_va_Dataclasses.md
        ├── Ngay_01_Bai_tap.md
        ├── Ngay_01_Dap_an_chi_tiet.md
        ├── lab_log.md
        └── test.py
```

---

## ⏱️ Quy Trình Học Tập Mỗi Ngày (Khung 30 - 50 - 20)

| Phân Bổ | Thời Lượng | Nội Dung Cốt Lõi |
| :--- | :---: | :--- |
| **30% Lý thuyết & Toán** | 36 phút | Đọc giáo án, hiểu cơ chế ngôn ngữ / chứng minh công thức toán ra giấy. |
| **50% Thực hành Code** | 60 phút | Tự viết mã nguồn bằng Python/NumPy thuần (không dùng hộp đen) và giải bộ bài tập. |
| **20% Kiểm tra & Lab Log** | 24 phút | Active Recall, đối chiếu đáp án chi tiết, ghi nhật ký `lab_log.md` và đẩy commit lên GitHub. |

---

## 📊 Bảng Theo Dõi Tiến Độ (Progress Dashboard)

### 🟢 Phase I: The Language & The Math Engine (Tuần 1 – Tuần 4)
- [ ] **Week 1 / Day 1:** Namespace, Scoping (LEGB Rule) & Quản lý cấu hình bất biến với `dataclasses`
- [ ] **Week 1 / Day 2:** Closures & Decorators (`@wraps`, `@time_it`, `@catch_oom`)
- [ ] **Week 1 / Day 3:** Generators (`yield`) & Tối ưu bộ nhớ RAM khi stream dữ liệu lớn
- [ ] **Week 1 / Day 4:** OOP cho ML (`BaseEstimator`, `__call__`, `__repr__`)
- [ ] **Week 1 / Day 5:** Type Hints, Docstrings & Refactor chuẩn PEP 8
- [ ] **Week 2:** Complexity & Data Structures (`Big-O`, Hash Maps, Trees, NumPy Memory Layout)
- [ ] **Week 3:** Linear Algebra & Vectorization (Norms, Eigenvalues, SVD)
- [ ] **Week 4:** Multivariable Calculus & Optimization (Chain Rule, Jacobians, Gradient Descent from Scratch)

### 🟡 Phase II: Statistical Rigor & Foundations (Tuần 5 – Tuần 7)
- [ ] **Week 5:** Data Distribution Analysis & Rigorous EDA (Skewness, Kurtosis, PDF/CDF, Q-Q Plot)
- [ ] **Week 6:** Statistical Inference (CLT, Hypothesis Testing, p-values, Power Analysis, p-hacking)
- [ ] **Week 7:** Probability & Parameter Estimation (Bayes' Rule, Likelihood, MLE vs MAP)

### 🟠 Phase III: The Machine Learning Core (Tuần 8 – Tuần 10)
- [ ] **Week 8:** Loss Engineering (MSE, MAE, Huber, Cross-Entropy, Hinge Loss)
- [ ] **Week 9:** Discriminative Modeling & Decision Boundaries (Logistic Regression, KNN, Naive Bayes, Inductive Bias)
- [ ] **Week 10:** Unsupervised Discovery (K-Means, Hierarchical Clustering, PCA / Eigenfaces)

### 🔴 Phase IV: Rigorous Evaluation & Data Pathologies (Tuần 11 – Tuần 13)
- [ ] **Week 11:** Metrics Deep-Dive (PR-Curves, ROC-AUC, Calibration / Brier Score)
- [ ] **Week 12:** Cross-Dataset Validation (Stratified K-Fold, TimeSeriesSplit, Out-of-Distribution Testing)
- [ ] **Week 13:** Data Pathologies (Target Leakage, Preprocessing Leakage, Sklearn Pipelines, SMOTE vs Class Weight)

### 🟣 Phase V: Synthesis & Advanced Basics (Tuần 14 – Tuần 18)
- [ ] **Week 14:** Diagnostic Frameworks (Bias-Variance Tradeoff, Learning Curves, Curse of Dimensionality, Permutation Importance)
- [ ] **Week 15–16:** End-to-End Research Simulation Project (Reproducible Pipeline & Statistical Benchmarking)
- [ ] **Week 17–18:** Technical Research Report, Code Review & Blog Synthesis

---

## 🛠️ Cách Thiết Lập Môi Trường Tái Lập (Reproducibility)

```bash
# Tạo môi trường ảo (khuyên dùng)
python -m venv .venv

# Kích hoạt trên Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Cài đặt toàn bộ thư viện chuẩn
pip install -r requirements.txt
```
