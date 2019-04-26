class Client():
    def __init__(self, client_name, balance):
        self.client_name = client_name
        self.balance = balance
        self.commission = commission

class Bank():
    def __init__(self, budget, commission):
        self.list_of_clients = []
        self.balance = budget
        self.commission

    def __str__(self):
        client_list_to_print = ""
        for client in self.list_of_clients:
            client_list_to_print+="Name: {} \nBank balance: {} \n\n".format(client.client_name, client.balance)
        return client_list_to_print

    def add_client(self, new_client_name, start_bank_balance):
        new_client = Client(new_client_name, start_bank_balance)
        self.list_of_clients.append(new_client)
        return new_client

    def transaction(self, type, sender, receiver, amount):
        pass

class Transaction():
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def 

def main():

    bank1 = Bank(1000)
    bank1.add_client("Ala", 400)
    bank1.add_client("Lukasz", 3004)
    print(bank1);



if __name__ == '__main__':
    main()
