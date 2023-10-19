import streamlit as st
import pickle

# Load data from the pickle file
def load_data():
    try:
        with open("supermarketdata", "rb") as ff:
            items = pickle.load(ff)
    except FileNotFoundError:
        items = []
    return items

# Save data to the pickle file
def save_data(data):
    with open("supermarketdata", "wb") as ff:
        pickle.dump(data, ff)

# Initialize Streamlit app
def main():
    st.title("Supermarket App")

    items = load_data()

    # Create a sidebar menu
    st.sidebar.header("Menu")
    selected_option = st.sidebar.radio("Select an option", ["View Items", "Add Item"])

    if selected_option == "View Items":
        st.header("Items Available in the Supermarket")
        if len(items) != 0:
            for item in items:
                for key, value in item.items():
                    st.write(f"{key}: {value}")
        else:
            st.write("No items available in the supermarket.")

    elif selected_option == "Add Item":
        st.header("Add Item to the Supermarket")
        item_name = st.text_input("Item Name")
        item_price = st.number_input("Item Price", min_value=0.0)
        if st.button("Add"):
            item = {"Name": item_name, "Price": item_price}
            items.append(item)
            save_data(items)
            st.success("Item added successfully!")

if __name__ == "__main__":
    main()
