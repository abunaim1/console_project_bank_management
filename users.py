class Users:
    def __init__(self, name, email, account_type) -> None:
            self.name = name
            self.email = email
            self.account_type = account_type
            self.balance = 0
            self.loan_time = 0
            self.transictions = {}
    
    def deposite(self, amount, date):
        self.balance += amount
        self.transictions[date] = ['Deposite', amount]
        print(f'Balance after deposite: {self.balance}')
    
    def withdraw(self, amount, date):
        if self.balance >= amount:
            self.balance -= amount
            self.transictions[date] = ['Withdraw', amount]
            print(f'Available balance after withdrawal: {self.balance}')
        else:
            print('Withdrawal amount exceeded')
    
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