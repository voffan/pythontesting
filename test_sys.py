import unittest
from program import main

class Sys_Tests(unittest.TestCase):
    def test_testcase1(self):
        inputs = ['21','15']
        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            with patch('builtins.input', side_effect=inputs) as mock_input:
                main()
        self.assertEqual(mock_print.getvalue(), '105\n')

    def test_testcase4(self):
        with self.assertRaises(Exception):
            inputs = ['a','15']
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                with patch('builtins.input', side_effect=inputs) as mock_input:
                    main()


if __name__ == '__main__':
    unittest.main()