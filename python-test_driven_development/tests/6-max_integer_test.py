#!/usr/bin/python3
""" Unittests for max_integer """

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """run test with python3 -m unittest tests.6-max_integer_test"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, 0, -2]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([-1, 2, -3]), 2)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.33, -2.7, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)


if __name__ == "__main__":
    unittest.main()
