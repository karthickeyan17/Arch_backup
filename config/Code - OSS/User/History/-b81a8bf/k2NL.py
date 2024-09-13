import requests
import streamlit as st

# Streamlit app title
st.title("📚 Dictionary App")

# Header for the input section
st.header("Look Up a Word")

# Input for the word with a placeholder
word = st.text_input("Enter a word:", "follow")

# Add a button to trigger the API call
if st.button("Search"):
    # Fetch the data from the dictionary API
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]['meanings']
        
        # Display the word and its phonetics
        st.subheader(f"Word: {word.capitalize()}")
        phonetics = data[0].get('phonetics', [])
        if phonetics:
            for phonetic in phonetics:
                audio = phonetic.get('audio')
                if audio:
                    st.audio(audio, format="audio/mp3")
        
        # Display meanings in a better layout
        st.markdown("### Meanings")
        for meaning in meanings:
            part_of_speech = meaning['partOfSpeech']
            definition = meaning['definitions'][0]['definition']
            example = meaning['definitions'][0].get('example', 'No example available.')
            
            # Use columns for better layout
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"**{part_of_speech.capitalize()}**")
            with col2:
                st.markdown(f"{definition}")
                st.markdown(f"_Example: {example}_")
            
            st.markdown("---")
    else:
        st.error("Word not found or API request failed.")

# Add some spacing at the bottom
st.write("\n" * 5)
