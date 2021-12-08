#test room module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\Hotel")
from Service.room import Room
class TestRoom(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup Room Class')
    @classmethod
    def tearDownClass(cls):
        print('Tear Down Room Class')
    def setUp(self):
        self.p1 = Room(150,100)
        self.p2 = Room(250,80)
        self.p3 = Room(350,100)
        self.p4 = Room(450,80)
    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.p4
    def test_modifyprice(self):
        self.p1.modifyprice(200)
        self.p2.modifyprice(100)
        self.p3.modifyprice(400)
        self.p4.modifyprice(300)
        self.assertEqual(self.p1.price,200)
        self.assertEqual(self.p2.price,100)
        self.assertEqual(self.p3.price,400)
        self.assertEqual(self.p4.price,300)
        self.assertNotEqual(self.p1.price,None)
        self.assertNotEqual(self.p2.price,None)
        self.assertNotEqual(self.p3.price,None)
        self.assertNotEqual(self.p4.price,None)
        self.assertIsInstance(self.p1,Room,msg=None)
        self.assertIsInstance(self.p2,Room,msg=None)
        self.assertIsInstance(self.p3,Room,msg=None)
        self.assertIsInstance(self.p4,Room,msg=None)
    def test_discountprice(self):
        self.p1.discountprice(0.8)
        self.p2.discountprice(0.9)
        self.p3.discountprice(0.95)
        self.p4.discountprice(0.85)
        self.assertEqual(self.p1.price,120)
        self.assertEqual(self.p2.price,225)
        self.assertEqual(self.p3.price,332.5)
        self.assertEqual(self.p4.price,382.5)
        self.assertNotEqual(self.p1.price,None)
        self.assertNotEqual(self.p2.price,None)
        self.assertNotEqual(self.p3.price,None)
        self.assertNotEqual(self.p4.price,None)
        self.assertIsInstance(self.p1,Room,msg=None)
        self.assertIsInstance(self.p2,Room,msg=None)
        self.assertIsInstance(self.p3,Room,msg=None)
        self.assertIsInstance(self.p4,Room,msg=None)
    def test_reduceroomnumber(self):
        self.p1.reduceroomnumber(3)
        self.p2.reduceroomnumber(7)
        self.p3.reduceroomnumber(5)
        self.p4.reduceroomnumber(6)
        self.assertEqual(self.p1.availablenumber,97)
        self.assertEqual(self.p2.availablenumber,73)
        self.assertEqual(self.p3.availablenumber,95)
        self.assertEqual(self.p4.availablenumber,74)
        self.assertNotEqual(self.p1.availablenumber,None)
        self.assertNotEqual(self.p2.availablenumber,None)
        self.assertNotEqual(self.p3.availablenumber,None)
        self.assertNotEqual(self.p4.availablenumber,None)
        self.assertIsInstance(self.p1,Room,msg=None)
        self.assertIsInstance(self.p2,Room,msg=None)
        self.assertIsInstance(self.p3,Room,msg=None)
        self.assertIsInstance(self.p4,Room,msg=None)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Price:150 Availablenumber:100')
        self.assertEqual(self.p2.display(),'Price:250 Availablenumber:80')
        self.assertEqual(self.p3.display(),'Price:350 Availablenumber:100')
        self.assertEqual(self.p4.display(),'Price:450 Availablenumber:80')
        self.assertNotEqual(self.p1.display(),'')
        self.assertNotEqual(self.p2.display(),'')
        self.assertNotEqual(self.p3.display(),'')
        self.assertNotEqual(self.p4.display(),'')
        self.assertIsInstance(self.p1,Room,msg=None)
        self.assertIsInstance(self.p2,Room,msg=None)
        self.assertIsInstance(self.p3,Room,msg=None)
        self.assertIsInstance(self.p4,Room,msg=None)
unittest.main()