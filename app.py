import streamlit as st

# 1. Setup
st.set_page_config(page_title="Salary App", layout="centered")

# 2. Logic to handle the page switch manually
if "page" not in st.session_state:
    st.session_state.page = "login"

# --- LOGIN PAGE ---
if st.session_state.page == "login":
    st.title("Login / Signup")
    option = st.radio("Choose Option", ["Login", "Signup"])

    if option == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.success("Login Successful!")
                # Switch the internal state
                st.session_state.page = "predictor"
                st.rerun()
            else:
                st.error("Wrong Username or Password")

    else:
        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password", type="password")
        confirm_pass = st.text_input("Confirm Password", type="password")

        if st.button("Signup"):
            if new_pass == confirm_pass:
                st.success("Account Created!")
                st.session_state.page = "predictor"
                st.rerun()
            else:
                st.error("Passwords do not match")

# --- REDIRECT TO PREDICTOR ---
elif st.session_state.page == "predictor":
    st.info("Redirecting you to the Predictor...")
    # This is the "Manual Link" that bypasses the registry bug
    st.page_link("pages/Salary_Predictor.py", label="Click here to open Predictor 💰", icon="🚀")
    
    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()