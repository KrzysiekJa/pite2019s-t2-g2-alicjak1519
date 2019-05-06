import unittest
from new_task import Bank, Client



class TestClient(unittest.TestCase):
    def test___init__(self):
        client = Client('Maciek', 5000)
        self.assertEqual(client.client_name, 'Maciek')
        self.assertEqual(client.balance, 5000)
        
        with self.assertRaises(Exception):
            Client(",,,,", 500)
        
        with self.assertRaises(ValueError):
            Client("Jan", -500000)
            
        with self.assertRaises(ValueError):
            Client('010', ---260000)
        
        with self.assertRaises(Exception):
            Client('@@@@@', 1000)
        
        with self.assertRaises(Exception):
            Client(None, 10)
            
        with self.assertRaises(Exception):
            Client(False, 10)



class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank1 = Bank(1000000, 2)
        self.bank2 = Bank(50000000, 1)
        self.bank3 = Bank(200000, -10)
        
        self.bank1.add_client('Maciek', 5000)
        self.bank1.add_client('Alicja', 4000)
        self.bank2.add_client('Jacek', 500)
    
    def tearDown(self):
        pass
    
    
    def test___init__(self):
        self.assertEqual(self.bank1.budget, 1000000)
        self.assertEqual(self.bank1.commission, 2)
        
        self.assertEqual(self.bank2.budget, 50000000)
        self.assertEqual(self.bank2.commission, 1)
        
        with self.assertRaises(Exception):
            Bank('.....', 1)
        
        with self.assertRaises(Exception):
            Bank(-10000, 2)
        
        with self.assertRaises(Exception):
            Bank(210, -57)
            
        with self.assertRaises(Exception):
            Bank(100000, 200)
    
    def test___str__(self):
        result1  = "Name: {} \nBank balance: {} \n\n".format('Maciek', 5000)
        result1 += "Name: {} \nBank balance: {} \n\n".format('Alicja', 4000)
        result2  = "Name: {} \nBank balance: {} \n\n".format('Jacek', 500)
        
        self.assertEqual(print(self.bank1), result1)
        self.assertEqual(print(self.bank2), result2)
    
    def test_name_in_account(self):
        self.assertEqual(self.bank1.name_in_account('Maciek'),'Maciek')
        self.assertEqual(self.bank1.name_in_account('Zbychu'), None)
        self.assertEqual(self.bank1.name_in_account('Alicja'),'Alicja')
        self.assertEqual(self.bank2.name_in_account('Jacek'), 'Jacek')
    
    def test_add_client(self):
        self.assertEqual(self.bank1.add_client('Waldek', 55000),Client('Waldek', 55000))
        self.assertEqual(self.bank2.add_client("Magda", 50050),Client("Magda", 50050))
        
        with self.assertRaises(Exception):
            bank3.add_client('','')
        
        with self.assertRaises(Exception):
            bank3.add_client("", 10)
    
    def test_input(self):
        self.bank1.input('Maciek', 1000)
        self.bank1.input('Alicja', -1000)
        
        self.assertEqual(self.bank1.name_in_account('Maciek').balance, 6000)
        self.assertEqual(self.bank1.name_in_account('Alicja').balance, 3000)
        self.assertEqual(self.bank1.input('Alicja', -1000), None)
        
        with self.assertRaises(Exception):
            self.bank2.input('Jacek', -1000)
        
    def test_output(self):
        self.bank1.output('Maciek', 1000)
        self.bank1.output('Alicja', 5000)      
        self.assertEqual(self.bank1.name_in_account('Maciek').balance, 4000)
        self.assertEqual(self.bank1.name_in_account('Alicja').balance, 4000)
        
        with self.assertRaises(Exception):
            self.bank3('Waldek', 55000)
    
    def test_transfer_inside(self):
        self.bank1.transfer_inside("Maciek", "Alicja", 1000)
        
        self.assertEqual(self.bank1.name_in_account('Maciek').balance, 6000)
        self.assertEqual(self.bank1.name_in_account('Alicja').balance, 3000)
        
        with self.assertRaises(Exception):
            self.bank3.transfer_inside('Waldek','Maja', 1000)
    
    def test_investment(self):
        self.assertEqual(self.bank1.investment("Maciek", 10000, 10), None)
        self.assertEqual(self.bank1.name_in_account('Maciek').balance, 7000)
        
        self.bank3.add_client("Filip", 3000)
        with self.assertRaises(Exception):
            self.bank3.investment("Filip", 10000, 10)
        
        with self.assertRaises(Exception):
            self.bank1.investment("Alicja", 10000, -10)
    
    def test_credit(self):
        self.assertEqual(self.bank1.credit("Maciek", 10000, 10), None)
        self.assertEqual(self.bank1.name_in_account('Maciek').balance, 4999.6)
        
        with self.assertRaises(Exception):
            self.bank1.credit("Alicja", 10000, -10)



if __name__ == '__main__':
    unittest.main()
