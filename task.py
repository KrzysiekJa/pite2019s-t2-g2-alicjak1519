class Account():
    def __init__(self,name,bank_balance):
        self.name = name
        self.bank_balance = bank_balance

    def reaction(self,transaction,amount):
        transaction.how_many(amount)
        transaction.action(self)

class Input():
    def how_many(self,sum):
        self.sum = sum
    def action(self,client):
        client.bank_balance += self.sum

class Withdrawal():
    def how_many(self, sum):
        self.sum = sum
    def action(self,client):
        client.bank_balance -= self.sum

class Two_accounts_transfer_plus():
    def how_many(self, sum):
        self.sum = sum
    def action(self,client):
        client_minus_name = input("Od kogo pobrac kase? ")
        client_minus = name_in_account(client_minus_name, client_list)
        client_minus.bank_balance -= self.sum
        client.bank_balance += self.sum

class Two_accounts_transfer_minus():
    def how_many(self, sum):
        self.sum = sum
    def action(self,client):
        client_plus_name = input("Komu wplacic kase? ")
        client_plus = name_in_account(client_plus_name, client_list)
        client_plus.bank_balance += self.sum
        client.bank_balance -= self.sum

def name_in_account(actual_name, client_list):
    for client in client_list:
        if client.name == actual_name:
            actual_client = client
    return actual_client

dic = {
    "in":Input(),
    "out":Withdrawal(),
    "t+":Two_accounts_transfer_plus(),
    "t-":Two_accounts_transfer_minus()
}


print("Mozliwe operacje: ")
print("1 - zaloz konto")
print("2 - wyswietl liste nazw klientow")
print("3 - zaloguj sie swoim numerem")

client_list = []

while True:
    operation = int(input("Podaj operacje: "))

    if operation == 1:

        client_list.append(Account(
            input("Podaj swoje imie: "),
            int(input("Podaj poczatkowy stan konta: "))))

    elif operation == 2:
        for client in client_list:
            print(client.name)

    elif operation == 3:
        actual_client_name = input("Podaj swoje imie: ")
        actual_client = name_in_account(actual_client_name, client_list)
        print("{}, napisz co chcesz zrobic".format(actual_client.name))
        print("in,out,t+,t-")
        action = input()
        actual_client.reaction(dic[action],int(input("Ile pieniazkow? ")))
        print("Stan konta po wykonaniu: ")
        print(actual_client.bank_balance)
    else:
        pass
