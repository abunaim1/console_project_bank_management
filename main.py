from admin import*
from users import*
from datetime import datetime
def main():
    admin = Admin('admin', 'admin')
    print('-----Admin panel-----')
    print('Enter your name: ')
    name = input()
    print('Enter your password: ')
    password = input()
    if name == 'admin' and password == 'admin':
        print('Login successfully')
        while True:
            print('1. Admin')
            print('2. Users')
            print('3. Exit')
            person = input()
            if person == '1':
                print('1. Create account')
                print('2. Delete account')
                print('3. See all users list')
                print('4. Total available balance') #not done
                print('5. Total loan amount') #not done
                print('6. Exit')
                press= input()
                if press == '1':
                    admin.create_account()
                if press == '2':
                    print('Enter a account number that you want to delete: ')
                    account_number = input()
                    admin.delete_account(account_number)
                if press == '3':
                    admin.check_user()
                if press == '4':
                    admin.check_bank_balance()
                if press == '6':
                    break
            if person == '2':
                print('Enter account number: ')
                account_number = input()
                match = False
                for user in admin.users:
                    if user.account_number == account_number:
                        match = True
                        print('1. Deposite')
                        print('2. Withdraw')
                        print('3. Transiction history')
                        print('4. Balance Transfer')
                        print('5. Take loan')
                        print('6. Check Balance')
                        x = input()
                        if x=='1':
                            print('Enter deposite amount')
                            year = datetime.now().year
                            month = datetime.now().month
                            day = datetime.now().day
                            deposite_amount = int(input())
                            user.deposite(deposite_amount,(year, month, day), admin)
                        if x=='2':
                            print('Enter withdrawal amount')
                            withdrawal_amount = int(input())
                            year = datetime.now().year
                            month = datetime.now().month
                            day = datetime.now().day
                            user.withdraw(withdrawal_amount, (year, month, day), admin)
                        if x=='3':
                            user.transiction_history()
                        if x=='4':
                            print('Enter amount that you want to transfer: ')
                            transfer_amount = int(input())
                            if user.balance >= transfer_amount:
                                user.transfer_money(transfer_amount, admin)
                        if x=='5':
                            print('Enter amount: ')
                            loan_amount = int(input())
                            print('Enter account number: ')
                            account_number = input()
                            user.take_loan(loan_amount, admin, account_number)
                        if x=='6':
                            user.check_balance()
                if match == False:
                    print('Account number does not exist! Create account with admin.')
            else:
                break
    else:
        print('Not exist!')
        
if __name__ == '__main__':
    main()