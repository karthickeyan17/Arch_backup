import streamlit as st
import pandas as pd
import pickle as pk

# Load the trained models
lr_model = pk.load(open("model1.pkl", "rb"))
svm_model = pk.load(open("model2.pkl", "rb"))

# Function to get user input
def get_user_input():
    Age = st.sidebar.slider('Age', 0, 100, 25)
    Gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    Height = st.sidebar.slider('Height (in cm)', 100, 220, 170)
    Weight = st.sidebar.slider('Weight (in kg)', 30, 200, 70)
    PhysicalActivityLevel = st.sidebar.slider('Physical Activity Level', 1, 4, 3)
    
    user_data = {
        'Age': Age,
        'Gender': 0 if Gender=='Male' else 1,
        'Height': Height,
        'Weight': Weight,
        'BMI': Weight//(Height**2),
        'PhysicalActivityLevel': PhysicalActivityLevel
    }
    
    features = pd.DataFrame(user_data, index=[0])
    return features

# Get user input
user_input = get_user_input()

# Display user input
st.subheader('User Input:')
st.write(user_input)

# Make predictions
lr_prediction = lr_model.predict(user_input)
svm_prediction = svm_model.predict(user_input)

st.subheader('Logistic Regression Prediction:')
st.write([lr_prediction])

st.subheader('SVM Prediction:')
st.write([svm_prediction])
