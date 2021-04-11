import unittest
from src.drink import Drink

class DrinkTest(unittest.TestCase):
    def setUp(self):

       self.drink_1 = Drink("Guinness", 5.00, 4.2) 
       self.drink_2 = Drink("Stella", 4.00, 5.5)
    
    def test_drink_name(self):
        self.assertEqual("Guinness", self.drink_1.name)