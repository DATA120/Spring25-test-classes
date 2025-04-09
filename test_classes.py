#!/usr/bin/env python3

import unittest
from os.path import exists

from gradescope_utils.autograder_utils.decorators import weight, number

try:
    from pa4 import 
except ImportError:
    pass
try:
    from pa4 import 
except ImportError:
    pass

class TestXYZ(unittest.TestCase):
    def setUp(self):


# author: wltrimbl
    @weight(1)
    @number("0.0")
    def test_exist_pa4(self):
        '''Test that pa4.py exists'''
        self.assertTrue(exists("pa4.py"), "pa4.py does not exist!")




if __name__ == "__main__":
    unittest.main()
