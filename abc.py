# arr = ['abc', 's2x', 'xyz', 'klm', 'abc']
# a = list(set(arr))
# a.sort()
# print(a)
# arr = (1, 3, 4, 10, 30, 40)
# a=[]
# for i in arr:
#     if i not in a:
#      a.append(i)
# print(a)
#binary search
# target = 10  # Change this to the value you want to search for
#
# low = 0
# high = len(arr) - 1
# found = False
#
# while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         found = True
#         print(f"{target} found at index {mid}")
#         break
#     elif arr[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
#
# if not found:
#     print(f"{target} not found in the array")
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
    selected_option = st.sidebar.radio("Select an option", ["View Items", "Add Item", "Purchase Item", "Search Item", "View Cart", "Remove From Cart", "Edit Item"])

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
