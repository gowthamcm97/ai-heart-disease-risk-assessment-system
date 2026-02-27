###🫀 AI-Powered Heart Disease Risk Assessment System

##📌 1. Problem Statement

Cardiovascular disease remains one of the leading causes of mortality worldwide. Early detection of heart disease risk can significantly improve preventive healthcare outcomes.

This project builds a machine learning–based risk assessment system that predicts the probability of heart disease using clinical indicators and symptom-based inputs.

The goal is to create a lightweight, deployable AI system that can assist in preliminary health risk screening.

.

##🎯 2. Business & Healthcare Impact

This system can:
A.Assist doctors in early-stage risk identification
B.Support telemedicine platforms
C.Enable symptom-based screening tools
D.Reduce diagnostic delays
E.Improve preventive care strategies

In real-world healthcare systems, such a model could be integrated into hospital dashboards or patient self-screening portals.

##📊 3. Dataset Overview

Age, Sex, Chest pain type, Resting blood pressure, Cholesterol level, Fasting blood sugar, ECG results, Maximum heart rate, Exercise-induced angina, ST depression, Number of major vessels, Thallium test result

##🏗 4. Project Architecture

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

⚙️ 5. Model Development Process

🔎 Exploratory Data Analysis (EDA)
A.Checked missing values
B.Analyzed feature distributions
C.Identified correlations between features and target
D.Visualized relationships using plots

##🧠 Models Evaluated
A.Logistic Regression
B.Random Forest Classifier
C.Support Vector Machine (optional if you tested)
D.The final model was selected based on performance metrics and generalization ability.

##🔁 Validation Strategy
A.Train-test split
B.Cross-validation
C.Performance comparison

##📈 6. Model Performance

A.Accuracy: 88.47%
B.ROC-AUC: 0.95
C.F1 Score: 0.84

##🚀 7. Deployment

The model is deployed using:
A.Gradio for UI
B.Scikit-learn for modeling
C.Joblib for model serialization

Users can input symptoms through an interactive interface and receive:
A.Risk classification (High / Low)
B.Probability percentage
C.Basic interpretation

##▶️ How to Run Locally

pip install -r requirements.txt
python app.py
