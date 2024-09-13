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
    Height = st.sidebar.slider('Height (in cm)', 100, 220, 170) / 100  # Convert to meters for BMI calculation
    Weight = st.sidebar.slider('Weight (in kg)', 30, 200, 70)
    PhysicalActivityLevel = st.sidebar.slider('Physical Activity Level', 1, 4, 3)
    
    BMI = Weight / (Height ** 2)
    
    user_data = {
        'Age': Age,
        'Gender': 0 if Gender == 'Male' else 1,
        'Height': Height * 100,  # Convert back to cm for the model
        'Weight': Weight,
        'BMI': BMI,
        'PhysicalActivityLevel': PhysicalActivityLevel
    }
    
    features = pd.DataFrame(user_data, index=[0])
    return features

# Main function to run the Streamlit app
def app():
    st.markdown("# Obesity Prediction App\n## Predict your weight category using Logistic Regression or SVM", unsafe_allow_html=True)
    
    # Get user input
    user_input = get_user_input()
    
    # Display user input
    st.subheader('User Input:')
    st.write(user_input)
    
    # Model selection
    model_choice = st.sidebar.selectbox('Choose Model', ('Logistic Regression', 'SVM'))
    
    img_urls = [
        'https://img.freepik.com/free-vector/hand-drawn-strong-man-cartoon-illustration_52683-117786.jpg?size=338&ext=jpg&ga=GA1.1.2008272138.1722902400&semt=ais_hybrid',
        'https://img.freepik.com/free-vector/overweight-man-eating-fast-food-table-isolated_1308-133546.jpg',
        'https://www.fitterfly.com/blog/wp-content/uploads/2021/09/overweight-in-child-1200x720.jpg',
        'https://static1.srcdn.com/wordpress/wp-content/uploads/2021/01/the-machinist-christian-bale-weight-loss.jpg'
    ]
    
    # Prediction button
    if st.button('Predict'):
        if model_choice == 'Logistic Regression':
            prediction = lr_model.predict(user_input)
        elif model_choice == 'SVM':
            prediction = svm_model.predict(user_input)
        
        labels = ['Normal weight', 'Obese', 'Overweight', 'Underweight']
        
        st.subheader(f'{model_choice} Prediction:')
        st.write(labels[prediction[0]])
        st.image(img_urls[prediction[0]])

if __name__ == '__main__':
    app()
