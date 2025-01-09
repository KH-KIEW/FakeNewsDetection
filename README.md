# Project_Nest_3_218

Here's a detailed explanation of your **Fake News Detection** project documentation and its breakdown:

---

### **Fake News Detection Using Python**
A machine learning-based Python software program for detecting fake news articles using libraries such as `numpy`, `pandas`, `pickle`, and `scikit-learn`.

---

### **Project Overview**
This project leverages natural language processing (NLP) techniques and machine learning algorithms to classify news articles as true or false using Python's sci-kit libraries.

#### **Main Features**
1. Preprocessing and feature extraction using NLP methods.
2. Implementation of multiple classifiers to determine the most accurate model.
3. Probability-based classification with the best-performing model (Logistic Regression).

---

### **Getting Started**

#### **Prerequisites**
- **Python 3.6:** Download it [here](https://www.python.org/downloads/). Set up the PATH variable (optional) following [these instructions](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/).
- **Anaconda (Optional):** Download it [here](https://www.anaconda.com/download/).

Install required libraries:
- Using Python:
  ```bash
  pip install -U scikit-learn numpy scipy
  ```
- Using Anaconda:
  ```bash
  conda install -c anaconda scikit-learn numpy scipy
  ```

#### **Dataset Used**
- **Source:** LIAR dataset, containing train, test, and validation datasets in `.tsv` format.
- **Variables Selected:** Simplified to two columns:
  - **Statement:** News headline or text.
  - **Label:** True (True, Mostly-true, Half-true) or False (Barely-true, False, Pants-fire).
- **Modified Dataset Format:** Saved as `.csv` files (`train.csv`, `test.csv`, `valid.csv`).

---

### **File Descriptions**

1. **`DataPrep.py`:** Handles data preprocessing, including tokenization, stemming, and exploratory data analysis.
2. **`FeatureSelection.py`:** Extracts features using methods such as:
   - Bag-of-Words, N-grams, TF-IDF weighting.
   - Future options: Word2Vec, POS tagging.
3. **`classifier.py`:**
   - Implements multiple classifiers (Naive Bayes, Logistic Regression, SVM, SGD, Random Forest).
   - Compares models using F1-score, confusion matrix, precision-recall, and learning curves.
   - Saves the best model (`Logistic Regression`) as `final_model.sav`.
4. **`prediction.py`:**
   - Uses the saved Logistic Regression model to classify user-input news headlines as "True" or "False".
   - Provides a probability of truth.

---

### **Process Flow**
1. Data is preprocessed and features are extracted.
2. Multiple classifiers are trained and evaluated.
3. The best classifier (Logistic Regression) is selected for deployment.
4. User inputs a news headline to receive classification results.

---

### **Performance**
- Best-performing model: **Logistic Regression** (F1 score in the 70s).
- Limitations:
  - Small dataset size.
  - Simplified feature selection methods.
- Future Enhancements:
  - Integrate Word2Vec, POS tagging, and topic modeling.
  - Increase training dataset size for improved accuracy.

---

### **Installation and Usage**

#### **Clone the Repository**
```bash
git clone https://github.com/nishitpatel01/Fake_News_Detection.git
cd Fake_News_Detection
```

#### **Run the Prediction Program**
1. **Using Python:**
   - If PATH is set:
     ```bash
     python prediction.py
     ```
   - If PATH is not set:
     ```bash
     /path/to/python.exe /path/to/Fake_News_Detection/prediction.py
     ```
2. **Using Anaconda:**
   ```bash
   python prediction.py
   ```

3. Enter a news headline when prompted to classify it as "True" or "False."

---

### **Next Steps**
- Introduce advanced NLP techniques for feature selection.
- Expand the dataset to improve model generalizability.
- Enhance the model pipeline with more robust preprocessing.

---

This documentation can be directly used for your project, ensuring a clear and comprehensive guide for developers and users. Let me know if you'd like modifications or additions!
