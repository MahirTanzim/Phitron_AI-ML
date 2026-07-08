import streamlit as st

st.title("input your audio file", anchor=False)
st.divider()
# st.audio_input("Entr Audio")

st.audio("audio/circus_psycho.mp3", loop=True)   #from directorey
st.divider()
audio = st.file_uploader("Enter Your audio", type=['mp3', 'ogg', 'flac'], #user input audio
                         ) # if you want to insert multiple file

if audio: st.audio(audio)