from admin import*
from users import*
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
            take = input()
            if take == '1':
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
            if take == '2':
                print('Enter account number: ')
                account_number = input()
                match = False
                for user in admin.users:
                    if user.account_number == account_number:
                        match = True
                        print('Got it')
                if match == False:
                    print('Account number does not exist! Create account with admin.')
    

        
    else:
        print('Not exist!')
        


if __name__ == '__main__':
    main()