# coding=utf-8

import unittest
from pydigits import sum_pi_digits


class ValidationTests(unittest.TestCase):

    def test_validation_simple_cases_all(self):
        self.assertEqual(sum_pi_digits(1), 1)
        self.assertEqual(sum_pi_digits(5), 20)
        self.assertEqual(sum_pi_digits(1, notation='binary'), 1)
        self.assertEqual(sum_pi_digits(5, notation='binary'), 10100)

    def test_validation_simple_cases_odd(self):
        self.assertEqual(sum_pi_digits(1, 'odd'), 1)
        self.assertEqual(sum_pi_digits(5, 'odd'), 16)
        self.assertEqual(sum_pi_digits(1, 'odd', 'binary'), 1)
        self.assertEqual(sum_pi_digits(5, 'odd', 'binary'), 10000)

    def test_validation_simple_cases_even(self):
        self.assertEqual(sum_pi_digits(1, 'even'), 0)
        self.assertEqual(sum_pi_digits(5, 'even'), 4)
        self.assertEqual(sum_pi_digits(1, 'even', notation='binary'), 0)
        self.assertEqual(sum_pi_digits(5, 'even', notation='binary'), 100)

    def test_validation_complex_case(self):
        self.assertEqual(sum_pi_digits(31_415, 'odd'), 78662)
        self.assertEqual(sum_pi_digits(31_415, 'odd', 'binary'), 10011001101000110)

    def test_validation_on_no_int(self):
        self.assertRaises(TypeError, sum_pi_digits, 'trolleo')
        self.assertRaises(TypeError, sum_pi_digits, 'trolleo', 'odd', 'binary')

    def test_validation_negative_numbers(self):
        self.assertEqual(sum_pi_digits(-1, 'odd'), 0)
        self.assertEqual(sum_pi_digits(-1_000, 'all'), 0)
        self.assertEqual(sum_pi_digits(-5, 'even'), 0)
    
    def test_validation_on_no_correct_nature(self):
        self.assertRaises(TypeError, sum_pi_digits, 1, 'trolleo', 'binary')

    def test_validation_on_no_correct_notation(self):
        self.assertRaises(TypeError, sum_pi_digits, 1, 'odd', 'trolleo')

    # To do time out test
    # import timeout_decorator
    # # @timeout_decorator.timeout(5)
    # def test_that_can_take_too_long(self):
    #     # import time
    #     # time.sleep(float('inf'))
    #     from sys import maxsize
    #     self.assertFalse(sum_pi_digits(maxsize))


if __name__ == '__main__':
    unittest.main()
