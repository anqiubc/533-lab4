#test restaurant module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\Hotel")
from Service.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup Restaurant class')
    @classmethod
    def tearDownClass(cls):
        print('Teardown Restaurant class')
    def setUp(self):
        self.p1 = Restaurant({"cake":5},["Annie","Adam"])
        self.p2 = Restaurant({"udon":13},["David","Carl"])
        self.p3 = Restaurant({"rice":6},["Mary","James"])
        self.p4 = Restaurant({"steak":20},["Jennifer"])
    def test_addfood(self):
        self.p1.addfood("roastchicken",10)
        self.p2.addfood("fish",20)
        self.p3.addfood("bubble tea",5)
        self.p4.addfood("ice cream",3)
        self.assertEqual(self.p1.menu,{"cake":5,"roastchicken":10})
        self.assertEqual(self.p2.menu,{"udon":13,"fish":20})
        self.assertEqual(self.p3.menu,{"rice":6,"bubble tea":5})
        self.assertEqual(self.p4.menu,{"steak":20,"ice cream":3})
        self.assertNotEqual(self.p1.menu,{})
        self.assertNotEqual(self.p2.menu,{})
        self.assertNotEqual(self.p3.menu,{})
        self.assertNotEqual(self.p4.menu,{})
        self.assertIsInstance(self.p1,Restaurant,msg=None)
        self.assertIsInstance(self.p2,Restaurant,msg=None)
        self.assertIsInstance(self.p3,Restaurant,msg=None)
        self.assertIsInstance(self.p4,Restaurant,msg=None)
    def test_addemployee(self):
        self.p1.addemployee("Dave")
        self.p2.addemployee("Jack")
        self.p3.addemployee("Thomas")
        self.p4.addemployee("Donald")
        self.assertEqual(self.p1.employee,["Annie","Adam","Dave"])
        self.assertEqual(self.p2.employee,["David","Carl","Jack"])
        self.assertEqual(self.p3.employee,["Mary","James","Thomas"])
        self.assertEqual(self.p4.employee,["Jennifer","Donald"])
        self.assertNotEqual(self.p1.employee,[])
        self.assertNotEqual(self.p2.employee,[])
        self.assertNotEqual(self.p3.employee,[])
        self.assertNotEqual(self.p4.employee,[])
        self.assertIsInstance(self.p1,Restaurant,msg=None)
        self.assertIsInstance(self.p2,Restaurant,msg=None)
        self.assertIsInstance(self.p3,Restaurant,msg=None)
        self.assertIsInstance(self.p4,Restaurant,msg=None)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Menu  Price\ncake      5\n\nEmployee\n   Annie\n    Adam')
        self.assertEqual(self.p2.display(),'Menu  Price\nudon     13\n\nEmployee\n   David\n    Carl')
        self.assertEqual(self.p3.display(),'Menu  Price\nrice      6\n\nEmployee\n    Mary\n   James')
        self.assertEqual(self.p4.display(),' Menu  Price\nsteak     20\n\nEmployee\nJennifer')
        self.assertNotEqual(self.p1.display(),'')
        self.assertNotEqual(self.p2.display(),'')
        self.assertNotEqual(self.p3.display(),'')
        self.assertNotEqual(self.p4.display(),'')
        self.assertIsInstance(self.p1,Restaurant,msg=None)
        self.assertIsInstance(self.p2,Restaurant,msg=None)
        self.assertIsInstance(self.p3,Restaurant,msg=None)
        self.assertIsInstance(self.p4,Restaurant,msg=None)
        