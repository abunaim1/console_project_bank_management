from datetime import date
class Users:
    def __init__(self, name, email, account_type, account_number) -> None:
            self.name = name
            self.email = email
            self.account_type = account_type
            self.account_number = account_number
            self.balance = 0
            self.loan_time = 0
            self.transictions = {}
    
    def deposite(self, deposite_amount, date):
        self.balance += deposite_amount
        self.transictions[date] = ['Deposite', deposite_amount]
        print(f'Balance after deposite: {self.balance}')
    
    def withdraw(self, withdrawal_amount, date):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            self.transictions[date] = ['Withdraw', withdrawal_amount]
            print(f'Available balance after withdrawal: {self.balance}')
        else:
            print(f'Withdrawal {withdrawal_amount}, balance exceeded')
    
    def check_balance(self):
        print(f'Your available balance: {self.balance}')

    def transiction_history(self):
        for key, valu in self.transictions.items():
            print(key, valu)
    
    def take_loan(self, amount):
        #TODO: if he has account in this bank he can take two loan from this bank.
        pass

    def transfer_money(self, amount, user):
        #TODO have to transfer money from one account to another account. 
        pass