# Problem Statement : Test that the code segment for factorial is correct.

"""
Explanation:

Input 5, given output 120.
As the factorial of 5 is 120.
The testing will show "OK" if the code is correct.
"""

import unittest
import math
class TestFactorial(unittest.TestCase):
    def test_fact(self):
        res = math.factorial(5)
        self.assertEqual(res, 120)
if __name__ == '__main__':
    unittest.main()