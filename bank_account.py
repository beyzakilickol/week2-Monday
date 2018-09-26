class Bank_account:
    def __init__(self, first_name, last_name, middle_name, accounty_type,status):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.accounty_type = accounty_type
        self.balance = 100
        self.status = status


    def deposit(self):
        deposited_amount = int(input('Enter deposited_amount: '))
        self.balance += deposited_amount
        print('Remaining balance = {0}'.format(self.balance))

    def withdraw(self):
        withdrawn_amount =int(input('Enter withdrawn_amount: '))
        self.balance -= withdrawn_amount
        print('Remaining balance = {0}'.format(self.balance))

    def transfer(self, from_account, to_account):
        from_account = input('Which account you want to transfer from?: ')
        to_account = input('Which account you want to transfer to?: ')
        transfer_amount = int(input('Enter the amount to transfer: '))
        self.balance -= transfer_amount
        print('Amount transfered: {0}'.format(transfer_amount))
        print('Remaining balance = {0}'.format(self.balance))
        print('Transfer from {0} to {1} is succesfully processed'.format(from_account, to_account))

    def overdraft(self):
        if self.balance < 0:
            self.balance -= 35
            print('Remaining balance = {0}, overdarft charge is applied'.format(self.balance))

    def account_status_closed(self):
        print('closed')
    def account_status_opened(self):
        print('opened')
    def account_status_freeze(self):
        print('freeze')
    def profile(self):
        print(self.first_name)
        print(self.last_name)
        if self.middle_name != '':
            print(self.middle_name)

        print(self.accounty_type)
        print(self.account_status_opened())



name =input('Enter you name: ')
last_name = input('Enter last name: ')
middle_name = input('Enter middle name: ')
accounty_type = input('Enter the account type (saving or checking): ')

account = Bank_account(name, last_name, middle_name, accounty_type, [] )

account.profile()
account.transfer('Beyza checking account', 'Emre checking account')
account.deposit()
account.withdraw()
account.overdraft()
