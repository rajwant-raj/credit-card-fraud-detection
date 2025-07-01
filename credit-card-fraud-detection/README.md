# credit-card-fraud
💳 Detect fraudulent credit card transactions using machine learning. Includes a Gradio web app, trained model, and interactive demo. Built with Python, scikit-learn, and Gradio — ready for deployment on Hugging Face Spaces.
# 💳 Credit Card Fraud Detection using Machine Learning + Gradio

Welcome! This project is a real-world machine learning solution to detect fraudulent credit card transactions using a trained classification model. It includes everything from data analysis and model training to a fully interactive Gradio web app that anyone can use — no coding required!

---

## 📌 Problem Statement

Credit card fraud is a serious financial crime that affects millions globally. Using a dataset of real transactions (with some anonymized features), the goal is to **build a machine learning model** that can classify transactions as:

- ✅ Legitimate (0)
- ⚠️ Fraudulent (1)

---

## 📂 Project Structure

credit-card-fraud-detection/
│
├── app.py # Gradio web interface (entry point)
├── fraud_model.pkl # Trained ML model (Logistic Regression)
├── creditcard.csv # Dataset (anonymized credit card transactions)
├── credit_card_fraud_detection.ipynb # Colab notebook for EDA + training
├── requirements.txt # All dependencies needed
└── README.md # You’re reading it!
---

## 📊 Dataset Info

- **Source**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Size**: 284,807 transactions
- **Imbalance**: Only ~0.17% of transactions are fraudulent
- **Features**:
  - `V1` to `V28`: PCA-transformed values for privacy
  - `Amount`: Transaction amount (normalized)
  - `Class`: Target (0 = Legit, 1 = Fraud)

---

## 🧠 Machine Learning Pipeline

1. **EDA & Preprocessing**:
   - Normalized `Amount`
   - Dropped `Time` column
   - Checked class imbalance

2. **Model Training**:
   - Model used: `Logistic Regression`
   - Evaluated with: `Precision`, `Recall`, `F1-score`, `Confusion Matrix`, `ROC AUC`

3. **Saving the Model**:
   - Trained model saved as `fraud_model.pkl` using `joblib`

---

## 🌐 Gradio Web App

An easy-to-use interactive frontend is built with **Gradio**.

### ✅ Features:
- 29 input fields: `V1–V28` + `Normalized Amount`
- Instant fraud prediction
- Friendly labels and response
- One-click Clear button

---

### 🖥️ How to Run the App Locally

Make sure Python is installed, then:

```bash
git clone https://github.com/rajwant-raj/credit-card-fraud-detection.git
cd credit-card-fraud-detection
pip install -r requirements.txt
python app.py
Visit: http://localhost:7860 in your browser.

🚀 Deploying on Hugging Face Spaces (FREE!)
You can host this app online using Hugging Face + Gradio:

Create a free account on https://huggingface.co

Click "New Space" > Choose Gradio

Name your space: credit-card-fraud-detection

Either:

Link your GitHub repo, OR

Upload files manually (app.py, fraud_model.pkl, requirements.txt)

Wait for deployment (~2 mins)

            or

🔗 You’ll can  run locally through -
     local URL:  http://127.0.0.1:7860

## 📸 Screenshots

### 🖥️ Gradio App UI
![Gradio UI](![gradio-creditcard-app ui](https://github.com/user-attachments/assets/cec19231-76c9-4832-8828-3ee0bca52212)
)

### 📊 sample test
![Test](![Screenshot 2025-07-01 204641](https://github.com/user-attachments/assets/ade29f3d-d517-4aa8-b1be-e8da23c902e8)
)


📦 Requirements
Install all dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Includes:
gradio
scikit-learn
joblib
pandas
numpy

🧠 Learnings & Takeaways
Handling imbalanced datasets

Data normalization and PCA features

Model performance beyond accuracy (Precision/Recall)

Building & deploying real ML apps for users

🙋‍♂️ Author
rajwant-raj – GitHub

Made with ❤️ , and with the help of scalezix and harsh sir.

------------------------------------------------------------------------------------------------
📄 License
This project is open-sourced under the MIT License.










