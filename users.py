from datetime import date
from admin import*
class Users:
    def __init__(self, name, email, account_type, account_number) -> None:
            self.name = name
            self.email = email
            self.account_type = account_type
            self.account_number = account_number
            self.balance = 0
            self.loan_time = 0
            self.transictions = []

    def deposite(self, deposite_amount, date, admin):
        self.balance += deposite_amount
        admin.balance += deposite_amount
        self.transictions.append(f'Deposite - {deposite_amount} - {date}')
        print(f'Balance after deposite: {self.balance}')
    
    def withdraw(self, withdrawal_amount, date, admin):
        if self.balance >= withdrawal_amount:
            admin.balance -= withdrawal_amount
            self.balance -= withdrawal_amount
            self.transictions.append(f'Withdraw - {withdrawal_amount} - {date}')
            print(f'Available balance after withdrawal: {self.balance}')
        else:
            print(f'Withdrawal balance exceeded')
    
    def check_balance(self):
        print(f'Your available balance: {self.balance}')

    def transiction_history(self):
        if len(self.transictions) > 0:
            for transiction in self.transictions:
                print(transiction)
        else:
            print('Not a single transiction yet!')
    
    def take_loan(self,amount, admin):
        #if he has account in this bank he can take two loan from this bank.
        if admin.balance > amount:
            admin.balance -= amount
            self.balance += amount
            print('The loan is added to your balance.')
        else:
            print('The bank is bankrupt.')

    def transfer_money(self, amount, user):
        #TODO have to transfer money from one account to another account. 
        pass