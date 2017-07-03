import unittest
from prime_numbers import prime_number


class TestForPrimeNumbers(unittest.TestCase):
    def test_raises_error_if_arg_is_a_string(self):
        self.assertRaises(ValueError,prime_number, "2")

    def test_function_returns_a_list(self):
        result = prime_number(10)
        self.assertEqual(type(list), result, "A list is not returned")


