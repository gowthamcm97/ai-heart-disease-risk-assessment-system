import gradio as gr
import joblib
import numpy as np

model = joblib.load("heart_model.pkl")

def predict_heart_disease(age, sex,
                          chest_pain,
                          bp_symptom,
                          chol_symptom,
                          sugar_symptom,
                          ekg_symptom,
                          hr_symptom,
                          exercise_pain,
                          st_depression_symptom,
                          slope_symptom,
                          vessels_symptom,
                          thal_symptom):

    sex_map = {"Female": 0, "Male": 1}

    cp_map = {
        "Severe crushing chest pain": 1,
        "Moderate chest discomfort": 2,
        "Mild chest pain during activity": 3,
        "No chest pain": 4
    }

    bp_map = {
        "Normal BP": 120,
        "Occasional headache / dizziness": 135,
        "Frequent headache / blurred vision": 155
    }

    chol_map = {
        "Healthy / No symptoms": 180,
        "Mild tiredness": 220,
        "Chest pain / breathlessness": 260
    }

    sugar_map = {
        "Normal energy": 0,
        "Frequent thirst / urination": 1
    }

    ekg_map = {
        "Normal heartbeat": 0,
        "Mild irregular heartbeat": 1,
        "Severe abnormal rhythm": 2
    }

    hr_map = {
        "Normal stamina": 150,
        "Low stamina / fatigue": 100,
        "Rapid heartbeat": 180
    }

    exang_map = {
        "No chest pain during exercise": 0,
        "Chest pain during exercise": 1
    }

    oldpeak_map = {
        "No stress symptoms": 0.5,
        "Mild chest discomfort": 2.0,
        "Severe chest pain during exertion": 4.0
    }

    slope_map = {
        "Normal exercise response": 1,
        "Moderate heart stress": 2,
        "Abnormal heart response": 3
    }

    vessels_map = {
        "No blockage symptoms": 0,
        "Mild blockage symptoms": 1,
        "Frequent chest pain": 2,
        "Severe blockage symptoms": 3
    }

    thal_map = {
        "Normal blood flow": 3,
        "Mild blood flow issue": 6,
        "Serious blood flow problem": 7
    }

    features = np.array([[
        age,
        sex_map[sex],
        cp_map[chest_pain],
        bp_map[bp_symptom],
        chol_map[chol_symptom],
        sugar_map[sugar_symptom],
        ekg_map[ekg_symptom],
        hr_map[hr_symptom],
        exang_map[exercise_pain],
        oldpeak_map[st_depression_symptom],
        slope_map[slope_symptom],
        vessels_map[vessels_symptom],
        thal_map[thal_symptom]
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1] * 100

    if prediction == 1:
        return f"⚠️ High Risk of Heart Disease\nRisk Probability: {probability:.2f}%"
    else:
        return f"✅ Low Risk of Heart Disease\nRisk Probability: {probability:.2f}%"

interface = gr.Interface(
    fn=predict_heart_disease,
    inputs=[

        gr.Slider(20, 100, label="Age"),
        gr.Radio(["Female", "Male"], label="Sex"),

        gr.Radio([
            "Severe crushing chest pain",
            "Moderate chest discomfort",
            "Mild chest pain during activity",
            "No chest pain"
        ], label="Chest Pain"),

        gr.Radio([
            "Normal BP",
            "Occasional headache / dizziness",
            "Frequent headache / blurred vision"
        ], label="Blood Pressure Symptoms"),

        gr.Radio([
            "Healthy / No symptoms",
            "Mild tiredness",
            "Chest pain / breathlessness"
        ], label="Cholesterol Symptoms"),

        gr.Radio([
            "Normal energy",
            "Frequent thirst / urination"
        ], label="Blood Sugar Symptoms"),

        gr.Radio([
            "Normal heartbeat",
            "Mild irregular heartbeat",
            "Severe abnormal rhythm"
        ], label="EKG Result"),

        gr.Radio([
            "Normal stamina",
            "Low stamina / fatigue",
            "Rapid heartbeat"
        ], label="Heart Rate Response"),

        gr.Radio([
            "No chest pain during exercise",
            "Chest pain during exercise"
        ], label="Exercise-Induced Angina"),

        gr.Radio([
            "No stress symptoms",
            "Mild chest discomfort",
            "Severe chest pain during exertion"
        ], label="ST Depression"),

        gr.Radio([
            "Normal exercise response",
            "Moderate heart stress",
            "Abnormal heart response"
        ], label="Slope of ST"),

        gr.Radio([
            "No blockage symptoms",
            "Mild blockage symptoms",
            "Frequent chest pain",
            "Severe blockage symptoms"
        ], label="Blood Vessel Condition"),

        gr.Radio([
            "Normal blood flow",
            "Mild blood flow issue",
            "Serious blood flow problem"
        ], label="Thallium Test")
    ],

    outputs="text",
    title="❤️ Symptom-Based Heart Disease Risk Assessment",
    description="Select symptoms to estimate heart disease risk. Educational use only."
)

interface.launch()