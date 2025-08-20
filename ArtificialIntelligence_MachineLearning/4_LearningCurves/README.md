# **Activity: Learning Curves**

This notebook explores **regression models** to analyze and predict outcomes from a dataset of social media advertising campaigns. The primary goal is to model and evaluate the performance of different machine learning regression techniques applied to social media metrics using **learning curves** and **model comparison**.

## 📊 Dataset

The dataset used is `dataset_Facebook.csv`, which contains multiple features such as:
- Post characteristics (e.g., Post Hour)
- Engagement metrics (e.g., Likes, Shares)
- Campaign attributes (e.g., Type, Category)

---

## 🧪 Models Used

The following regression models are implemented and compared:
- **Random Forest Regressor**
- **XGBoost Regressor**
- **Support Vector Regressor (SVR)**
- **Multi-Layer Perceptron Regressor (MLP)**

Model performance is evaluated using:
- Mean Squared Error (MSE)
- Learning curves
- Cross-validation (Repeated K-Fold)
- Hyperparameter tuning (GridSearchCV, HalvingGridSearchCV, RandomizedSearchCV)
- Permutation feature importance

---

## 🛠️ Libraries Used

Key Python libraries utilized in this notebook include:

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn` (models, pipelines, metrics, hyperparameter search)
- `xgboost`

---

## 📈 Learning Curves

Learning curves are generated to:
- Visualize model performance with increasing training size
- Detect overfitting or underfitting behavior
- Compare generalization error across models

---

## 📂 File Structure

- `LearningCurves_A01796701.ipynb`: Main Jupyter Notebook with code, analysis, and plots
- `dataset_Facebook.csv`: Input dataset (must be in the same directory)

---

## ▶️ Running the Notebook

1. Ensure all required libraries are installed (see above).
2. Place `dataset_Facebook.csv` in the same directory.
3. Open the notebook in Jupyter or VSCode and run cells sequentially.

---

## ✅ Learning Outcomes

- Application of multiple regression algorithms to real-world data
- Proper use of learning curves for model diagnostics
- Effective use of pipelines and transformers for preprocessing
- Use of cross-validation and hyperparameter tuning for performance improvement

---
## 👨‍🎓 Author

- **Mario Alberto Guillen De La Torre**
- Student ID: A01796701
- Professor: Luis Eduardo Falcón Morales

---
## 📌 Course

- Master’s in Applied Artificial Intelligence
- Tecnológico de Monterrey

---
