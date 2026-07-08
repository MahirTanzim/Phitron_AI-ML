import streamlit as st
st.title(":joy: My Fist streamlit WebApp", anchor=False)
st.header("Chapter 1", divider=True, anchor=False)
st.subheader("Content 1: Subheader", anchor=False)
st.text("Hellow World")
st.markdown(":red[**Hello**] *World*")
st.markdown(":red-background[:orange[**Hello**] *World*]")


a = 12
b = 20

st.write(a, b)
st.write(a+b)
