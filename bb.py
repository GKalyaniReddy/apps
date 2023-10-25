import streamlit as st
import pickle

# Load data from the pickle file
def load_data(filename):
    try:
        with open(filename, "rb") as file:
            credentials = pickle.load(file)
    except FileNotFoundError:
        credentials = {}
    return credentials

# Save data to the pickle file
def save_data(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Create a Streamlit app
def main():
    st.title("Login Page")

    st.sidebar.header("Login")
    user_type = st.sidebar.radio("Select user type", ["Admin", "Customer"])

    credentials = load_data("admincredentials")

    if user_type == "Admin":
        st.sidebar.header("Admin Login")
        user_id = st.sidebar.text_input("Admin User ID")
        password = st.sidebar.text_input("Admin Password", type="password")

        if st.sidebar.button("Admin Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Admin login successful.")
            else:
                st.error("Admin login failed. Please check your credentials.")
    elif user_type == "Customer":
        st.sidebar.header("Customer Login")
        user_id = st.sidebar.text_input("Customer User ID")
        password = st.sidebar.text_input("Customer Password", type="password")

        if st.sidebar.button("Customer Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Customer login successful.")
            else:
                st.error("Customer login failed. Please check your credentials.")

if __name__ == "__main__":
    main()
