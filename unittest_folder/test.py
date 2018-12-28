
def add(a,b):
    return a+b


def mul(a,b):
    return a*b



m = 10
n = 5

import unittest

class TestCases(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(m,n) ,15)

    def test_mul(self):
        self.assertEqual(add(m, n), 40)




# unittest.main()               #for executing all functions


tc  = TestCases()
tc.test_add()
tc.test_mul()
