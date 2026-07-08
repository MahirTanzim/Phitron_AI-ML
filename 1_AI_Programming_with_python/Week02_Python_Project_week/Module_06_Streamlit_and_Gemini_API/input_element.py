import streamlit as st

st.title("Input your information", anchor=False)
st.divider()

name = st.text_input("Enter your name:", placeholder='Type your name')
# st.write("Your Name is: ", name)
# print(type(name))
st.divider()
age = st.number_input("Enter your age: ", placeholder='Type your age', value=None)
# st.write("Your age is: ", age)
# print(type(age))
st.divider()
# password = st.text_input("Enter your passward: ", placeholder='Type your password', type="password")
# # st.write("Your Passward is: ", password)
# print(type(password))

select = st.selectbox("Choose your Profession", 
                      ('Student', 'Teacher', 'Doctor', 'Engineer'), 
                      index=None,
                      accept_new_options=True)
print(type(select))

st.write(f"You seleceted {select}")

st.divider()
pressed = st.button("Enter to Confirm", type="primary")

if pressed:
    st.write(f"Your Name is {name} and your age is {age}")

