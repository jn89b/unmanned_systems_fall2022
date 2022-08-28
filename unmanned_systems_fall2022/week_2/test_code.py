import os
import unittest
import main_code
from util_functions import some_functions

class TestFunctions(unittest.TestCase):
    def test_good_add(self):
        """test and see if I can return correct values"""
        input_x = 4 
        input_y = 5
        results = some_functions.add(input_x, input_y)        
        assert results == 9
        
    def test_bad_input(self):
        """test """
        pass

class TestMainFunctions(unittest.TestCase):        
    def test_print(self):
        input = "justin"
        value = main_code.print_hello(input)
        self.assertEqual(value, "hello justin")

class TestNodeClass(unittest.TestCase):
    def test_comparison(self):
        """two nodes with same class, can also instiate 
        nodes here"""
        self.node_1 = main_code.Node([0,0,1], [0,0,0,2])
        self.node_1.f = 5
        self.node_2 = main_code.Node([0,0,1], [0,0,0,2])
        self.node_2.f = 5
        self.assertEqual(self.node_1, self.node_2)
        
if __name__ == "__main__":
    
    """import and use assert and print value"""
    # value = some_functions.add(3,5)
    # print("value is ", value)
    # assert value == 8
    
    unittest.main()
    
    