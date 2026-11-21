
# Text Encryption & Decryption Tool

A Python-based web application that allows users to encrypt and decrypt text securely using password-based encryption.

## Features

- Encrypt text using Fernet encryption.
- Decrypt previously encrypted text.
- Password-based key derivation using PBKDF2-HMAC-SHA256.
- Password generator with customizable length.
- Password strength indicator.
- Copy and download generated passwords.
- Download encrypted text.
- Clear input fields easily.
- Security tips and usage instructions.

## Technologies Used

- Python
- Streamlit
- Cryptography Library
- Fernet Encryption
- PBKDF2-HMAC-SHA256

## Installation

1. Clone this repository:

   git clone https://github.com/ayeshayaseendigital-max/Text-Encryption-Tool.git

2. Open the project folder.

3. Install the required libraries:

   pip install -r requirements.txt

4. Run the application:

   python -m streamlit run app.py

## Security Information

- Keep your encryption password private.
- Share the encryption password separately from the encrypted text.
- Anyone with both the encrypted text and correct password can decrypt the message.
- Do not use this beginner project as a substitute for professionally audited security software.

## Project Purpose

This project was developed to practice Python programming, cryptography, password security, and building interactive web applications using Streamlit.
