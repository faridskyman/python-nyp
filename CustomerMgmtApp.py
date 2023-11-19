from Customer import *
import shelve
import os

#c1 = Customer("jon", "j@e.co", "23123", "s456")
#c2 = Customer("jane", "jane@e.co", "78978", "s123")

custDict = {}

def OpenDB():
    #access global var
    global custDict
    db = shelve.open('storage.db','c')
    try:
        if 'Customers' in db:
            custDict = db['Customers']
        else:
            db['Customers'] = custDict
    except:
        print("error occured")
    db.close()

def SaveToDB():
    #access global var
    global custDict
    db = shelve.open('storage.db','c')
    try:
        db['Customers'] = custDict
    except:
        print("error occured")
    db.close()    


def Menu():
    print('A. Add New Customer')
    print('B. View All  Customers')
    print('Q. Exit')
    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        clear_screen()
        AddCustomer()
    elif choice == 'b':
        clear_screen()
        ViewAllCustomers()
    elif choice == 'q':
        clear_screen()
        print('Bye...')
    else:
        clear_screen()
        print('Pls enter A, B or Q only, try again')
        Menu()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ViewAllCustomers():
    global custDict
    if len(custDict) > 0:
        for cust in custDict:
            print(custDict[cust])
    else:
        print("No data")
    Menu()
    

def AddCustomer():
    global custDict
    name = input("Enter  customer name: ")
    email = input("Enter in customer email: ")
    mobile = input("Enter in customer mobile: ")
    nric = input("Enter in customer nric: ")
    newCust = Customer(name, email, mobile, nric)
    custDict[newCust.get_name] = newCust
    SaveToDB()
    clear_screen()
    print("Customer Record saved.")
    Menu()



#******************program start*********
clear_screen()
OpenDB()
Menu()

#custDict[c1.get_name()] = c1
#custDict[c2.get_name()] = c2

#db["Customers"] = custDict



