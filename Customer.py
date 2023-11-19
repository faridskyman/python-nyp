class Customer:
    def __init__(self, name, email, mobile, nric):
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile
        self.nric = nric

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def __str__(self):
        s = 'Name: {}, Email: {}, Mob:{}, Nric: {}'.format(self.__name, self.__email, self.__mobile_number, self.nric)
        return s

