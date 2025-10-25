# MSc Applied Artificial Intelligence – Projects Portfolio

This repository contains selected projects from my **Master’s in Applied Artificial Intelligence**, covering topics across **machine learning** and **big data engineering**. 

Each notebook demonstrates applied techniques on real datasets with a focus on **model evaluation, reproducibility, and interpretability**.  

⚠️ **Status**  
- **Artificial Intelligence & ML** → Two notebooks are now fully polished and portfolio-ready: **01 (Linear Regression)** and **02 (Employee Attrition Analysis — IBM HR Dataset)**. Remaining modules are in draft stage and will be progressively updated.
- **Big Data** → Draft phase but reviewable. Structure and workflows are in place, some results may still evolve.  

---

## Repository Structure  

```
.
├── notebooks/
│   ├── artificial_intelligence_ml/                                     # ML coursework
│   │   ├── _common/                                                    # shared setup, utils, style
│   │   ├── _drafts/                                                    # This folder contains notebooks still under development.  
│   │   ├── 01_basic_data_transformations_linear_regression/
│   │   │   ├── source/                                                 # original unpolished notebook
│   │   │   ├── data/                                                   # raw & processed datasets
│   │   │   ├── reports/                                                # figures & metrics artifacts
│   │   │   ├── 01_basic_data_transformations_linear_regression.ipynb   # polished portfolio notebook ✅
│   │   │   └── README.md                                               # module-level documentation
│   │   ├── 02_employee_attrition_ibm_hr/
│   │   │   ├── source/                                                 # original unpolished notebook
│   │   │   ├── data/                                                   # raw & processed datasets
│   │   │   ├── reports/                                                # figures & metrics artifacts
│   │   │   ├── 02_employee_attrition_ibm_hr.ipynb                      # polished portfolio notebook ✅
│   │   │   └── README.md                                               # module-level documentation
│   │   └── README.md                                                   # module-level documentation
│   └── big_data/                                                       # Big Data coursework
│       ├── 01_readingwriting_pyspark_files/
│       │   ├── 01_pyspark_io_bigdata.ipynb
│       │   └── README.md
│       ├── 02_supervised_unsupervised_learning/
│       │   ├── 02_supervised_unsupervised_learning.ipynb
│       │   └── README.md
│       ├── 03_result_quality_metrics/
│       │   ├── 03_result_quality_metrics.ipynb
│       │   └── README.md
│       ├── 04_results_visualization/
│       │   ├── 04_results_visualization.ipynb
│       │   └── README.md
│       ├── 05_final_delivery/
│       │   ├── 05_final_delivery.ipynb
│       │   └── README.md
│       ├── data/                                                       # dataset instructions
│       └── README.md                                                   # module-level documentation
├── environment.yml
├── .gitignore
└── README.md   # this file
```

---

## Artificial Intelligence & Machine Learning
Projects covering core ML techniques on structured datasets.

| Module | Status | Description |
|--------|--------|-------------|
| 01 – Basic Data Transformations & Linear Regression | ✅ Polished | Regression on structured data with feature engineering, Ridge/Lasso CV, and residual diagnostics. |
| 02 — Employee Attrition Analysis (IBM HR Dataset) | ✅ Polished | End-to-end classification workflow predicting employee attrition using logistic regression, feature engineering, grid search, and imbalance-aware evaluation. |
| 03 – ROC & PR Curves for Imbalanced Data | 🚧 Draft | Comparison of ROC-AUC vs PR-AUC and threshold selection. |
| 04 – Learning Curves | 🚧 Draft | Bias–variance diagnosis via learning curves. |
| 05 – Recommendation Systems | 🚧 Draft | Collaborative filtering and baseline recommenders. |
| 06 – Time Series Forecasting | 🚧 Draft | Forecasting with ARIMA and Prophet. |

---

## Big Data Project
This section is structured as a standalone project, covering ingestion, learning, evaluation, and final reporting.  
It includes its own `/data/` folder with sample files and instructions.

| Module | Status | Description |
|--------|--------|-------------|
| 01 – Reading/Writing Big Data with PySpark | 🚧 Draft | Efficient data I/O with PySpark (CSV vs Parquet). |
| 02 – Supervised & Unsupervised Learning | 🚧 Draft | Applying Spark MLlib models (Random Forest, KMeans). |
| 03 – Result Quality Metrics | 🚧 Draft | Cookbook of metrics for classification & regression in Spark. |
| 04 – Results Visualization | 🚧 Draft | Visualization of MLlib results with Seaborn/Matplotlib. |
| 05 – Final Delivery | 🚧 Draft | Consolidated summary for stakeholders. |

---

## Datasets
Datasets are **not stored** in this repo due to size.  

- For **AI/ML projects**: sample datasets are included in each folder.  
- For the **Big Data project**: dataset instructions are included inside `notebooks/big_data/data/README.md`.

---

## Environment Setup

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate applied_ai
jupyter lab
```

---

## Tools & Libraries

- **Languages:** Python 3.11, PySpark 3.5  
- **Libraries:** pandas, scikit-learn, matplotlib, seaborn, statsmodels, prophet, SHAP, implicit, scikit-surprise  
- **Big Data:** PySpark, Parquet/CSV I/O, Spark MLlib  
- **Visualization:** matplotlib, seaborn  

---

## Key Takeaways
- Demonstrates **ML end-to-end workflows** (from data audit → model → evaluation → conclusions).  
- Includes **diagnostics & interpretability** (residual plots, feature importances, SHAP).  
- Applies **big data processing** with PySpark and MLlib.  
- Shows an evolving portfolio: one module polished, others reviewable drafts.  

---

## License
This project is released under the [MIT License](LICENSE).
