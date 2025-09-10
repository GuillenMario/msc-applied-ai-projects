# ai_ml_utils.py
from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    roc_auc_score, average_precision_score, f1_score,
    precision_score, recall_score
)

# Outlier handling
class Winsorizer(BaseEstimator, TransformerMixin):
    """
    Caps numeric columns at given quantiles to reduce outlier impact.
    """
    def __init__(self, columns, lower_q=0.01, upper_q=0.99):
        self.columns = columns
        self.lower_q = lower_q
        self.upper_q = upper_q

    # X: Train Data
    def fit(self, X, y=None):
        Xc = pd.DataFrame(X, columns=self.columns) if not isinstance(X, pd.DataFrame) else X
        self.bounds_ = {}
        for c in self.columns:
            low, high = Xc[c].quantile([self.lower_q, self.upper_q])
            self.bounds_[c] = (low, high)
        return self

    def transform(self, X):
        Xc = X.copy()
        # If input is numpy array (e.g., inside ColumnTransformer), convert to DataFrame to clip by name
        if not isinstance(Xc, pd.DataFrame):
            Xc = pd.DataFrame(Xc, columns=self.columns)
        for c, (low, high) in self.bounds_.items():
            Xc[c] = Xc[c].clip(lower=low, upper=high)
        return Xc[self.columns].values  # return as array to play nice with sklearn


def ensure_dirs(*paths):
    """Create directories if missing."""
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)

def dump_json(obj, path):
    """Write a JSON file with parent dirs created."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
    return p

def evaluate_regression(y_true, y_pred):
    """Return common regression metrics."""
    rmse = mean_squared_error(y_true, y_pred) ** 0.5
    mae  = mean_absolute_error(y_true, y_pred)
    r2   = r2_score(y_true, y_pred)
    return {"rmse": float(rmse), "mae": float(mae), "r2": float(r2)}

def evaluate_classification(y_true, y_prob, threshold=0.5):
    """
    Given probabilities for the positive class, compute ROC-AUC, PR-AUC, and thresholded metrics.
    """
    y_pred = (np.asarray(y_prob) >= threshold).astype(int)
    metrics = {
        "roc_auc": float(roc_auc_score(y_true, y_prob)),
        "pr_auc": float(average_precision_score(y_true, y_prob)),
        "threshold": float(threshold),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
    }
    return metrics

def detect_outliers_iqr(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - k*iqr, q3 + k*iqr
    return series[(series < lower) | (series > upper)]