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
| Linear Regression | 583.0 | 634351.3 | 794.4 | 0.84 |
| Decision Tree | 586.1 | 827773.4 | 909.8 | 0.79 |
| Random Forest | 440.1 | 463235.2 | 680.6 | 0.88 |
| SVR (tuned) | 1691.3 | 3990231.2 | 1997.5 | 0.049 |
| Gradient Boosting | 443.9 | 410257.8 | 640.5 | 0.89 |

### Hour-level Results

| Model | MAE | MSE | RMSE | R² |
|------|-----|-----|------|----|
| Linear Regression | 74.1 | 10089.3 | 100.4 | 0.68 |
| Decision Tree | 39.9 | 4356.9 | 66.6 | 0.86 |
| Random Forest | 29.5 | 2236.5 | 47.2 | 0.92 |
| SVR (tuned) | 92.1 |19075.5 | 138.1 | 0.39 |
| Gradient Boosting | 58.0 | 6383.3 | 79.8 | 0.79 |

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

**Your Amit Birbitte**
Data Analyst & Machine Learning Enthusiast
