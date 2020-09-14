class Client():
    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance

class Bank():
    def __init__(self, budget, commission):
        self.list_of_clients = []
        self.budget = budget
        self.commission = commission

    def __str__(self):
        client_list_to_print = ""
        for client in self.list_of_clients:
            client_list_to_print+="Name: {} \nBank balance: {} \n\n".format(client.client_name, client.balance)
        return client_list_to_print

    def name_in_account(self, actual_name):
        for client in self.list_of_clients:
            if client.client_name == actual_name:
                actual_client = client
        return actual_client

    def add_client(self, new_client_name, start_bank_balance):
        new_client = Client(new_client_name, start_bank_balance)
        self.list_of_clients.append(new_client)
        return new_client

    def input(self, client, amount):
        self.name_in_account(client).balance+=amount

    def output(self, client, amount):
        if self.name_in_account(client).balance > amount:
            self.name_in_account(client).balance-=amount

    def transfer_inside(self, receiver, sender, amount):
        self.input(receiver, amount)
        self.output(sender, amount)

    def investment(self, client, amount, number_of_month):
        profit = (self.commission/100)*number_of_month*amount
        self.input(client, profit)

    def credit(self, client, amount, number_of_month):
        if self.name_in_account(client).balance > amount/2:
            if amount < self.budget/2:
                loss = (self.commission/50)*number_of_month
                self.output(client, loss)


def transfer_outside(receiver_name, receiver_bank, sender_name, sender_bank, amount):
    for client in receiver_bank.list_of_clients:
        if client.client_name == receiver_name:
            receiver = client

    for client in sender_bank.list_of_clients:
        if client.client_name == sender_name:
            sender = client

    if receiver.balance > amount:
        receiver.balance+=amount
        sender.balance-=amount



def main():

    bank1 = Bank(100000, 2)
    bank2 = Bank(1020302302, 1)
    bank3 = Bank(1302030, 2)

    print("Bank1:")
    print(bank1)


    print("Bank2:")
    print(bank2)


    print("Bank3:")
    print(bank3)


    for i in range(0,4):
        bank1.add_client(input("Name: "), input("Start bank balance: "))
        bank2.add_client(input("Name: "), input("Start bank balance: "))
        bank3.add_client(input("Name: "), input("Start bank balance: "))


if __name__ == '__main__':
    main()