import streamlit as st


def main():
    st.set_page_config(page_title="Password Vault")

    st.header("Welcome to Password Vault! The ultimate Cyber Security Toolkit.")

    st.write("### Password Strength Analyzer")
    st.write("""This tool can evaluate the strength of your passwords using machine learnig.
             Use it to identify weak passwords to help enhance your password security with guidelines and recommendations.""")

    st.write("### Pwned Password Checker")
    st.write("""This tool uses the *Have I Been Pwned* API to check if your passwords have been part of any data breaches.
             Protect sensitive information by ensuring your passwords are not compromised.
             For security reasons it is not recommended to submit your real password.
             Run the tool on a local machine to use it more safely.""")

    st.write("### Password Generator")
    st.write("""This tool generates strong and unique passwords with customizable length.
             Enhance your safety and secure your online accounts with robust passwords.
             Optimal for quickly and effortlessly replacing weak passwords.""")

    st.write("### IP Lookup")
    st.write("""This tool can help you identify potential threats and suspicious activities by providing information about a given IP address.
             Find geographic location, owner and other details of IP addresses.""")

    st.sidebar.success("Select a demo above.")


if __name__ == "__main__":
    main()
