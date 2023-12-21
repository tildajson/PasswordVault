import streamlit as st
import hashlib
import requests

st.set_page_config(page_title="Pwned Password Checker")

st.markdown("# Pwned Password Checker")
st.sidebar.header("Pwned Password Checker")
st.write("### Enter a password to determine if it has been compromised")

API_URL = "https://api.pwnedpasswords.com/range/"


def request_api_data(query_char):
    url = API_URL + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f"ERROR FETCHING: {res.status_code}, CHECK API AND TRY AGAIN")
    return res


def get_compromised_count(hashes, tail_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == tail_hash:
            return count
    return 0


def check_password_api(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    hash_prefix, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(hash_prefix)
    return get_compromised_count(response, tail)


password = st.text_input("Enter Password", type="password")
if st.button("Check"):
    compromised_count = check_password_api(password)
    if compromised_count:
        st.error(
            f"**Your password has been compromised {compromised_count} times.**")
    else:
        st.success("**Your password was not found in the compromised list.**")
