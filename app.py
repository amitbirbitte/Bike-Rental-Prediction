from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# 1. Load the saved model when Flask starts
with open("bike_rental_model.pkl", "rb") as f:
    model = pickle.load(f)

# 2. Define the columns in the same order as training
FEATURE_COLUMNS = [
    "season", "yr", "mnth", "holiday", "weekday",
    "workingday", "weathersit", "temp", "atemp", "hum", "windspeed"
]

@app.route("/")
def home():
    return "Bike Rental Prediction API is running!"

# 3. Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects JSON input with keys matching FEATURE_COLUMNS.
    Example:
    {
      "season": 3,
      "yr": 1,
      "mnth": 7,
      "holiday": 0,
      "weekday": 4,
      "workingday": 1,
      "weathersit": 1,
      "temp": 0.6,
      "atemp": 0.58,
      "hum": 0.5,
      "windspeed": 0.2
    }
    """
    data = request.get_json()

    # Convert single JSON to DataFrame
    df = pd.DataFrame([data], columns=FEATURE_COLUMNS)

    # Use the loaded model to predict
    prediction = model.predict(df)[0]

    # Return as JSON (convert numpy types to normal float)
    return jsonify({
        "prediction": float(prediction)
    })

if __name__ == "__main__":
    # debug=True only for development
    app.run(host="0.0.0.0", port=5000, debug=True)
