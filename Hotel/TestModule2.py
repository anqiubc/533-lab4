#test customer module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from Person.customers import Customers
class TestCustomers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup Customers class')
    @classmethod
    def tearDownClass(cls):
        print('Teardown Customers class')
    def setUp(self):
        self.p1 = Customers('Betty',19,4,220)
        self.p2 = Customers('Grace',25,8,480)
        self.p3 = Customers('Can',26,7,800)
        self.p4 = Customers('Evelyn',23,4,200)
    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.p4
    def test_add_bill(self):
        self.p1.addbill(140)
        self.p2.addbill(20)
        self.assertEqual(self.p1.bill,360)
        self.assertEqual(self.p2.bill,500)
        self.assertEqual(self.p3.bill,800)
        self.assertEqual(self.p4.bill,200)
        self.assertNotEqual(self.p2.bill,None)
    def test_reduce_bill(self):
        self.p1.reducebill(40)
        self.p2.reducebill(20)
        self.p3.reducebill(50)
        self.assertEqual(self.p1.bill,180)
        self.assertEqual(self.p2.bill,460)
        self.assertEqual(self.p3.bill,750)
        self.assertNotEqual(self.p2.bill,None)
        self.assertIsInstance(self.p2,Customers)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Name:Betty Age:19 Duration:4 bill:220')
        self.assertEqual(self.p2.display(),'Name:Grace Age:25 Duration:8 bill:480')
        self.assertEqual(self.p3.display(),'Name:Can Age:26 Duration:7 bill:800')
        self.assertEqual(self.p4.display(),'Name:Evelyn Age:23 Duration:4 bill:200')
        self.assertNotEqual(self.p2.display(),'Name:Grace, Age:25 Duration:8 bill:480')#wrong format

