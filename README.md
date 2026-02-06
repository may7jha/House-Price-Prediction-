# 🏠 House Price Prediction – End-to-End ML Web App

🌐 **Live App:**  
👉 https://2zfehqmwak3s3cu6k5lgas.streamlit.app/

---

## 📌 Business Problem

Real estate price estimation depends on multiple factors such as area, quality, age of property, and amenities.  
Manual estimation is subjective and error-prone.

This project provides a **Machine Learning powered system** that:

- Accepts house details from user  
- Processes them using trained ML model  
- Predicts house price instantly through a web interface  

---

## 🤖 Model Overview

- **Algorithm:** Random Forest Regressor  
- **Target Variable:** Sale Price  
- **Evaluation Metrics:**

| Metric | Value |
|------|-------|
| RMSE | 28,767 |
| R² Score | 0.89 |

The model was trained on structured housing data with proper preprocessing and feature engineering.

---

## 🧠 How the Model Was Trained

### Dataset Features Used
- GrLivArea  
- OverallQual  
- GarageArea  
- YearBuilt  
- LotArea  

### Preprocessing Steps
- Selected important numerical features  
- Handled missing values  
- Train-Test split (80-20)  
- Feature scaling  
- Column alignment for prediction  

### Training Pipeline
1. Load dataset  
2. Clean & preprocess  
3. Train Random Forest model  
4. Evaluate using RMSE & R²  
5. Save model using `joblib`  
6. Save training columns for consistency  

---

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- Joblib  
- Streamlit  
- Git & GitHub  

---

## ⚙ How to Run Locally

```bash
# Clone repository
git clone https://github.com/may7jha/House-Price-Prediction.git
cd House-Price-Prediction

# Create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

---

## 🔁 Prediction Pipeline

1. User enters house details  
2. Input converted to DataFrame  
3. Columns aligned with training  
4. Model predicts price  
5. Result displayed on UI  

---

## 🖼 Application Screenshots

### 1. Input Dashboard  
![Dashboard](images/dashboard.png)

### 2. Entering Details  
![Input](images/input.png)

### 3. Prediction Result  
![Result](images/result.png)

---

## 📈 Future Enhancements

- Add location feature  
- Compare models (XGBoost, LightGBM)  
- Add EDA dashboard  
- FastAPI backend  
- User authentication  

---

## 👤 Author

**Mayank Jha** – Aspiring Data Scientist  
GitHub: https://github.com/may7jha  

⭐ If you like this project, give it a star!
