
import unittest

class TestCaseCreation(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        print("will run only one time before all the function")
    def setUp(self):
        print("will run before each test function")
    def testOne(self):
        print("here only we are going to write the logic") 
    def tearDown(self):
        print("will run after each test function")
 
    @classmethod
    def tearDownClass(cls):
        print("will run after all the method")