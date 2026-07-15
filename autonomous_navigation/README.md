# Autonomous Navigation – MSc Applied AI

**Status:** This project is currently in its draft phase. The structure, workflow, and notebook are in place and reviewable, but some sections (metrics, results) may still be refined.

This section is a standalone project developed during my **Master's in Applied Artificial Intelligence**, focusing on **imitation learning for autonomous navigation** using a CNN-based end-to-end steering model built with Keras.

The project simulates an **end-to-end imitation learning pipeline**:
1. Reading recorded driving data (images, commands, and steering angles).
2. Preparing and encoding the data for training (image normalization, command one-hot encoding, stratified train/test split).
3. Defining and training a multi-input neural network (CNN for images + dense network for commands).
4. Visualizing training performance.
5. Saving the trained model and encoder, and demonstrating inference on a new sample.

---

## 📂 Folder Structure

```
autonomous_navigation/
└── 01_imitation_learning/
    └── 01_imitationLearning.ipynb
```

---

## 📊 Notebook Overview

| # | Notebook | Description | Key Techniques | Results / Metrics |
|---|----------|-------------|----------------|------------------|
| 1 | [Imitation Learning](01_imitation_learning/01_imitationLearning.ipynb) | End-to-end steering-angle prediction from images and driving commands | Multi-input CNN + dense network (Keras/Torch backend), OneHotEncoder, stratified train/test split, `ReduceLROnPlateau`, `EarlyStopping` | Training vs. validation loss curves; qualitative inference example |

---

## 📊 Dataset

The recorded driving data is not included due to size.

- Expected structure: an `annotations/annotations.csv` file with `PATH`, `COMMAND`, and `ANGLE` columns, referencing the corresponding image files (typically captured during a data-collection/driving session).
- A `test/` folder with sample images is used for the inference example at the end of the notebook.

---

## ⚙️ Environment Setup

The project runs on the same root environment as the rest of the repo. From repo root:

```bash
conda env create -f ../../environment.yml
conda activate applied_ai
```

Additional notes:
- Uses **Keras** with the **PyTorch backend** (`KERAS_BACKEND=torch`) and a **local GPU** for training.
- Key libraries used: `keras`, `torch`, `scikit-learn`, `numpy`, `pandas`, `opencv-python`, `Pillow`, `matplotlib`.

---

## 📌 Key Takeaways

- Built a **multi-input neural network** that combines a **convolutional branch** (for camera images) with a **dense branch** (for driving commands), merging both to predict a continuous **steering angle**.
- Used **stratified train/test splitting** based on the driving command to keep the class distribution balanced across sets.
- Applied **`ReduceLROnPlateau`** and **`EarlyStopping`** callbacks to stabilize and speed up training, halving the learning rate after 3 epochs without improvement and stopping training (restoring best weights) after 6.
- Persisted both the **trained model** (`.keras`) and the **command encoder** (`.pkl`) so the model can be reloaded and used for inference on new images and commands.

---

### **Final Thoughts**

*(Add your closing reflections here — e.g., what worked well with this imitation learning approach, challenges with data collection or model generalization, and any parameters that required tuning.)*
