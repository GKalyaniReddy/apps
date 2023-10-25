import streamlit as st
import pickle


# Load data from the pickle file
def load_data(filename):
    try:
        with open(filename, "rb") as ff:
            data = pickle.load(ff)
    except FileNotFoundError:
        data = {}
    return data


# Save data to the pickle file
def save_data(filename, data):
    with open(filename, 'wb') as ff:
        pickle.dump(data, ff)


# Create a Streamlit app
def main():
    st.title("Supermarket App")
    show_app = False
    # Load or initialize login credentials
    credentials = load_data("admincredentials")

    st.sidebar.header("Login")
    user_type = st.sidebar.radio("Select user type", ["Admin", "Customer"])


    if user_type == "Admin":
        st.sidebar.header("Admin Login")
        user_id = st.sidebar.text_input("Admin User ID")
        password = st.sidebar.text_input("Admin Password", type="password")

        if st.sidebar.button("Admin Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Admin login successful.")
                st.write(credentials)
                show_app= True
            else:
                st.error("Admin login failed. Please check your credentials.")
                show_app = False
    elif user_type == "Customer":
        st.sidebar.header("Customer Login")
        user_id = st.sidebar.text_input("Customer User ID")
        password = st.sidebar.text_input("Customer Password", type="password")

        if st.sidebar.button("Customer Login"):
            if user_id in credentials and credentials[user_id] == password:
                st.success("Customer login successful.")
                show_app = True
            else:
                st.error("Customer login failed. Please check your credentials.")
                show_app = False
    if show_app:
        # Load or initialize data
        items = load_data("supermarketdata")
        cart = load_data("cartinfo")

        st.sidebar.header("Menu")
        selected_option = st.sidebar.radio("Select an option",
                                           ["View Items", "Add Item", "Purchase Item", "Search Item", "Add to Cart",
                                            "View Cart", "Remove From Cart", "Edit Item"])

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
            item_quantity = st.number_input("Item Quantity", min_value=0)
            item_price = st.number_input("Item Price ($)", min_value=0.0)
            if st.button("Add"):
                item = {"name": item_name, "quantity": item_quantity, "price": item_price}
                items.append(item)
                save_data("supermarketdata", items)
                st.success("Item added successfully!")

        elif selected_option == "Purchase Item":
            st.header("Purchase Item")
            purchase_item = st.text_input("Enter the name of the item you want to purchase")
            quantity1 = st.number_input("Enter the required quantity", min_value=1, max_value=100, step=1)
            if st.button("Purchase"):
                for item in items:
                    if purchase_item.lower() == item['name'].lower():
                        if item['quantity'] >= quantity1:
                            st.write(f"Pay ${quantity1 * item['price']} at the checkout counter.")
                            item['quantity'] -= quantity1
                            save_data("supermarketdata", items)
                        else:
                            st.warning("Item is out of stock.")

        elif selected_option == "Search Item":
            st.header("Search for an Item")
            find_item = st.text_input("Enter the item's name to search in inventory")
            f = False
            for item in items:
                if item['name'].lower() == find_item.lower():
                    f = True
                    st.write("The item named " + find_item + " is displayed below with its details:")
                    st.write(item)
                    break
            if not f:
                st.warning("Item not found.")

        elif selected_option == "Add to Cart":

            st.header("Add Items to Cart")
            item_name = st.text_input("Enter the name of the item you want to add to the cart")
            f = False

            for item in items:
                if item_name.lower() == item['name'].lower():
                    f = True
                    st.write("Details of the item to add to the cart:")
                    st.write(item)
                    quantity_to_add = st.number_input("Enter the quantity to add to the cart", min_value=1,
                                                    max_value=item['quantity'], step=1)

                    if st.button("Add to Cart"):
                        for cart_item in cart:
                            if cart_item["name"].lower() == item['name'].lower():
                                # Update the quantity in the cart
                                total_quantity = cart_item["quantity"] + quantity_to_add
                                if total_quantity <= item['quantity']:
                                    cart_item["quantity"] = total_quantity
                                    st.success(f"{quantity_to_add} {item['name']} added to the cart successfully.")
                                    item['quantity'] -= quantity_to_add
                                    save_data("supermarketdata", items)
                                    save_data("cartinfo", cart)
                                else:
                                    st.warning(
                                        f"Cannot add {quantity_to_add} {item['name']} to the cart. Not enough in stock.")
                                break
                        else:
                            # If the item is not already in the cart, add it as a new entry
                            if quantity_to_add <= item['quantity']:
                                cart_item = {"name": item['name'], "quantity": quantity_to_add, "price": item['price']}
                                cart.append(cart_item)
                                st.success(f"{quantity_to_add} {item['name']} added to the cart successfully.")
                                item['quantity'] -= quantity_to_add
                                save_data("supermarketdata", items)
                                save_data("cartinfo", cart)
                            else:
                                st.warning(f"Cannot add {quantity_to_add} {item['name']} to the cart. Not enough in stock.")
                        break

            if not f:
                st.warning("Item not found.")

        elif selected_option == "View Cart":
            st.header("Shopping Cart")
            if len(cart) != 0:
                st.write("Items in your cart:")
                for item in cart:
                    st.write(item)
            else:
                st.write("Your shopping cart is empty.")

        elif selected_option == "Remove From Cart":
            st.header("Remove Items from Cart")
            if len(cart) != 0:
                items_to_remove = st.multiselect("Select items to remove from the cart", [item["name"] for item in cart])
                if st.button("Remove Selected Items"):
                    cart = [item for item in cart if item["name"] not in items_to_remove]
                    save_data("cartinfo", cart)
                    st.success("Selected items removed from the cart.")
            else:
                st.warning("Your shopping cart is empty.")

        elif selected_option == "Edit Item":
            st.header("Edit Item")
            item_name = st.text_input("Enter the name of the item you want to edit")
            f = False
            for item in items:
                if item_name.lower() == item['name'].lower():
                    f = True
                    st.write("Current details of " + item_name)
                    st.write(item)
                    new_name = st.text_input("New Item Name", value=item['name'])
                    new_quantity = st.number_input("New Item Quantity", value=item['quantity'])
                    new_price = st.number_input("New Item Price ($)", value=item['price'])
                    if st.button("Update"):
                        item['name'] = new_name
                        item['quantity'] = new_quantity
                        item['price'] = new_price
                        save_data("supermarketdata", items)
                        st.success("Item updated successfully.")
                    break
            if not f:
                st.warning("Item not found.")
        # The rest of your application code remains the same as in the previous response.


if __name__ == "__main__":
    main()





