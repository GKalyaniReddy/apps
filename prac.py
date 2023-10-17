# import supermarket

import pickle
import string
import random
from supermarket import SuperMarket
from supermarket import items
# credentials = {'GK': '123'}
with open("admincredentials", 'rb') as ff:
    credentials=pickle.load(ff)
    print(credentials)


def PW():
    Max_len = 12
    Symbols = "@#$%=:?./|~>*()<"
    Combined_List = string.ascii_uppercase + string.digits + string.ascii_lowercase + Symbols

    # randomly select at least one character from each character set above
    rand_upper = random.choice(string.ascii_uppercase)
    rand_lower = random.choice(string.ascii_lowercase)
    rand_symbol = random.choice(Symbols)
    rand_digit = random.choice(string.digits)
    temp_pass = rand_upper + rand_lower + rand_digit + rand_symbol
    for x in range(Max_len - 4):
        temp_pass = temp_pass + random.choice(Combined_List)
    print(temp_pass)
    return ''.join(random.sample(temp_pass, len(temp_pass)))


# credentials={}
print("confirm if you are a admin person or a customer")
Type = input("enter whether you are a admin person or customer:")
login_flag = False
cred_flag = False
if Type.lower() == 'admin':
    a = input("login or signup")
    if a == 'signup':
        User_Id = input("create your User_Id")
        Password = PW()
        print("your user id is: " + User_Id + "  your password is: " + Password)
        credentials[User_Id] = Password
        login_flag = True
    elif a == 'login':
        for _ in range(3):
            User_Id = input("enter your User_Id")
            Password = input("enter your password")
            if User_Id in credentials and credentials[User_Id] == Password:
                cred_flag = True
                break

            else:
                print("please cross check your credentials and retry again")
    while cred_flag or login_flag:
        m = SuperMarket()
        display = input('Press enter to continue.')
        print('------------------Welcome to the supermarket dear ADMIN------------------')
        print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6.change Password\n7. Exit\n8.Add to Cart\n9.Remove from cart')
        choice = input('Enter the number of your choice : ')

        if choice == '1':
            print('------------------View Items------------------')

            print('The number of items in the inventory are : ', len(m.items))
            m.view()

        elif choice == '2':
            print('------------------Add items------------------')
            print('To add an item fill in the form')
            m.additems()
            with open("supermarketdata", 'wb') as ff:
                pickle.dump(m.items, ff)

        elif choice == '3':
            print('------------------purchase items------------------')
            m.purchase()
            print(m.items)

        elif choice == '4':
            print('------------------search items------------------')
            m.search()

        elif choice == '5':
            print('------------------edit items------------------')
            m.edit()
        elif choice=='6':
            print("you are trying to change the password")
            NewPW=input("Please enter the new password")
            credentials[User_Id] = NewPW
            with open("admincredentials", 'wb') as ff:
                pickle.dump(credentials,ff)
        elif choice == '8':
            m.cartitems()
        elif choice == '9':
            m.RemoveFromCart()
        elif choice == '7':
            print('------------------exited------------------')
            break
            # exit(0)
        else:
            print('You entered an invalid option')
elif Type.lower() == 'customer':
    while True:
        print('------------------Welcome to the supermarket dear customers------------------')
        n = SuperMarket()
        print('1. View items\n2. Purchase items\n3. Search items \n4. Exit')
        choice = input('Enter the number of your choice : ')
        if choice == '1':
            print('------------------View Items------------------')
            print('The number of items in the inventory are : ', len(items))
            n.view()
        elif choice == '2':
            print('------------------purchase items------------------')
            n.purchase()
            print(items)

        elif choice == '3':
            print('------------------search items------------------')
            n.search()
        elif choice=='5':
            n.cartitems()
        elif choice == '4':
            print('------------------exited------------------')
            break
        else:
            print('You entered an invalid option')




























