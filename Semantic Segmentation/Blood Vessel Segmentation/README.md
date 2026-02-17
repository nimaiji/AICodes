# Human Blood Vessel Segmentation

**Paper:** *[Google Drive](https://drive.google.com/file/d/1Ilpa29iZdfE5dXlGCFHlxyfi3Nm9_Wap/view?usp=sharing)*  
**Code:** *[Notebook](main-exp.ipynb)*  
**Kaggle:** [Competition](https://www.kaggle.com/competitions/blood-vessel-segmentation)
---

## Overview

This project presents a **computer vision and deep learning approach** for segmenting **human blood vessels** from medical imaging data.  
The method leverages a **U-Net–based semantic segmentation architecture** applied to **3D HiP-CT kidney images**, combined with preprocessing, augmentation, and optimized loss functions to improve segmentation accuracy.

Accurate vessel segmentation can support:

- Simulation of **blood, oxygen, and drug flow**
- Analysis of **vasculature variations** across demographics
- Automated replacement of **time-consuming manual annotation** in medical research 

---

## Abstract (Short)

We propose a deep learning framework for **pixel-wise segmentation of human vasculature** using U-Net and HiP-CT imaging data.  
The pipeline includes **normalization, resizing, elastic deformation, Gaussian noise, flipping, and test-time augmentation**, alongside **Dice Loss** and **Focal Tversky Loss** comparisons during training on a **Tesla P100 GPU**.  
Results demonstrate how preprocessing choices, augmentation, and loss functions influence segmentation performance and biomedical applicability.

---

## Dataset

- **3D HiP-CT kidney images** stored in `.tiff` format  
- Multiple kidneys with varying **resolutions and label availability**  
- Separate **image–label pairs** for supervised learning  
- Limited dataset size, motivating **augmentation and careful train/validation splitting** 

---

## Methodology

### 1. Preprocessing

- Convert `.tiff` images into tensors  
- **Normalize pixel values** and resize to **512×512**  
- Optimize memory usage for **high-resolution medical imaging** 

### 2. Data Augmentation

To reduce overfitting and improve robustness:

- **Elastic deformation** for biological shape variation  
- **Random Gaussian noise** injection  
- **Horizontal and vertical flips**  
- **Test-Time Augmentation (TTA)** with averaged predictions 

### 3. Model Architecture

- **U-Net convolutional neural network** for semantic segmentation  
- Encoder–decoder with **skip connections** for precise localization  
- Designed for **biomedical pixel-wise prediction tasks** 

### 4. Training Strategy

- Trained on **NVIDIA Tesla P100 GPU**  
- **Early stopping** and **learning rate decay** applied  
- Careful **train/validation split** due to limited data 

---

## Loss Functions

Two segmentation losses were evaluated:

- **Dice Loss** – measures overlap similarity between prediction and ground truth  
- **Focal Tversky Loss** – balances false positives/negatives and improves difficult segmentation cases 

---

## Results & Impact

The proposed pipeline demonstrates:

- Effective **semantic vessel segmentation** from HiP-CT data  
- Sensitivity of performance to **augmentation, preprocessing, and loss design**  
- Potential applications in **vascular simulation, biomedical analysis, and clinical research** 
