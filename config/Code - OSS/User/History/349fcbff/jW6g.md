# Obesity Prediction App

This is a Streamlit web application that predicts obesity categories based on user input features such as Age, Gender, Height, Weight, BMI, and Physical Activity Level. The app uses trained machine learning models (Logistic Regression and SVM) to make predictions.

## Hosted App

The app is hosted on Streamlit and can be accessed [here](https://obesity.streamlit.app).

## Features

- Interactive web interface to input user data
- Option to select between Logistic Regression and SVM models for prediction
- Displays predictions for obesity categories

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**

   ```sh
   git clone https://github.com/karthickeyan17/Obesity_Detector.git
   cd Obesity_Detector 
2. **Create and activate a virtual environment**
  For macOS/Linux:

sh

python3 -m venv env
source env/bin/activate

For Windows:

sh

python -m venv env
env\Scripts\activate

3. **Install the dependencies**

sh

pip install -r requirements.txt

Running the App

    Run the Streamlit app

    sh

streamlit run app.py

Open your web browser

Navigate to http://localhost:8501 to interact with the app.