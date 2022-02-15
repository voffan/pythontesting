import io
import unittest
from unittest.mock import patch
from program import nod


class test_nod(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(nod(25,35), 5)

    def test_testcase2(self):
        self.assertEqual(nod(1,1), 1)

    def test_testcase3(self):
        self.assertEqual(nod(3,15), 3)

    def test_testcase4(self):
        with self.assertRaises(Exception):
            nod(-1,5)

    def test_testcase5(self):
        with self.assertRaises(Exception):
            nod(3,-5)

    def test_testcase6(self):
        with self.assertRaises(ZeroDivisionError):
            nod(0,1)

    def test_testcase7(self):
        with self.assertRaises(ZeroDivisionError):
            nod(1,0)



if __name__ == '__main__':
    unittest.main()