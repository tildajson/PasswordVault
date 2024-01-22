# PasswordVault

This project consists of a powerful collection of tools intended to assist users with enhancing their online safety and privacy. Easy to use and navigate so anyone can benefit from the tools provided, despite previous technical experience.

1. Password Strength Analyzer
This tool can evaluate the strength of your passwords with machine learning, using a XGBClassifier model. Use it to identify weak passwords to help enhance your password security with guidelines and recommendations.

2. Pwned Password Checker
This tool uses the Have I Been Pwned API to check if your passwords have been part of any data breaches. Protect sensitive information by ensuring your passwords are not compromised.

3. Password Generator
This tool generates strong and unique passwords with customizable length. Enhance your safety and secure your online accounts with robust passwords. Optimal for quickly and effortlessly replacing weak passwords.

4. IP Lookup
This tool can help you identify potential threats and suspicious activities by providing information about a given IP address. Find geographic location, owner and other details of IP addresses.

Two factor authentication and password manager in progress.

## Tech Stack

+ Python
+ Streamlit
+ Jupyter

## Screenshots

[Live demo](https://passwordvault.streamlit.app/)

![passwordvaultscreenshot](https://github.com/tildajson/PasswordVault/assets/130234732/149264f3-3818-4899-8016-a88e8ba56ff0)


## Installation

Clone this repository.

#### Install dependencies:

```bash

pip install -r requirements.txt

```

#### To start server:

```bash

python -m streamlit run Password_Vault.py

```

#### To visit app:

```bash

http://192.168.1.184:8501

```
