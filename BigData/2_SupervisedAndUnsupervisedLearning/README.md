# 🤖 Supervised and Unsupervised Learning with PySpark

This notebook demonstrates the workflow for building **supervised** and **unsupervised** machine learning models using PySpark with a dataset of taxi trips. It includes **data preprocessing, stratified sampling, feature engineering, model training, and evaluation**.

## 🚀 Project Overview

The goal of this notebook is to:

- Predict **tip amounts** using a supervised learning model (Linear Regression).
- Identify natural data groupings using an unsupervised learning model (KMeans).

## 📊 Workflow Steps

### 1. Data Preparation
- Create a **StrataGrouping** column for stratified sampling.
- Apply `sampleBy` to extract 15% of data from each stratum, ensuring balanced sampling and efficiency.

### 2. Handling Missing Data
- Categorical variables: Use placeholder values for imputation.
- Treat **trip_hour**, **trip_day_of_week**, and **trip_month** as categorical (though stored as numeric).

### 3. Feature Engineering
- **Categorical features:** Apply StringIndexer + OneHotEncoder.
- **Numerical features:** Use StandardScaler to normalize.
- Combine all transformed features using VectorAssembler.

### 4. Dataset Splitting
- Split dataset into **training** and **testing** sets to prevent data leakage.
- Apply preprocessing pipelines separately to training and testing sets.

### 5. Supervised Learning
- **Model:** Linear Regression (predict tips).
- **Hyperparameter Tuning:** Grid search to find the best parameters.
- **Evaluation:** Model predicts tip values with high accuracy (difference of only a few cents).

### 6. Unsupervised Learning
- **Model:** KMeans clustering.
- **Evaluation:** Silhouette score of 0.41 indicates positive but improvable clustering quality.

## 🛠 Technologies

- Python 3.x
- PySpark / Apache Spark
- Jupyter Notebook

## 📌 Key Results

- Stratified sampling ensures representative subsets while reducing computational costs.
- The supervised model provides accurate predictions for tip amounts.
- Clustering highlights consumer patterns, though with potential for improvement.

## 👨‍🎓 Author

Mario Alberto Guillen De La Torre

---
