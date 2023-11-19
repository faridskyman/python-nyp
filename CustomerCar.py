from Customer import *

class CustomerCar(Customer):
    def __init__(self, name, email, mobile, nric, license):
        #super().__init__(name, email, mobile, nric) 
        #Customer.__init__(self, name, email, mobile, nric) 
        super().__init__(name, email, mobile, nric) 
        self.__license = license

    def getLicense(self):
        print(self.__license)

    #def get_name(self):
     #   return "Name of Car cust:" + super().get_name()