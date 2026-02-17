# Document Clustering & News Classification

📄 **Project Documentation:** *[Google Drive](https://drive.google.com/file/d/15ShlpqPuq2VxqPzjZPAme9rSJfYSX9vL/view?usp=sharing)*  
🧑‍💻 **Code:** [Notebook](./Notebooks)

---

## Overview

This project explores **text similarity, document clustering, and large-scale news classification** using Natural Language Processing (NLP) and machine learning techniques.

Two main experiments are conducted:

1. **Clustering introduction documents** related to linear regression to measure semantic similarity between sentences.
2. **Classifying ~200k news headlines** from HuffPost into **40 categories** using vectorization and supervised learning.

---

## Objectives

- Measure **sentence similarity** through text vectorization.
- Apply **unsupervised clustering** to group related documents.
- Train **supervised classifiers** for large-scale news categorization.
- Compare **vectorization techniques** and evaluate model accuracy.

---

## Datasets

### 1. Introductions Dataset
- 12 `.txt` documents collected from research papers and articles about **linear regression**.
- Used for **unsupervised clustering** and similarity analysis.

### 2. News Dataset
- ~200,000 HuffPost headlines from **2012–2018**.
- Labeled with **40 news categories**.
- Used for **supervised text classification**.

---

## Pipeline Architecture

### 1. Corpus Loading
- Custom **CorpusLoader** converts `.txt` or `.json` datasets into:
  - **Pandas DataFrame**
  - **NumPy array**
- Provides structured access to unstructured text.

### 2. Text Normalization
- Removes:
  - Stopwords  
  - Punctuation  
  - Numbers  
- Applies **NLTK lemmatization** to reduce words to root forms.

### 3. Vectorization Methods

Three Scikit-learn vectorizers are evaluated:

- **Count Vectorizer**
- **TF-IDF Vectorizer**
- **Hashing Vectorizer**

---

## Machine Learning Approaches

### Unsupervised Learning
- **MiniBatch K-Means clustering** for document grouping.
- **Silhouette score** used to determine optimal cluster count.
- **PCA visualization** applied for 2D cluster inspection.

### Supervised Learning
- **Stochastic Gradient Descent (SGD) classifier** for:
  - Cluster label prediction
  - News category classification
- **7-fold cross-validation** used for robust evaluation.

---

## Key Results

### Clustering Insights
- Optimal clustering determined via **Silhouette scoring**.
- PCA visualization confirms **separable semantic groups**.

### News Classification Findings

- **Headlines** are strong predictors of news category.
- **Short descriptions** lack consistent patterns for prediction.
- **TF-IDF and Hashing vectorizers** show similar accuracy,
  while **Hashing** offers faster processing for large datasets.
