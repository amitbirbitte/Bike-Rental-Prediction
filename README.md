# 🚴‍♂️ Bike Rental Prediction — Machine Learning Project

Predict bike rental demand using **daily (day.csv)** and **hourly (hour.csv)** datasets.  
This project demonstrates complete Machine Learning workflow including:  
- Data cleaning & preprocessing  
- EDA & visualization  
- Model training & evaluation  
- Hyperparameter tuning for SVR  
- Flask API deployment  

---

## 📂 Datasets

- **day.csv** — Daily rental counts  
- **hour.csv** — Hourly rental counts  

**Target variable:** `cnt` (number of rented bikes)

---

## 🧠 Models Trained

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Support Vector Regressor (SVR, tuned using GridSearchCV)  
- Gradient Boosting Regressor  

---

## 📊 Model Performance (Test Results)

> Fill your actual results here

### Day-level Results

| Model | MAE | MSE | RMSE | R² |
|------|-----|-----|------|----|
| Linear Regression | X | X | X | X |
| Decision Tree | X | X | X | X |
| Random Forest | X | X | X | X |
| SVR (tuned) | X | X | X | X |
| Gradient Boosting | X | X | X | X |

### Hour-level Results

| Model | MAE | MSE | RMSE | R² |
|------|-----|-----|------|----|
| Linear Regression | X | X | X | X |
| Decision Tree | X | X | X | X |
| Random Forest | X | X | X | X |
| SVR (tuned) | X | X | X | X |
| Gradient Boosting | X | X | X | X |

---

## 🚀 Deployment

✔ Saved models using `pickle`  
✔ Flask API endpoints:  
- `/predict_day`  
- `/predict_hour`  

### Example JSON Request

```json
{
  "season": 3,
  "yr": 1,
  "mnth": 7,
  "weekday": 4,
  "workingday": 1,
  "weathersit": 1,
  "temp": 0.67,
  "atemp": 0.65,
  "hum": 0.48,
  "windspeed": 0.19
}
```

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy, Scikit‑Learn  
- Matplotlib, Seaborn  
- Flask  
- Pickle  

---

## 📁 Project Structure

```
📦 BikeRentalPrediction
├─ data/
│  ├─ day.csv
│  └─ hour.csv
├─ models/
│  ├─ bike_rental_day.pkl
│  └─ bike_rental_hour.pkl
├─ notebook.ipynb
├─ app.py
└─ README.md
```

---

## ✍️ Author

**Your Name**  
Data Analyst & Machine Learning Enthusiast
