#test swimming_pool module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from Service.swimming_pool import swimming_pool

class TestSwimmingPool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup Swimming Pool Class')
    @classmethod
    def tearDownClass(cls):
        print('Tear Down Swimming Pool Class')
    def setUp(self):
        self.p1 = swimming_pool(8)
        self.p2 = swimming_pool(12)
        self.p3 = swimming_pool(5)
        self.p4 = swimming_pool(10)
    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.p4
    def test_modifyprice(self):
        self.p1.modifyprice(10)
        self.p2.modifyprice(7)
        self.p3.modifyprice(9)
        self.p4.modifyprice(8)
        self.assertEqual(self.p1.price,10)
        self.assertEqual(self.p2.price,7)
        self.assertEqual(self.p3.price,9)
        self.assertEqual(self.p4.price,8)
        self.assertNotEqual(self.p1.price,None)
        self.assertNotEqual(self.p2.price,None)
        self.assertNotEqual(self.p3.price,None)
        self.assertNotEqual(self.p4.price,None)
        self.assertIsInstance(self.p1,swimming_pool,msg=None)
        self.assertIsInstance(self.p2,swimming_pool,msg=None)
        self.assertIsInstance(self.p3,swimming_pool,msg=None)
        self.assertIsInstance(self.p4,swimming_pool,msg=None)
    def test_discountprice(self):
        self.p1.discountprice(0.8)
        self.p2.discountprice(0.9)
        self.p3.discountprice(0.85)
        self.p4.discountprice(0.95)
        self.assertEqual(self.p1.price,6.4)
        self.assertEqual(self.p2.price,10.8)
        self.assertEqual(self.p3.price,4.25)
        self.assertEqual(self.p4.price,9.5)
        self.assertNotEqual(self.p1.price,None)
        self.assertNotEqual(self.p2.price,None)
        self.assertNotEqual(self.p3.price,None)
        self.assertNotEqual(self.p4.price,None)
        self.assertIsInstance(self.p1,swimming_pool,msg=None)
        self.assertIsInstance(self.p2,swimming_pool,msg=None)
        self.assertIsInstance(self.p3,swimming_pool,msg=None)
        self.assertIsInstance(self.p4,swimming_pool,msg=None)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Swimming pool ticket price:8')
        self.assertEqual(self.p2.display(),'Swimming pool ticket price:12')
        self.assertEqual(self.p3.display(),'Swimming pool ticket price:5')
        self.assertEqual(self.p4.display(),'Swimming pool ticket price:10')
        self.assertNotEqual(self.p1.display(),'')
        self.assertNotEqual(self.p2.display(),'')
        self.assertNotEqual(self.p3.display(),'')
        self.assertNotEqual(self.p4.display(),'')
        self.assertIsInstance(self.p1,swimming_pool,msg=None)
        self.assertIsInstance(self.p2,swimming_pool,msg=None)
        self.assertIsInstance(self.p3,swimming_pool,msg=None)
        self.assertIsInstance(self.p4,swimming_pool,msg=None)