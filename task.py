class Account():
    def __init__(self):
        self.name = ""
        self.bank_balance = 0

    def get_name(self):
        self.name = input()
    def get_start_bank_balance():
        self.bank_balance = input()

    def reaction(self,act):
        act.how_many()
        pass

class Input():
    def __init__(self):
        self.sum = 0
    def how_many(self):
        self.sum = input()
    def action(self):


class Withdrawal():
    def __init__(self):
        self.sum = 0
    def how_many(self):
        self.sum = input()

class Two_accounts_transfer():
    def __init__(self):
        self.sum = 0
    def how_many(self):
        self.sum = 0
    def transfer(self,user_plus,user_minus):
        user_plus.bank_balance += self.sum
        user_minus.bank_balance -= self.sum


user1 = Account()
    user1.get_name()
    user1.get_start_bank_balance()

user2 = Account()
    user2.get_name()
    user2.get_start_bank_balance()

while True:
    
