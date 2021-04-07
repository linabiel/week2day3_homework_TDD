import unittest

from src.compare import compare


class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare__10_returns_10_is_equal_to_10(self):
        self.assertEqual("numbers are the same", compare(10, 10))
