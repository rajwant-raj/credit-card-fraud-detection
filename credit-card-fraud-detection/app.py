import gradio as gr
import joblib
import numpy as np

# Load the trained model
model = joblib.load(r"credit-card-fraud-detection\fraud_model.pkl")


# Prediction function
def predict_fraud(*features):
    input_data = np.array(features).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    return "⚠️ Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"

# Feature names (28 PCA components + normalizedAmount)
feature_names = [
    "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
    "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
    "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Normalized Amount"
]

# Define input components
inputs = [gr.Number(label=fn) for fn in feature_names]
output = gr.Textbox(label="Prediction")

# Build interface
app = gr.Interface(
    fn=predict_fraud,
    inputs=inputs,
    outputs=output,
    title="💳 Credit Card Fraud Detection",
    description="Enter values for V1 to V28 and Normalized Amount to predict fraud.",
    allow_flagging="never",
    live=True  # Enables "Clear" button
)

# Launch the app
app.launch()
