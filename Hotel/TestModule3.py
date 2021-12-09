#test Employee module
import unittest
import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from Person.employee import Employee
class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup Employee class')
    @classmethod
    def tearDownClass(cls):
        print('Teardown Employee class')
    def setUp(self):
        self.p1 = Employee('Jack',30,20,30,600)
        self.p2 = Employee('Cassie',35,15,10,250)
        self.p3 = Employee('Ann',35,12,30,360)
        self.p4 = Employee('Anqi',34,20,10,200)
    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.p4
    def test_add_work_salary(self):
        self.p1.add_work_salary(20)
        self.p2.add_work_salary(10)
        self.p3.add_work_salary(50)
        self.p4.add_work_salary(50)
        self.assertEqual(self.p1.workhour,50)
        self.assertEqual(self.p2.workhour,20)
        self.assertEqual(self.p1.salary,1000)
        self.assertEqual(self.p2.salary,400)
        self.assertEqual(self.p3.salary,960)
    def test_add_bonus(self):
        self.p1.add_bonus(140)
        self.p2.add_bonus(20)
        self.p3.add_bonus(80)
        self.p4.add_bonus(100)
        self.assertEqual(self.p1.salary,740)
        self.assertEqual(self.p2.salary,270)
        self.assertEqual(self.p3.salary,440)
        self.assertEqual(self.p4.salary,300)
        self.assertNotEqual(self.p4.salary,None)
        self.assertIsInstance(self.p2,Employee)
    def test_reduce_salary(self):
        self.p1.reduce_salary(40)
        self.p2.reduce_salary(50)
        self.p3.reduce_salary(40)
        self.p4.reduce_salary(50)
        self.assertEqual(self.p1.salary,560)
        self.assertEqual(self.p2.salary,200)
        self.assertEqual(self.p3.salary,320)
        self.assertEqual(self.p4.salary,150)
        self.p1.reduce_salary(50)
        self.assertEqual(self.p1.salary,510)
    def test_display(self):
        self.assertEqual(self.p1.display(),'Name:Jack Age:30 Hourlyrate:20 Workhour:30 Salary:600')
        self.assertEqual(self.p2.display(),'Name:Cassie Age:35 Hourlyrate:15 Workhour:10 Salary:250')
        self.assertEqual(self.p3.display(),'Name:Ann Age:35 Hourlyrate:12 Workhour:30 Salary:360')
        self.assertEqual(self.p4.display(),'Name:Anqi Age:34 Hourlyrate:20 Workhour:10 Salary:200')
        self.assertNotEqual(self.p1.display(),'Name:Jack, Age:30, Hourlyrate:20 Workhour:30 Salary:600')#wrong format