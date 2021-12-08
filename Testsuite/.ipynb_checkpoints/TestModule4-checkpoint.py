#test room module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\Hotel")
from Service.room import Room
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.p1 = Room(150,100)
        self.p2 = Room(250,80)
    def test_modifyprice(self):
        self.p1.modifyprice(200)
        self.p2.modifyprice(100)
        self.assertEqual(self.p1.price,200)
        self.assertEqual(self.p2.price,100)
    def test_discountprice(self):
        self.p1.discountprice(0.8)
        self.p2.discountprice(0.9)
        self.assertEqual(self.p1.price,120)
        self.assertEqual(self.p2.price,225)
    def test_reduceroomnumber(self):
        self.p1.reduceroomnumber(3)
        self.p2.reduceroomnumber(7)
        self.assertEqual(self.p1.availablenumber,97)
        self.assertEqual(self.p2.availablenumber,73)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Price:150 Availablenumber:100')
        self.assertEqual(self.p2.display(),'Price:250 Availablenumber:80')