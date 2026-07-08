import streamlit as st

st.title("Enter media", anchor=False)
st.divider()
st.image("image/105285.jpg")  #from directory
st.divider()
image = st.file_uploader("Enter Your Image", type=['jpg', 'jpeg', 'png'], #user input image
                         accept_multiple_files=True) # if you want to insert multiple file
print(type(image))
if image: st.image(image)

if image:
    col = st.columns(len(image))
    # print("col", type(col))
    for i, img in enumerate(image):
        with col[i]:
            st.image(img)


 