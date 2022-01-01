import unittest
import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from input_checker import Validator
from valid import validList
from invalid import invalidList

class TestChecker(unittest.TestCase):

    def test_Function_valid(self):
        v= Validator()
        for input in validList:
            self.assertTrue(v.function_check(input))

    
    def test_Function_invalid(self):
        v= Validator()
        for input in invalidList:
            self.assertFalse(v.function_check(input))        


if __name__ =="__main__":
    unittest.main()
