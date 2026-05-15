import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

# Initialize database in memory
if "user_db" not in st.session_state:
    st.session_state.user_db = {"admin": "1234"}

st.title("AAC Salary Predictor")

tab1, tab2 = st.tabs(["Login", "Signup"])

with tab1:
    u_login = st.text_input("Username")
    p_login = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if u_login in st.session_state.user_db and st.session_state.user_db[u_login] == p_login:
            st.success("Redirecting...")
            # THIS IS THE AUTOMATIC REDIRECT
            st.switch_page("pages/Salary_Predictor.py")
        else:
            st.error("Invalid credentials")

with tab2:
    u_signup = st.text_input("Create Username")
    p_signup = st.text_input("Create Password", type="password")
    if st.button("Signup"):
        if u_signup:
            st.session_state.user_db[u_signup] = p_signup
            st.success("Account created! You can now Login.")
