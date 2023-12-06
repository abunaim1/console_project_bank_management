from admin import*
from users import*
def main():
    print('-----Admin panel-----')
    print('Enter you name: ')
    name = input()
    print('Enter your password: ')
    password = input()
    print('Login successfully')
    admin = Admin(name, password)
    while True:
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


if __name__ == '__main__':
    main()