from Customer import *
import shelve

c1 = Customer("jon", "j@e.co", "23123", "s456")
c2 = Customer("jane", "jane@e.co", "78978", "s123")

custDict = {}
db = shelve.open('storage.db','c')

try:
    if 'Customers' in db:
        custDict = db['Customers']
    else:
        db['Customers'] = custDict
except:
    print("error occured")


custDict[c1.get_name()] = c1
custDict[c2.get_name()] = c2

db["Customers"] = custDict
db.close()
