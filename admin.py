from users import*
class Admin:
    def __init__(self, name, password) -> None:
        self.name = name
        self.__password = password
        self.users = []
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value

    def create_account(self):
        print('Savings or Current')
        print('Account Type: ')
        acc_type = input()
        acc_type.lower()
        if acc_type == 'savings' or acc_type == 'current':
            print('Enter name: ')
            name = input()
            print('Enter you email: ')
            email = input()
            account_number = f'{name.lower()}-{email.lower()}'
            match = False
            for user in self.users:
                if user.account_number == account_number:
                    print('This account already exist.')
                    match = True
            if match == False:
                user = Users(name, email, acc_type, account_number)
                self.users.append(user)
                print(f'Account created successfully your account number is: {account_number}')
        else:
            print('Not available this type')
    
    def check_user(self):
        if len(self.users) > 0:
            for user in self.users:
                print(f'{user.name} with account number {user.account_number}')
        else:
            print('No users found')

    def delete_account(self, account_number):
        match = False
        if len(self.users) > 0:
            for user in self.users:
                if account_number == user.account_number:
                    user.remove()
                    print(f'Removed {account_number} this account')
                    match = True
        if match == False:
            print('Not available')

    def check_bank_balance(self):
        pass

    def check_loan_amount(self):
        pass

