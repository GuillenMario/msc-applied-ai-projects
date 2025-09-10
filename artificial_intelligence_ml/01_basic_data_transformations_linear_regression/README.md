# California Housing — Linear Regression Case Study  

## Overview  
This project applies **linear regression models** to predict housing prices in California, using the [California Housing dataset](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html). The notebook demonstrates a complete ML workflow, from **data auditing** to **model evaluation**, with a focus on good practices and interpretability.  

---

## Workflow  
1. **Data Loading & Audit**  
   - Checked for missing values and invalid entries.  
   - Generated descriptive statistics, skew/kurtosis, and IQR outlier reports.  
   - Explored correlations and identified collinearity (e.g., population vs. rooms/households).  

2. **Preprocessing & Feature Engineering**  
   - Selected a reduced feature set to simplify modeling.  
   - Engineered a new feature: `bedroom_ratio = total_bedrooms / total_rooms`.  
   - Built preprocessing pipelines for numeric and categorical variables.  

3. **Modeling & Validation**  
   - Established a baseline using a **DummyRegressor**.  
   - Compared **Ordinary Least Squares (OLS)**, **Ridge**, and **Lasso**.  
   - Tuned hyperparameters (α) for Ridge and Lasso using `GridSearchCV`.  

4. **Evaluation & Error Analysis**  
   - Residuals vs predicted plot, QQ-plot, and histogram to assess assumptions.  
   - Identified most influential features from the model coefficients.  
   - Saved metrics and plots into the project’s `reports/` folder.  

5. **Conclusions & Next Steps**  
   - Ridge/Lasso reduced error compared to baseline but RMSE remained high (~71k).  
   - Residual plots revealed a systematic bias: underestimation of low-priced homes and overestimation of high-priced ones.  
   - Suggested next steps: log-transforming the target, adding interaction terms, or using tree-based models.  

---

## Key Findings  
- **Top predictors:** `median_income`, `total_bedrooms`, `total_rooms`.  
- **Performance:** RMSE ≈ 71k on test set (≈30% of average house value).  
- **Limitations:** Linear models cannot capture non-linear dynamics of housing prices.  

---

## Folder Structure  
- **`_common/`** → Shared utilities (setup notebook, helper scripts, style files). This folder is outside the current California Housing folder.  
- **`data/`**  → original datasets (e.g., `housing.csv`).  
- **`reports/`**  
  - `figures/` → saved plots (residuals, QQ-plots, histograms).  
  - `artifacts/` → metrics files (`metrics.json`), model outputs.  
- **`source/`** → original unpolished notebooks provided as course material.  
---

## How to Run  
1. Clone the repository and install dependencies:  
   ```bash
   conda env create -f environment.yml
   conda activate msc-applied-ai
   jupyter lab
   ```
2. Open `01_basic_data_transformations_linear_regression/polished/01_basic_data_transformations_linear_regression_polished.ipynb`.  
3. Ensure the dataset `housing.csv` is located under `data/raw/`.  

Outputs (plots and metrics) will be saved automatically to `reports/figures/` and `reports/artifacts/`.  

---

## Takeaway  
Even when performance is limited, a well-structured linear regression workflow provides valuable insights into data quality, feature importance, and model assumptions — laying the groundwork for more complex models.  
