# IBM HR Analytics — Employee Attrition Prediction  

## Overview  
This project applies a **Logistic Regression model** to predict **employee attrition** using IBM’s fictional HR dataset. The notebook demonstrates a complete **machine learning workflow**, from **data auditing** and **feature engineering** to **model tuning** and **validation**, with a focus on interpretability and class imbalance handling.  

---

## Workflow  
1. **Data Loading & Audit**  
   - Inspected missing values, invalid categorical ranges, and constant columns.  
   - Identified ordinal, nominal, and binary categorical features based on expert knowledge.  
   - Verified target balance and noted a significant class imbalance (≈80/20 split).  

2. **Preprocessing & Feature Engineering**  
   - Applied imputers for missing values across all feature types.  
   - Encoded ordinal, nominal, and binary features using appropriate encoders (`OrdinalEncoder`, `OneHotEncoder`).  
   - Scaled numerical data using **Yeo–Johnson Power Transformation** to reduce skewness and standardize scales.  
   - Built a unified **ColumnTransformer pipeline** for reproducibility and deployment readiness.  

3. **Modeling & Validation**  
   - Established a baseline with a **Dummy Classifier** (most frequent strategy).  
   - Trained multiple **Logistic Regression** models using `GridSearchCV` with stratified K-fold cross-validation.  
   - Evaluated models on multiple metrics (`balanced_accuracy`, `ROC AUC`, `F1`, `accuracy`) to handle imbalance.  

4. **Feature Importance & Interpretation**  
   - Extracted model coefficients from the best estimator to identify key drivers of attrition.  
   - Found that **OverTime**, **BusinessTravel**, **MaritalStatus**, and **EducationField** were the strongest predictors.  
   - Interpreted findings within an HR context, linking frequent travel and overtime to potential burnout.  

5. **Testing & Generalization**  
   - Assessed final performance on unseen test data using a **classification report** and **confusion matrix**.  
   - Accuracy ≈78%, balanced accuracy ≈71%, F1 ≈0.50.  
   - Results consistent with cross-validation — indicating good generalization with no over/underfitting.  

6. **Conclusions & Next Steps**  
   - Model generalizes well but remains affected by **class imbalance** (high recall for “No,” lower for “Yes”).  
   - Suggested next steps:  
     - Apply **SMOTE** or undersampling methods to balance classes.  
     - Explore **class-weighted** models and **tree-based ensembles**.  
     - Perform **threshold tuning** to improve recall on the minority class.  

---

## Key Findings  
- **Top predictors:** `OverTime_Yes`, `BusinessTravel_Travel_Frequently`, `MaritalStatus_Single`, `MonthlyIncome`.  
- **Performance:** Accuracy ≈78%, Balanced Accuracy ≈71%, ROC AUC ≈0.83.  
- **Limitations:** Strong class imbalance reduces sensitivity to positive attrition cases.  

---

## Folder Structure  
- **`_common/`** → shared utilities (styles, helper scripts, setup).  
- **`data/`** → raw and processed IBM HR datasets.  
- **`reports/`**  
  - `figures/` → confusion matrix, ROC and PR curves.  
  - `artifacts/` → metrics files and model coefficients.  
- **`source/`** → original course notebook before polishing.  
  
---

1. Clone the repository and install dependencies:  
   ```bash
   conda env create -f environment.yml
   conda activate msc-applied-ai
   jupyter lab
   ```
2. Open `02_employee_attrition_ibm_hr/polished/02_employee_attrition_ibm_hr_polished.ipynb`.  
3. Ensure the dataset `WA_Fn-UseC_-HR-Employee-Attrition.csv` is located under `data/`.

---

## Takeaway  
This project demonstrates how a well-designed **Logistic Regression pipeline** can provide interpretable and actionable insights into **employee turnover**.  
Even with limitations from class imbalance, the model highlights meaningful patterns and establishes a strong foundation for more advanced techniques such as **resampling**, **cost-sensitive learning**, or **ensemble methods**.  