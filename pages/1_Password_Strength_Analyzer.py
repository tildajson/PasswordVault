import streamlit as st
import pickle


st.set_page_config(page_title="Password Strength Analyzer")

st.markdown("# Password Analyzer")
st.sidebar.header("Password Analyzer")

with st.container(border=True):
    st.write("""#### NIST Password Guidelines:
            \nPasswords should be at least 8 characters in length.
            \nAvoid repetitive or incremental characters.
            \nAvoid dictionary words.
            \nAvoid using context-specific and personal words.
            \nUse a unique password for each account.
            \nDo not store passwords online.
            \nHash and salt your passwords.
            \nEnable multi-factor authentication.
            \nDo not use passwords that have been compromised in data breaches.""")

st.write("### Enter a password to evaluate its strength")
with open("Models/xgboost_model.pkl", 'rb') as xg_file:
    # load the winner genome to the genome variable
    xg_model = pickle.load(xg_file)

password = st.text_input("Enter Password", type="password")

if st.button("Analyze"):
    strength = xg_model.predict([password])
    if strength == 0:
        st.error("**Weak password**")
    elif strength == 1:
        st.warning("**Medium strength password**")
    elif strength == 2:
        st.success("**Strong password**")
