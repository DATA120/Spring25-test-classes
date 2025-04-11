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

class TestShows(unittest.TestCase):
    def setUp(self):
        self.test_show1 = Show("CBS", "Survivor", "21-5", "Alliances shift and tempers flare as trust issues erupt during a high-stakes immunity challenge.", "Reality", 1900, 2000, False)
        self.test_show2 = Show("NBC", "The Office", "4-13", "Michael and Jan invite Jim, Pam, Andy, and Angela over for an incredibly awkward dinner.", "Comedy", 2000, 2100, False)
        self.guide1 = Guide([self.test_show1, self.test_show2])

        # You may add additional fixtures for your tests here
        

# author: Instructors
    @weight(1)
    @number("0.0")
    def test_exist_pa4(self):
        '''Test that pa4.py exists'''
        self.assertTrue(exists("pa4.py"), "pa4.py does not exist!")

# author: Instructors
    @weight(1)
    @number("0.1")
    def test_show_runs(self):
        '''Test Show constructor runs without error with valid input'''
        def construct():
            return Show("PBS", "Antiques Roadshow", "24-2", "A rare Magic: The Gathering card collection stuns appraisers with a six-figure value in Bonanzaville.", "Reality", 1300, 1400, False)
        construct()


# author: Instructors
    @weight(1)
    @number("0.2")
    def test_show_raises(self):
        '''Test Show constructor raises error when genre is not one of 6 provided'''
        def badconstruct(self):
            return Show("PBS", "Antiques Roadshow", "24-2", "A rare Magic: The Gathering card collection stuns appraisers with a six-figure value in Bonanzaville.", "Human Interest", 1300, 1400, False)
        self.assertRaises(ValueError, badconstruct,
          "Show constructor must raise error when genre is not in provided list")

# Your tests here


if __name__ == "__main__":
    unittest.main()
