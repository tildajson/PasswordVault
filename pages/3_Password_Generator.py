import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator")

st.markdown("# Password Generator")
st.sidebar.header("Password Generator")
st.write("### Generate a secure password. Use the slider to edit password length.")


def generate_password(length):
    characters = list(string.ascii_letters +
                      string.digits + string.punctuation)

    random.shuffle(characters)
    password = []

    for _ in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)

    return ("".join(password))


password_length = st.slider("Enter the length of password.", 10, 64)
st.write("Password Length: ", str(password_length))


if st.button("Generate"):
    custom_password = generate_password(password_length)
    with st.container(border=True):
        st.text(custom_password)
