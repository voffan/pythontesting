import unittest
from program import nok

class Nok_Tests(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(nok(25,35), 17)

    def test_testcase2(self):
        self.assertEqual(nok(1, 1), 1)

    def test_testcase3(self):
        self.assertEqual(nok(3, 15), 15)

    def test_testcase4(self):
        with self.assertRaises(Exception):
            nok(-1,5)

    def test_testcase5(self):
        with self.assertRaises(Exception):
            nok(3,-5)

    def test_testcase6(self):
        with self.assertRaises(ZeroDivisionError):
            nok(0,1)

    def test_testcase7(self):
        with self.assertRaises(ZeroDivisionError):
            nok(1,0)


if __name__ == '__main__':
    unittest.main()