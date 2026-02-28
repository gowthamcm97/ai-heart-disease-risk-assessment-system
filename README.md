# 🫀 AI-Powered Heart Disease Risk Assessment System

## APP- https://huggingface.co/spaces/gowtham9731/heart-disease-predictor
## 📌 1. Problem Statement

Cardiovascular disease remains one of the leading causes of mortality worldwide. Early detection of heart disease risk can significantly improve preventive healthcare outcomes.

This project builds a machine learning–based risk assessment system that predicts the probability of heart disease using clinical indicators and symptom-based inputs.

The goal is to create a lightweight, deployable AI system that can assist in preliminary health risk screening.

---

## 🎯 2. Business & Healthcare Impact

This system can:

- Assist doctors in early-stage risk identification  
- Support telemedicine platforms  
- Enable symptom-based screening tools  
- Reduce diagnostic delays  
- Improve preventive care strategies  

In real-world healthcare systems, such a model could be integrated into hospital dashboards or patient self-screening portals.

---

## 📊 3. Dataset Overview

The dataset includes:

- Age  
- Sex  
- Chest pain type  
- Resting blood pressure  
- Cholesterol level  
- Fasting blood sugar  
- ECG results  
- Maximum heart rate  
- Exercise-induced angina  
- ST depression  
- Number of major vessels  
- Thallium test result  

---

## 🏗 4. Project Architecture

User Input (Symptoms)
↓
Feature Mapping & Encoding
↓
Preprocessing Pipeline
↓
Trained Machine Learning Model
↓
Probability Estimation
↓
Risk Interpretation Output


---

## ⚙️ 5. Model Development Process

### 🔎 Exploratory Data Analysis (EDA)

- Checked missing values  
- Analyzed feature distributions  
- Identified correlations between features and target  
- Visualized relationships using plots  

### 🧠 Models Evaluated

- Logistic Regression  
- Random Forest Classifier  
- Support Vector Machine  

The final model was selected based on performance metrics and generalization ability.

### 🔁 Validation Strategy

- Train-test split  
- Cross-validation  
- Performance comparison  

---

## 📈 6. Model Performance

- Accuracy: 88.47%  
- ROC-AUC: 0.95  
- F1 Score: 0.84  

---

## 🚀 7. Deployment

The model is deployed using:

- Gradio (UI)  
- Scikit-learn (Modeling)  
- Joblib (Model Serialization)  

Users can input symptoms through an interactive interface and receive:

- Risk classification (High / Low)  
- Probability percentage  
- Basic interpretation  

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python app.py
