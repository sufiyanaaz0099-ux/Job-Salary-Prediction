import streamlit as st

st.set_page_config(page_title="Salary App", layout="centered")

# 1. Initialize "Database" in memory so signups work during this session
if "user_db" not in st.session_state:
    st.session_state.user_db = {"admin": "1234"} # Default user

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- LOGOUT LOGIC ---
def logout():
    st.session_state.authenticated = False
    st.rerun()

# --- AUTHENTICATION UI ---
if not st.session_state.authenticated:
    st.title("AAC Salary Predictor")
    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        u_login = st.text_input("Username", key="l_user")
        p_login = st.text_input("Password", type="password", key="l_pass")
        if st.button("Login"):
            if u_login in st.session_state.user_db and st.session_state.user_db[u_login] == p_login:
                st.session_state.authenticated = True
                st.rerun() # This handles the "Automatic Redirect"
            else:
                st.error("Invalid Username or Password")

    with tab2:
        u_signup = st.text_input("Create Username", key="s_user")
        p_signup = st.text_input("Create Password", type="password", key="s_pass")
        if st.button("Signup"):
            if u_signup:
                st.session_state.user_db[u_signup] = p_signup
                st.success("Account created! Now go to the Login tab.")
            else:
                st.warning("Please enter a username")

# --- POST-LOGIN PAGE ---
else:
    st.title("Dashboard")
    st.success(f"Welcome back!")
    
    # The Redirect Link
    st.page_link("pages/Salary_Predictor.py", label="Open Salary Predictor", icon="💰")
    
    # The Logout Button
    if st.button("Log Out"):
        logout()
