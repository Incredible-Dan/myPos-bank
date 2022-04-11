class Account:
    def __init__(self,name, balance = 0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f'{self.name} your account balance is {self.balance}'

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print('Deposit is successful!')
            print(f'Your balance is {self.balance}')
        else:
            print('You cannot deposit negative amount !')


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print('Withdrawal successful!')
            print(f'Your balance is {self.balance}')
        else:
            print('Insufficient fund, please fund your account!')


# customer1 = Account('Daniel', '500')
# print(customer1)

print(' Welcome to MyPOS BANK:')
user  = input('Enter your name: \n')
new_account = Account(user)


while True:
    print(''' Operational Guide:
    =========
    Enter d to deposit:
    Enter W to withdraw:
    Enter B to check your balance ''')
    # amount = int(input('Enter Amount to deposit: '))
    # new_account.deposit(amount)
    # amount = int(input('Enter Amount to withdraw: '))
    # new_account.withdraw(amount)
    print(new_account)

    choice = input('Choose operation to perform: \n')
    if choice.lower() == 'd':
        amount = int(input('Enter Amount to deposit: '))
        new_account.deposit(amount)
    elif choice.lower() == 'w':
        amount = int(input('Enter Amount to withdraw: \n'))
        new_account.withdraw(amount)

    elif choice.lower() == 'b':
        print(f'Your balance is {new_account.balance}')

    else:
        print('Incorrect selection please try again')

    check = input('Do you want to perform another transaction ? Y/N')
    if check.lower() == 'y':
        continue
    else:
        print('Thank you for banking with us, have a nice day!')
        break
