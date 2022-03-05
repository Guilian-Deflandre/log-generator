import unittest
from src.main import function1

class UnitTest(unittest.TestCase):
    def test_function_1(self):
        self.assertEqual(function1(10), 10)

if __name__ == '__main__':
    unittest.main()