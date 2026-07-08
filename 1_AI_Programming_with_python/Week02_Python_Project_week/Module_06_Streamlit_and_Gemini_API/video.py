import streamlit as st
st.title("Enter your video: ", anchor= False)
st.divider()

#from directory
st.video("video/rainy-cyberpunk-streets.1920x1080.mp4")

video = st.file_uploader("Enter Your Video", #user input audio
                         type=['mp4', 'mkv']) # if you want to insert multiple file

button = st.button("Click To Upload")

if button: 
    if video: 
        st.video(video)
        st.success("Your Video was uploaded successfully...!!")
    else:
        st.error("No video Found. Please upload a video.") 