from users import*
class Admin:
    def __init__(self, name, password) -> None:
        self.name = name
        self.__password = password
        self.users = []
        self.balance = 0
        self.loan_amount = 0
    
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
            print('Enter your name: ')
            name = input()
            print('Enter your email: ')
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
                    self.users.remove(user)
                    print(f'Removed {account_number} this account successfully.')
                    match = True
        if match == False:
            print('Not available')

    def check_bank_balance(self):
        if self.balance > 0:
            print(self.balance)
        else:
            print('No amount yet!')

    def check_loan_amount(self):
        if self.loan_amount > 0:
            print(f'You are given {self.loan_amount} tk loan')
        else:
            print('No one given loan with this bank')

