from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load your trained model
model = joblib.load('best_model.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Housing Price Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.json
    
    # Check if data is provided
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Convert JSON to DataFrame
    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        return jsonify({"error": "Invalid data format"}), 400

    # Ensure the DataFrame has the correct format
    required_features = ['bedrooms', 'bathrooms', 'city_Nairobi', 'city_Mombasa']

    # Ensure all required features are present
    for feature in required_features:
        if feature not in df.columns:
            df[feature] = 0 

    # Reorder columns to match the model input
    df = df[required_features]

    # Make predictions
    try:
        predictions = model.predict(df)
    except Exception as e:
        logging.error(f"Prediction Error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

    # Convert predictions to a list and return as JSON
    return jsonify({"predictions": predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
