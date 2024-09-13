import streamlit as st
import pandas as pd
import pickle as pk

# Load the trained models
lr_model = pk.load(open("model1.pkl", "rb"))
svm_model = pk.load(open("model2.pkl", "rb"))

# Function to get user input
def get_user_input():
    Gender = st.sidebar.selectbox('Gender', (0, 1))
    Age = st.sidebar.slider('Age', 0, 100, 25)
    Height = st.sidebar.slider('Height (in cm)', 100, 220, 170)
    Weight = st.sidebar.slider('Weight (in kg)', 30, 200, 70)
    family_history_with_overweight = st.sidebar.selectbox('Family history with overweight', (0, 1))
    FAVC = st.sidebar.selectbox('Frequent consumption of high caloric food', (0, 1))
    FCVC = st.sidebar.slider('Frequency of vegetables consumption', 1, 3, 2)
    NCP = st.sidebar.slider('Number of main meals', 1, 4, 3)
    CAEC = st.sidebar.selectbox('Consumption of food between meals', (0, 1, 2, 3))
    SMOKE = st.sidebar.selectbox('Smoking habit', (0, 1))
    CH2O = st.sidebar.slider('Daily water consumption (liters)', 1, 3, 2)
    SCC = st.sidebar.selectbox('Calories consumption monitoring', (0, 1))
    FAF = st.sidebar.slider('Physical activity frequency', 0, 3, 1)
    TUE = st.sidebar.slider('Time using technology devices', 0, 2, 1)
    CALC = st.sidebar.selectbox('Consumption of alcohol', (0, 1, 2, 3))
    MTRANS = st.sidebar.selectbox('Mode of transportation', (0, 1, 2, 3, 4))

    user_data = {
        'Gender': Gender,
        'Age': Age,
        'Height': Height,
        'Weight': Weight,
        'family_history_with_overweight': family_history_with_overweight,
        'FAVC': FAVC,
        'FCVC': FCVC,
        'NCP': NCP,
        'CAEC': CAEC,
        'SMOKE': SMOKE,
        'CH2O': CH2O,
        'SCC': SCC,
        'FAF': FAF,
        'TUE': TUE,
        'CALC': CALC,
        'MTRANS': MTRANS
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
st.write(lr_prediction[0])

st.subheader('SVM Prediction:')
st.write(svm_prediction[0])
