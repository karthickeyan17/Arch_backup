import requests
import streamlit as st

# Streamlit app title
st.title("Dictionary App")

# Input for the word
word = st.text_input("Enter a word:", "follow")

# Fetch the data from the dictionary API
response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    meanings = data[0]['meanings']
    st.subheader(f"Meanings of the word: {word}")
    
    for meaning in meanings:
        st.write(f"**Part of Speech:** {meaning['partOfSpeech']}")
        st.write(f"**Definition:** {meaning['definitions'][0]['definition']}")
        st.write("="*50)
else:
    st.error("Word not found or API request failed.")


