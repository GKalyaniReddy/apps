import streamlit as st
import pickle

# Load data from the pickle file
def load_data(filename):
    try:
        with open(filename, "rb") as ff:
            data = pickle.load(ff)
    except FileNotFoundError:
        data = []
    return data

# Save data to the pickle file
def save_data(filename, data):
    with open(filename, 'wb') as ff:
        pickle.dump(data, ff)

# Create a Streamlit app
def main():
    st.title("Supermarket App")

    # Load or initialize data
    items = load_data("supermarketdata")
    cart = load_data("cartinfo")

    st.sidebar.header("Menu")
    selected_option = st.sidebar.radio("Select an option", ["View Items", "Add Item", "Purchase Item", "Search Item","Add to Cart", "View Cart", "Remove From Cart", "Edit Item"])

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
                cart_item = None
                for cart_item in cart:
                    if cart_item["name"].lower() == item['name'].lower():
                        break

                    if cart_item is not None:
                      cart_item_quantity = cart_item["quantity"]
                      item_quantity = item['quantity']
                      total_quantity = cart_item_quantity + quantity_to_add

                      if total_quantity <= item_quantity:
                        cart_item["quantity"] = total_quantity
                        st.success(f"{quantity_to_add} {item['name']} added to the cart successfully.")
                        item['quantity'] -= quantity_to_add
                        save_data("supermarketdata", items)
                      else:
                        st.warning(f"Cannot add {quantity_to_add} {item['name']} to the cart. Not enough in stock.")
                else:
                        cart_item = {"name": item['name'], "quantity": quantity_to_add, "price": item['price']}
                        cart.append(cart_item)
                        st.success(f"{quantity_to_add} {item['name']} added to the cart successfully.")
                        item['quantity'] -= quantity_to_add
                        save_data("supermarketdata", items)

                        save_data("cartinfo", cart)
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

if __name__ == "__main__":
    main()
