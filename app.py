
import streamlit as st
import base64
import os
import hashlib
import secrets
import string
from cryptography.fernet import Fernet, InvalidToken

# Page configuration
st.set_page_config(
    page_title="Text Encryption Tool",
    page_icon="🔐",
    layout="centered"
)

# Custom Professional Theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(
            135deg,
            #171923 0%,
            #202438 55%,
            #171923 100%
        );
        color: #F1F3F9;
    }

    h1, h2, h3 {
        color: #E8EAF6 !important;
    }

    p, label, .stCaption {
        color: #C4C7D4 !important;
    }

    div.stButton > button {
        background-color: #367BF5;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 1rem;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #A78BFA;
        color: white;
        border: none;
    }

    div[data-baseweb="input"],
    div[data-baseweb="textarea"] {
        background-color: #242738;
        border-radius: 10px;
    }

    /* Dark Input Fields */
    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea {
        background-color: #242738 !important;
        color: #F1F3F9 !important;
        border: 1px solid #454858 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] input::placeholder,
    div[data-baseweb="textarea"] textarea::placeholder {
        color: #A1A1AA !important;
    }

    div[data-baseweb="input"]:focus-within,
    div[data-baseweb="textarea"]:focus-within {
        border-color: #A78BFA !important;
    }

    /* Force Dark Text Areas */
    .stTextArea textarea,
    .stTextInput input,
    div[data-baseweb="textarea"] > div {
        background-color: #242738 !important;
        color: #F1F3F9 !important;
        border: 1px solid #454858 !important;
    }

    .stTextArea textarea::placeholder {
        color: #A1A1AA !important;
    }

    .stTextArea textarea:focus,
    .stTextInput input:focus {
        border-color: #A78BFA !important;
    }


/* Generated Password Box */
div[data-testid="stCode"] pre {
    background-color: #242738 !important;
    color: #F1F3F9 !important;
    border: 1px solid #454858 !important;
    border-radius: 10px !important;
}

/* Download Button */
div[data-testid="stDownloadButton"] button {
    background-color: #367BF5 !important;
    color: #FFFFFF !important;
    border: 1px solid #367BF5 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

div[data-testid="stDownloadButton"] button:hover {
    background-color: #A78BFA !important;
    border-color: #A78BFA !important;
    color: #FFFFFF !important;
}

/* Security Warning - Dark Theme */
div[data-testid="stAlert"],
div[data-testid="stAlert"] > div {
    background-color: #242738 !important;
    border: 1px solid #A78BFA !important;
    border-radius: 10px !important;
    color: #F1F3F9 !important;
}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span {
    color: #F1F3F9 !important;
}

/* Slider Accent */
:root {
    --primary-color: #367BF5;
}

div[data-testid="stSlider"] [role="slider"] {
    background-color: #367BF5 !important;
    border-color: #367BF5 !important;
}
    
</style>


""", unsafe_allow_html=True)


st.title("🔐 Text Encryption & Decryption Tool")

st.write(
    "Encrypt and decrypt your text securely using your own password."
)

# Password-based key generation
def generate_key(password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600000,
        dklen=32
    )
    return base64.urlsafe_b64encode(key)
# Secure password generator
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    while True:
        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in "!@#$%^&*" for c in password)):
            return password


# Encryption section
st.header("🔒 Encrypt Your Text")
# Password generator section
st.subheader("Generate a Strong Password")

password_length = st.slider(
    "Choose password length:",
    min_value=12,
    max_value=32,
    value=16
)

if st.button("Generate Strong Password"):
    st.session_state.generated_password = generate_password(
        password_length
    )

if "generated_password" in st.session_state:
    st.code(st.session_state.generated_password)

    st.caption("📋 Copy your generated password using the copy icon above.")

    st.warning(
        "Security Warning: Your password will be saved "
        "in a readable text file. Keep this file private "
        "and store it securely."
    )

    st.download_button(
        label="Download Password",
        data=st.session_state.generated_password,
        file_name="My_Generated_Password.txt",
        mime="text/plain"
    )
    if st.button("Use Generated Password"):
        st.session_state.encrypt_password = st.session_state.generated_password
        st.session_state.confirm_password = st.session_state.generated_password

plain_text = st.text_area(
    "Enter your text:",
    key="plain_text"
)
def clear_text():
    st.session_state["plain_text"] = ""

st.button("Clear Text", on_click=clear_text)



password = st.text_input(
    "Choose your encryption password:",
    type="password",
    key="encrypt_password"
)
confirm_password = st.text_input(
    "Confirm your password:",
    type="password",
    key="confirm_password"
)
# Password strength indicator
# Password strength indicator
if password:
    score = 0

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        st.error("Weak Password")

    elif score <= 3:
        st.warning("Medium Password")

    else:
        st.success("Strong Password")
if st.button("Encrypt Text"):
    if not plain_text or not password or not confirm_password:
        st.warning("Please fill in all fields.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:
        salt = os.urandom(16)
        key = generate_key(password, salt)
        fernet = Fernet(key)

        encrypted = fernet.encrypt(plain_text.encode())

        result = base64.urlsafe_b64encode(
            salt + encrypted
        ).decode()

        st.success("Text encrypted successfully!")
        st.code(result)
        st.caption(
            "Share the encrypted text with the recipient "
            "and provide the password separately."
        )

        st.download_button(
            label="Download Encrypted Text",
            data=result,
            file_name="Encrypted_Text.txt",
            mime="text/plain"
        )

# Decryption section
st.divider()

st.header("🔓 Decrypt Your Text")

encrypted_input = st.text_area(
    "Enter encrypted text:",
    key="encrypted_input"
)
def clear_encrypted_text():
    st.session_state["encrypted_input"] = ""

st.button("Clear Encrypted Text", on_click=clear_encrypted_text)


decrypt_password = st.text_input(
    "Enter your encryption password:",
    type="password",
    key="decrypt_password"
)
if st.button("Decrypt Text"):
    if not encrypted_input or not decrypt_password:
        st.warning("Please enter encrypted text and password.")

    else:
        try:
            decoded = base64.urlsafe_b64decode(
                encrypted_input.encode()
            )

            salt = decoded[:16]
            encrypted_data = decoded[16:]

            key = generate_key(decrypt_password, salt)
            fernet = Fernet(key)

            decrypted = fernet.decrypt(
                encrypted_data
            ).decode()

            st.success("Text decrypted successfully!")
            st.code(decrypted)

        except (InvalidToken, ValueError, UnicodeDecodeError):
            st.error("Incorrect password or invalid encrypted text.")

        except Exception:
            st.error("Something went wrong. Please check your input.")

# Security Instructions
st.divider()

with st.expander("🔐 Security Tips & How to Use"):
    st.subheader("How to Use This Tool")

    st.markdown("""
    1. Enter the text you want to encrypt.
    2. Create a strong encryption password.
    3. Confirm your password and click Encrypt Text.
    4. Copy or download your encrypted text.
    5. To decrypt, enter the encrypted text and the same password.

    **Important Security Tips**

    - Always use a strong and unique password.
    - Never share your password with unauthorized people.
    - Share your password through a separate, secure channel.
    - Keep a private backup of your password.
    - Anyone with both the encrypted text and its password can decrypt it.
    - Never share sensitive information on a device you do not trust.
    """)

