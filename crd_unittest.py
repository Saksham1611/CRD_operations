import unittest
from CRD_Class import *

x=CRD()


class TestD(unittest.TestCase):

    def test(self):
        self.assertEqual(sum([1, 2, 3]), 6, "")

    def test1(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test2(self):

if __name__ == '__main__':
    unittest.main()