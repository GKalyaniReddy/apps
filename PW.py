import streamlit as st
import pickle
credentials = {'GK': '123'}
with open("admincredentials", 'rb') as ff:
    credentials=pickle.load(ff)
    print(credentials)
def main():
    st.title("Supermarket App")

    st.sidebar.header("Login")
    user_type = st.sidebar.radio("Select user type", ["Admin", "Customer"])
    login_flag = False
    if user_type == "admin":
        st.sidebar.header("Admin Login")
        user_id = st.sidebar.text_input("Admin User ID")
        password = st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Admin login successful.")
                login_flag = True
            else:
                st.error("Admin login failed. Please check your credentials.")

    elif user_type == "customer":
        st.sidebar.header("Customer Login")
        user_id = st.sidebar.text_input("Customer User ID")
        password = st.sidebar.text_input("Customer Password", type="password")
        if st.sidebar.button("Customer Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Customer login successful.")
                login_flag = True
            else:
                st.error("Customer login failed. Please check your credentials.")