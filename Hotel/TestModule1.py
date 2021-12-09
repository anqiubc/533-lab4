#test children module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from Person.children import Children
class TestChildren(unittest.TestCase):
    @classmethod
    def setUpClass(Children):
        print("Setup Children Class")
    @classmethod
    def tearDownClass(Children):
        print("Teardown Children Class")
    def setUp(self):
        self.p1 = Children('Alex',8,4,150,2)
        self.p2 = Children('William',5,3,80,0)
        self.p3 = Children('David',9,4,200,1)
        self.p4 = Children('Carol',6,10,170,0)
    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.p4
    def test_add_children_pool_time(self):
        self.p1.add_children_pool_time(2)
        self.p2.add_children_pool_time(3)
        self.p3.add_children_pool_time(1)
        self.p4.add_children_pool_time(0)
        self.assertEqual(self.p1.pooltime,4)
        self.assertEqual(self.p2.pooltime,3)
        self.assertEqual(self.p3.pooltime,2)
        self.assertEqual(self.p4.pooltime,0)
        self.assertNotEqual(self.p4.pooltime,None)
    def test_add_bill(self):
        self.p1.add_bill(140)
        self.p2.add_bill(20)
        self.p3.add_bill(120)
        self.p4.add_bill(80)
        self.assertEqual(self.p1.bill,290)
        self.assertEqual(self.p2.bill,100)
        self.assertEqual(self.p3.bill,320)
        self.assertEqual(self.p4.bill,250)
        self.assertNotEqual(self.p4.bill,None)
    def test_reduce_bill(self):
        self.p1.reduce_bill(40)
        self.p2.reduce_bill(20)
        self.p3.reduce_bill(30)
        self.p4.reduce_bill(10)
        self.assertEqual(self.p1.bill,110)
        self.assertEqual(self.p2.bill,60)
        self.assertEqual(self.p3.bill,170)
        self.assertEqual(self.p4.bill,160)
        self.assertNotEqual(self.p1.bill,None)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Name:Alex Age:8 Duration:4 bill:150 pooltime:2')
        self.assertEqual(self.p2.display(),'Name:William Age:5 Duration:3 bill:80 pooltime:0')
        self.assertEqual(self.p3.display(),'Name:David Age:9 Duration:4 bill:200 pooltime:1')
        self.assertEqual(self.p4.display(),'Name:Carol Age:6 Duration:10 bill:170 pooltime:0')
        self.assertNotEqual(self.p1.display(),'Name:Alex,Age:8,Duration:4,bill:150,pooltime:2')#wrong format