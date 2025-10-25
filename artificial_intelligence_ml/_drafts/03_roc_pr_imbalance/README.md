# **Activity: ROC and PR Curves Analysis for Imbalanced Datasets**

This activity focuses on the analysis of ROC (Receiver Operating Characteristic) and PR (Precision-Recall) curves in the context of imbalanced datasets. The well-known "oil-spill" dataset is used for this purpose.

## **📁 Dataset**

The oil-spill dataset comprises 50 columns and 937 records.

* The first 49 columns represent metrics derived from satellite images of the ocean, some of which indicate oil spills.  
* The last column is a binary target variable, where 1 signifies an oil spill in that section of the image and 0 indicates no spill.

For more detailed information about the dataset and its feature extraction, refer to the related article: [Oil Spill Detection Research Paper](https://webdocs.cs.ualberta.ca/~holte/Publications/oilspill.pdf)

## **📊 Methodology**

The notebook processes the data using a standard approach to focus on the core concepts of ROC and PR curve analysis. Key libraries used include:

* pandas for data manipulation.  
* numpy for numerical operations.  
* matplotlib.pyplot for plotting.  
* sklearn.model\_selection for data splitting (train\_test\_split, RepeatedStratifiedKFold, cross\_val\_score, cross\_validate).  
* sklearn.metrics for model evaluation (make\_scorer, RocCurveDisplay, PrecisionRecallDisplay, classification\_report).  
* imblearn.metrics.geometric\_mean\_score for computing the geometric mean, particularly useful for imbalanced datasets.  
* sklearn.pipeline, sklearn.compose, sklearn.impute, sklearn.preprocessing, sklearn.linear\_model, sklearn.neighbors for data preprocessing and model building (Pipeline, ColumnTransformer, SimpleImputer, StandardScaler, PowerTransformer, OneHotEncoder, LogisticRegression, KNeighborsClassifier).

The dataset is partitioned into training, validation, and test sets with stratified sampling to maintain class distribution.

* **Training Set:** 659 records, 29 positive class instances (4.40%)  
* **Validation Set:** 165 records, 7 positive class instances (4.24%)  
* **Test Set:** 108 records, 5 positive class instances (4.42%)

Additional information on model evaluation metrics can be found here: [Scikit-learn Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)  
The implementation of the geometric mean score from imbalanced-learn can be found here: [Imbalanced-learn Geometric Mean Score](https://glemaitre.github.io/imbalanced-learn/generated/imblearn.metrics.geometric_mean_score.html)

## **📃 Findings**

Based on the analysis of the test set, two primary issues were observed:

1. **Model Overfitting:** The model exhibits significant overfitting, as indicated by a notable difference between validation/test set results and training set results. This suggests a need for more data, different transformations, or an alternative model architecture.  
2. **Poor Minority Class Classification:** The model struggles to accurately classify instances belonging to the minority class. This highlights the necessity of applying oversampling and undersampling techniques to address the class imbalance.

## 👨‍🎓 Author

- **Mario Alberto Guillen De La Torre**
- Student ID: A01796701
- Professor: Luis Eduardo Falcón Morales

## 📌 Course

- Master’s in Applied Artificial Intelligence
- Tecnológico de Monterrey

---
