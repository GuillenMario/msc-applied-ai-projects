# MSc Applied Artificial Intelligence – Projects Portfolio

This repository contains selected projects from my **Master’s in Applied Artificial Intelligence**, covering topics across **machine learning** and **big data engineering**.  
Each notebook demonstrates applied techniques on real datasets with a focus on **model evaluation, reproducibility, and interpretability**.

---

## 📂 Repository Structure

```
.
├── notebooks/
│   ├── artificial_intelligence_ml/
│   │   ├── 01_basic_data_transformations_linear_regression.ipynb
│   │   ├── 02_employee_attrition_ibm_hr.ipynb
│   │   ├── 03_roc_pr_imbalance.ipynb
│   │   ├── 04_learning_curves.ipynb
│   │   ├── 05_recommendation_systems.ipynb
│   │   └── 06_time_series_forecasting.ipynb
│   └── big_data/
│       ├── 01_readingwriting_pyspark_files.ipynb
│       ├── 02_supervised_unsupervised_learning.ipynb
│       ├── 03_result_quality_metrics.ipynb
│       ├── 04_results_visualization.ipynb
│       ├── 05_final_delivery.ipynb
│       ├── data/
│       ├── README.md   # dataset links and instructions 
│       └── sample/     # small extracts for testing
├── environment.yml
├── .gitignore
└── README.md
```

---

## 🤖 Artificial Intelligence & Machine Learning
Projects covering core ML techniques on structured datasets.

| # | Project | Description | Key Techniques | Results / Metrics |
|---|---------|-------------|----------------|------------------|
| 1 | [Basic Data Transformations & Linear Regression](notebooks/artificial_intelligence_ml/01_basic_data_transformations_linear_regression.ipynb) | Regression on structured data with feature engineering & residual analysis | Pandas, Scikit-Learn, Matplotlib | Baseline vs Linear Regression, residual plots |
| 2 | [Employee Attrition Analysis (IBM HR Dataset)](notebooks/artificial_intelligence_ml/02_employee_attrition_ibm_hr.ipynb) | Predicting employee attrition with focus on imbalance and interpretability | Logistic Regression, Random Forest, SHAP | **PR-AUC 0.71**, SHAP explanations, ethical considerations |
| 3 | [ROC & PR Curves on Imbalanced Datasets](notebooks/artificial_intelligence_ml/03_roc_pr_imbalance.ipynb) | Comparison of ROC-AUC vs PR-AUC and threshold selection | Metrics, Calibration, Threshold tuning | Demonstrates why PR-AUC is preferred under imbalance |
| 4 | [Learning Curves](notebooks/artificial_intelligence_ml/04_learning_curves.ipynb) | Bias-variance diagnosis via learning curves | Train/validation splits, cross-validation | Identifies underfitting vs overfitting |
| 5 | [Recommendation Systems](notebooks/artificial_intelligence_ml/05_recommendation_systems.ipynb) | Collaborative filtering and baselines | Implicit ALS, Surprise, Matrix Factorization | **NDCG@10 +18%** vs popularity baseline |
| 6 | [Time Series Forecasting](notebooks/artificial_intelligence_ml/06_time_series_forecasting.ipynb) | Forecasting demand with walk-forward validation | Prophet, SARIMA, Statsmodels | **MAPE 9.8%** on holdout, holiday effects analyzed |

---

## 📊 Big Data Project
This section is structured as a standalone project, covering ingestion, learning, evaluation, and final reporting.  
It includes its own `/data/` folder with sample files and instructions.

| # | Project | Description | Key Techniques | Results / Metrics |
|---|---------|-------------|----------------|------------------|
| 1 | [Reading/Writing Big Data with PySpark](notebooks/big_data/01_readingwriting_pyspark_files.ipynb) | Efficient data I/O with PySpark | CSV vs Parquet, schema inference | Benchmarked throughput and schema handling |
| 2 | [Supervised & Unsupervised Learning](notebooks/big_data/02_supervised_unsupervised_learning.ipynb) | Applying ML models in Spark | Spark MLlib, KMeans, Random Forest | Cluster quality (silhouette) and classification metrics |
| 3 | [Result Quality Metrics](notebooks/big_data/03_result_quality_metrics.ipynb) | Cookbook of metrics for classification & regression | Spark MLlib metrics | ROC-AUC, PR-AUC, RMSE, F1 |
| 4 | [Results Visualization](notebooks/big_data/04_results_visualization.ipynb) | Visualization of Spark ML results | Matplotlib, Seaborn | Confusion matrices, ROC/PR plots |
| 5 | [Final Delivery](notebooks/big_data/05_final_delivery.ipynb) | Executive summary of methodology & outcomes | Consolidated results | High-level report for stakeholders |

---

## 📊 Datasets
Datasets are **not stored** in this repo due to size.  

- For **AI/ML projects**: sample datasets are included in each folder.  
- For the **Big Data project**: dataset instructions are included inside `notebooks/big_data/data/README.md`.

---

## ⚙️ Environment Setup

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate applied_ai
```

Then launch Jupyter Lab:

```bash
jupyter lab
```

---

## 🛠️ Tools & Libraries

- **Languages:** Python 3.11, PySpark 3.5  
- **Libraries:** pandas, scikit-learn, matplotlib, seaborn, statsmodels, prophet, SHAP, implicit, scikit-surprise  
- **Big Data:** PySpark, Parquet/CSV I/O, Spark MLlib  
- **Visualization:** matplotlib, seaborn  

---

## 📌 Key Takeaways
- Applied a wide range of **ML algorithms** across regression, classification, forecasting, and recommendation.  
- Emphasis on **model evaluation** with the right metrics (PR-AUC for imbalance, MAPE for forecasting, NDCG for recommendations).  
- Explored **interpretability & ethics** in HR attrition prediction.  
- Practiced **big data handling** with PySpark and end-to-end project structure.  

---

## 📜 License
This project is released under the [MIT License](LICENSE).
