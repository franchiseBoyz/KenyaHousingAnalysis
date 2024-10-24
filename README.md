# Kenyan Housing Price Prediction API

This project is a **Flask-based API** that predicts housing prices for apartments located in **Nairobi** and **Mombasa**, Kenya. The data was **scraped from Property24** by [Beverlyn Akoth](https://www.kaggle.com/beverlyneakoth) and includes apartment listings with details such as the number of bedrooms, bathrooms, and the city of the listing.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [API Endpoints](#api-endpoints)
- [Model Details](#model-details)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This is a **Kenya-based housing price prediction API** focusing on the cities of **Nairobi** and **Mombasa**. The data was scraped by [Beverlyn Akoth](https://www.kaggle.com/beverlyneakoth) from the Property24 website, which displays various apartment listings in Kenya. The scraped data includes the location, number of bedrooms, bathrooms, and, in some cases, floor sizes (though floor sizes were excluded due to a lack of sufficient data).

The project uses **machine learning models** to predict the housing prices based on the available data. The best-performing model is deployed through the API, which users can interact with via a simple frontend or by sending requests directly to the API.

## Features

- **Predict housing prices** based on input features like the number of bedrooms, bathrooms, and city.
- **Kenya-focused dataset** with apartments from Nairobi and Mombasa.
- **Frontend user interface** that allows users to enter details and receive price predictions.
- **Flask-based API** that allows for easy integration into other applications.

## Architecture

The architecture of the project is as follows:

1. **Data Collection**: Data was scraped from the Property24 website by [Beverlyn Akoth](https://www.kaggle.com/beverlyneakoth).
2. **Model Training**: Several machine learning models were trained to predict housing prices, and the best model was saved using `joblib`.
3. **API Development**: Flask is used to develop an API that takes user inputs (bedrooms, bathrooms, city) and returns a price prediction.
4. **Frontend**: A simple HTML and JavaScript frontend interacts with the API for user-friendly price predictions.

## Installation

### Prerequisites

- Python 3.8+
- Flask
- Joblib
- Pandas
- Scikit-learn
- Requests

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/kenya-housing-price-prediction.git
    cd kenya-housing-price-prediction
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:

    ```bash
    python app.py
    ```

5. Access the app by visiting `http://127.0.0.1:5000` in your browser.

## Usage

You can use the app in two ways:

1. **Frontend Interface**: Open the web page where you can input the number of bedrooms, bathrooms, and the city (Nairobi or Mombasa) and receive a predicted price.
2. **API**: Send a `POST` request to the `/predict` endpoint with JSON input.

### API Example

- **Endpoint**: `/predict`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:

    ```json
    {
        "bedrooms": 3,
        "bathrooms": 2,
        "city_Nairobi": 1,
        "city_Mombasa": 0
    }
    ```

- **Response**:

    ```json
    [1234567.89]  # Predicted price
    ```

## Technologies

- **Flask**: Python micro-framework for the web application.
- **Pandas**: For data manipulation and cleaning.
- **Scikit-learn**: For training the machine learning models.
- **Joblib**: For saving and loading the machine learning model.
- **HTML, CSS, JavaScript**: For the frontend.

## API Endpoints

1. `/`: Returns a welcome message.
2. `/predict`: Accepts a `POST` request with JSON data and returns the predicted housing price.

## Model Details

The following models were trained on the dataset, and the best-performing model was selected for deployment:

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- Support Vector Regressor
- Neural Network (MLP)

The **Random Forest Regressor** gave the best results in terms of performance metrics and was saved using `joblib`.

## Future Enhancements

- Extend the dataset to include more cities and regions across Kenya.
- Add more features like floor size, neighborhood details, and building age.
- Improve the frontend with more interactive elements and better UI design.
- Deploy the app on a cloud platform like **Microsoft Azure**.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute.

## License

This project is licensed under the MIT License.
