import unittest
from CRD_Class import *

x=CRD()


class TestD(unittest.TestCase):

    def test(self):
        self.assertEqual(x.create("VarunSehgal",1700360),None,msg="No message Displayed")
        self.assertEqual(x.create("VarunSehgal",1700360),""key is already Present"",msg="Message displayed should be key is already Present")
        # self.assertEqual(x.create("VarunSehgal",1700360),None,msg="No message Displayed")
        # self.assertEqual(x.create("VarunSehgal",1700360),None,msg="No message Displayed")
        # self.assertEqual(x.create("VarunSehgal",1700360),None,msg="No message Displayed")

    # def test2(self):

if __name__ == '__main__':
    unittest.main()
