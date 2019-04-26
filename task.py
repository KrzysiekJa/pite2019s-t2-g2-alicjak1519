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
        client_minus_name = input("Where to transfer money from?")
        client_minus = name_in_account(client_minus_name, client_list)
        client_minus.bank_balance -= self.sum
        client.bank_balance += self.sum

class Two_accounts_transfer_minus():
    def how_many(self, sum):
        self.sum = sum
    def action(self,client):
        client_plus_name = input("Where to transfer money to?")
        client_plus = name_in_account(client_plus_name, client_list)
        client_plus.bank_balance += self.sum
        client.bank_balance -= self.sum

def name_in_account(actual_name, client_list):
    for client in client_list:
        if client.name == actual_name:
            actual_client = client
    return actual_client

def main():

        dic = {
            "in":Input(),
            "out":Withdrawal(),
            "t+":Two_accounts_transfer_plus(),
            "t-":Two_accounts_transfer_minus()
            }


        print("Operations: ")
        print("1 - create an account")
        print("2 - display a list of clients")
        print("3 - log in with your account number")

    client_list = []

    while True:
        operation = int(input("Choose an operation: "))

        if operation == 1:

            client_list.append(Account(
                input("Your name: "),
                int(input("Initial bank balance: "))))

        elif operation == 2:
            for client in client_list:
                print(client.name)

        elif operation == 3:
            actual_client_name = input("Your name: ")
            actual_client = name_in_account(actual_client_name, client_list)
            print("{}, what do you want to do?\n".format(actual_client.name))
            print("in,out,t+,t-")
            action = input()
            actual_client.reaction(dic[action],int(input("How much money?\n")))
            print("Actual bank balance: ")
            print(actual_client.bank_balance)
        else:
            pass

if __name__ == '__main__':
    main()
