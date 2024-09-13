import requests
import streamlit as st

st.title("📚 Dictionary App")
st.header("Look Up a Word")
words = st.text_input("Enter a word:", "follow")

if st.button("Search"):
    words = words.replace("\n"," ").split()    
    responses =[requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}') for word in words]
    for ind,response in enumerate(responses):
        if response.status_code == 200:
            data = response.json()
            meanings = data[0]['meanings']
            
            st.subheader(f"Word: {word[ind].capitalize()}")
            phonetics = data[0].get('phonetics', [])
            if phonetics:
                for phonetic in phonetics:
                    audio = phonetic.get('audio')
                    if audio:
                        st.audio(audio, format="audio/mp3")
            
            st.markdown("### Meanings")
            for meaning in meanings:
                part_of_speech = meaning['partOfSpeech']
                definition = meaning['definitions'][0]['definition']
                example = meaning['definitions'][0].get('example', 'No example available.')
                
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.markdown(f"**{part_of_speech.capitalize()}**")
                with col2:
                    st.markdown(f"{definition}")
                    st.markdown(f"_Example: {example}_")
                
                st.markdown("---")
        else:
            st.error("Sorry,reponse not found for %s"%word[ind])
