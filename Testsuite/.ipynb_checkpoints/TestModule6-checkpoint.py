#test swimming_pool module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\Hotel")
from Service.swimming_pool import swimming_pool

class TestSwimmingPool(unittest.TestCase):
    def setUp(self):
        self.p1 = swimming_pool(8)
        self.p2 = swimming_pool(12)
    def test_modifyprice(self):
        self.p1.modifyprice(10)
        self.p2.modifyprice(7)
        self.assertEqual(self.p1.price,10)
        self.assertEqual(self.p2.price,7)
    def test_discountprice(self):
        self.p1.discountprice(0.8)
        self.p2.discountprice(0.9)
        self.assertEqual(self.p1.price,6.4)
        self.assertEqual(self.p2.price,10.8)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Swimming pool ticket price:8')
        self.assertEqual(self.p2.display(),'Swimming pool ticket price:12')