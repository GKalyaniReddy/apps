import streamlit as st
import pickle

# Load data from the pickle file
def load_data(filename):
    try:
        with open(filename, "rb") as ff:
            credentials = pickle.load(ff)
    except FileNotFoundError:
        credentials={}
    return credentials

# Save data to the pickle file
def save_data(filename, data):
    with open(filename, 'wb') as ff:
        pickle.dump(data, ff)

# Create a Streamlit app
def main():
    st.title("Supermarket App")

    st.sidebar.header("Login")
    user_type = st.sidebar.radio("Select user type", ["Admin", "Customer"])


    credentials = {
        "GK": "123",  # Replace with actual admin credentials
        "moon": "456"  # Replace with actual customer credentials
    }
    save_data("admincredentials", credentials)

    credentials=load_data("admincredentials")
    st.write(credentials)


    if user_type.lower() == "admin":
        st.sidebar.header("Admin Login")
        user_id = st.sidebar.text_input("Admin User ID")
        password = st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Admin login successful.")

            else:
                st.error("Admin login failed. Please check your credentials.")

    elif user_type.lower() == "customer":
        st.sidebar.header("Customer Login")
        user_id = st.sidebar.text_input("Customer User ID")
        password = st.sidebar.text_input("Customer Password", type="password")
        if st.sidebar.button("Customer Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Customer login successful.")

            else:
                st.error("Customer login failed. Please check your credentials.")


