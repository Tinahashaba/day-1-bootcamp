import unittest
from prime_numbers import prime_number


class TestForPrimeNumbers(unittest.TestCase):
    def test_raises_error_if_arg_is_a_string(self):
        self.assertRaises(ValueError, prime_number, "2")

    def test_function_returns_a_list(self):
        result = prime_number(10)
        self.assertEqual(type(result), list, "A list is not returned")

    def test_empty_list_returned_when_arg_is_negative(self):
        result = prime_number(-5)
        self.assertEqual([], result, "function should return an empty list")

    def test_function_returns_a_list_of_integer(self):
        self.assertEqual(all(isinstance(int, n) for n in prime_number(10)), "Returned list has non-integer elements")

    def test_function_returns_correct_result(self):
        result = prime_number(10)
        self.assertEqual([2, 3, 5, 7], result)
