# Big Data Project – MSc Applied AI

**Status:** This project is currently in its draft phase. The structure, workflows, and notebooks are in place and reviewable, but some sections (metrics, results) may still be refined. 

This section is a standalone project developed during my **Master’s in Applied Artificial Intelligence**, focusing on **big data ingestion, processing, machine learning, and reporting** using PySpark and related tools.

The project simulates an **end-to-end big data pipeline**:  
1. Reading and writing large datasets in efficient formats.  
2. Applying supervised and unsupervised learning with Spark MLlib.  
3. Evaluating models with the correct quality metrics.  
4. Visualizing results.  
5. Delivering a final stakeholder report.  

---

## 📂 Folder Structure

```
big_data/
├── 01_readingwriting_pyspark_files.ipynb
├── 02_supervised_unsupervised_learning.ipynb
├── 03_result_quality_metrics.ipynb
├── 04_results_visualization.ipynb
├── 05_final_delivery.ipynb
└── data/
    ├── README.md      # dataset links and instructions
    └── sample/        # small extracts for testing
```

---

## 📊 Notebooks Overview

| # | Notebook | Description | Key Techniques | Results / Metrics |
|---|----------|-------------|----------------|------------------|
| 1 | [Reading/Writing Big Data with PySpark](01_readingwriting_pyspark_files.ipynb) | Efficient data I/O with Spark | Parquet vs CSV, explicit schemas, partitioning | Throughput benchmarks and schema control |
| 2 | [Supervised & Unsupervised Learning](02_supervised_unsupervised_learning.ipynb) | ML models at scale in Spark | KMeans, Random Forest, Spark Pipelines | **Silhouette score:** (fill), **F1/Accuracy:** (fill) |
| 3 | [Result Quality Metrics](03_result_quality_metrics.ipynb) | Cookbook of metrics for Spark ML | ROC-AUC, PR-AUC, RMSE, F1 | Metric interpretation examples |
| 4 | [Results Visualization](04_results_visualization.ipynb) | Standard plots for Spark ML results | Confusion matrices, ROC/PR plots | Standardized visual outputs |
| 5 | [Final Delivery](05_final_delivery.ipynb) | Executive summary | Consolidated metrics & figures | High-level report for stakeholders |

---

## 📊 Dataset
The dataset is not included due to size.  

- See [data/README.md](data/README.md) for dataset source and download instructions.  
- Small samples are available in `data/sample/` for quick testing.  

---

## ⚙️ Environment Setup

The project runs on the same root environment as the rest of the repo. From repo root:

```bash
conda env create -f ../../environment.yml
conda activate applied_ai
```

On Windows, ensure:  
- Java 17 (Temurin recommended).  
- `JAVA_HOME` is set and points to your JDK.  
- Spark 3.5.x is installed (PySpark handles this automatically in Conda).  

---

## 📌 Key Takeaways
- Learned to **handle large datasets efficiently** with PySpark.  
- Built **supervised and unsupervised models** using Spark MLlib.  
- Explored **quality metrics** and how they scale to big data.  
- Developed **visualizations** for Spark results.  
- Delivered a **stakeholder-oriented final report**.  

---
