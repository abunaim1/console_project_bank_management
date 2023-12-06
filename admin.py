from datetime import date
class Admin:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.__password = password
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value

    def create_account(self):
        #TODO generate acc number
        pass

    def delete_account(self):
        pass

    def check_bank_balance(self):
        pass

    def check_loan_amount(self):
        pass

