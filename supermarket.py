# -----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
import pickle

# items = []

# with open("supermarketdata", 'wb') as ff:
#     pickle.dump(items, ff)

with open("supermarketdata", "rb") as ff:
    items = pickle.load(ff)


class SuperMarket:
    def __init__(self):
        # pass

        with open("supermarketdata", "rb") as ff:
            self.items = pickle.load(ff)

    def view(self):

        if len(items) != 0:
            print('Here are all the items available in the supermarket.')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)

    def additems(self):
        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                item['price'] = int(input('Price $ : '))
                break
            except ValueError:
                print('Price should only be in digits')
        print('Item has been successfully added.')
        items.append(item)

    def purchase(self):
        purchase_item = input('which item do you want to purchase? Enter name : ')
        for item in items:
            if purchase_item.lower() == item['name'].lower():
                quantity1=int(input("enter the required quantity"))
                if item['quantity'] >=quantity1:
                    print('Pay ', quantity1*item['price'], 'at checkout counter.')
                    item['quantity'] -= quantity1
                    with open("supermarketdata", 'wb') as ff:
                        pickle.dump(items, ff)
                else:
                    print('item out of stock.')

    def search(self):
        find_item = input('Enter the item\'s name to search in inventory : ')
        f = False
        for item in items:
            if item['name'].lower() == find_item.lower():
                f = True
                print('The item named ' + find_item + ' is displayed below with its details')
                print(item)
                break
        if not f:
            print('item not found.')
    def cartitems(self):

        # cart = []

        with open("cartinfo", 'rb') as ff:
            cart = pickle.load(ff)
            print(cart)

        # cart_item = input(" What would you like to add?  ")
        # for item in items:
        #     if cart_item.lower() == item['name'].lower():
        #         cart.append(cart_item)
        #         price = item['price']
        #         cart.append(price)
        #         with open("cartinfo", 'wb') as ff:
        #             pickle.dump(cart,ff)
        #         print(f"'{cart_item}' has been added to your cart.")
        #         print(f' The price is ${price}')
        #         print("This is what is in your shopping cart")
        # for i in range(0,len(cart),2):
        #     print(f'The item present in your cart is {cart[i]}:{cart[i+1]}')
        # print(cart)
        #cart=[]

        cart_item = {}
        cart_item['name'] = input('Item name: ')
        flat=False
        for item in items:
            if cart_item['name'] in [x['name'].lower() for x in cart]:
                x=item['name']
                print(x)
                y=cart_item['0'].get('price')
                print(y)
                w = cart_item.get('quantity')
                print(w)
                required_quantity = int(input('enter the required quantity'))
                if item['quantity'] >= required_quantity+cart_item['quantity']:
                    cart_item['quantity'] = required_quantity
                    cart_item['price'] = item['price']
                    cart.append(cart_item)
                    with open("cartinfo", 'wb') as ff:
                        pickle.dump(cart, ff)
                    print(cart)
                    flat=True
                else:
                    print('we dont have the required quantity')
            elif cart_item['name'].lower() == item['name'].lower():
                if cart_item['name'] in [x['name'].lower() for x in cart]:
                 print("abccccc")
                print("the available quantity of "+item['name']+":"+str(item['quantity']))
                required_quantity = int(input('enter the required quantity'))
                if item['quantity'] >= required_quantity:
                    cart_item['quantity'] = required_quantity
                    cart_item['price'] = item['price']
                    cart.append(cart_item)
                    with open("cartinfo", 'wb') as ff:
                        pickle.dump(cart, ff)
                    print(cart)
                    flat=True
                else:
                    print('we dont have the required quantity')
        if not flat:
            print("The item which you are searching to add is not available")



    def RemoveFromCart(self):
        with open("cartinfo", 'rb') as ff:
            cart = pickle.load(ff)
            print(cart)
        takeout = input(" Type in what you would like to remove?  ")
        z=cart.index(takeout)
        del cart[z:z+2]
        # cart.remove(takeout)
        with open("cartinfo", 'wb') as ff:
            pickle.dump(cart, ff)
        print(cart)


    def edit(self):
        f=False
        item_name = input('Enter the name of the item that you want to edit : ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                f=True
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('Price $ : '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                print(item)
                with open("supermarketdata", 'wb') as ff:
                    pickle.dump(items, ff)
                break
        if not f:
            print('Item not found')

# market=SuperMarket()
# while True:
#     display = input('Press enter to continue.')
#     print('------------------Welcome to the supermarket------------------')
#     print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
#     choice = input('Enter the number of your choice : ')
#
#     if choice == '1':
#         print('------------------View Items------------------')
#         print('The number of items in the inventory are : ', len(items))
#         market.view()
#
#     elif choice == '2':
#         print('------------------Add items------------------')
#         print('To add an item fill in the form')
#         market.additems()
#         with open("supermarketdata", 'wb') as ff:
#             pickle.dump(items, ff)
#
#     elif choice == '3':
#         print('------------------purchase items------------------')
#         market.purchase()
#         print(items)
#
#     elif choice == '4':
#         print('------------------search items------------------')
#         market.search()
#
#     elif choice == '5':
#         print('------------------edit items------------------')
#         market.edit()
#
#     elif choice == '6':
#         print('------------------exited------------------')
#         break
#
#     else:
#         print('You entered an invalid option')

















