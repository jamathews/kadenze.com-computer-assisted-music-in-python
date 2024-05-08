from random import randint
from unittest import TestCase

from Coursework.Coursework_1 import a_times_b
from Coursework.Coursework_1 import first_five_powers_of_base
from Coursework.Coursework_1 import first_n_powers
from Coursework.Coursework_1 import first_seven_fibonnaci

TEST_RANGE = 100


class Test(TestCase):
    def test_first_n_powers(self):
        for i in range(TEST_RANGE):
            base = randint(1, TEST_RANGE)
            n = randint(1, TEST_RANGE)
            result = first_n_powers(base=base, n=n)
            expected = []
            for power in range(1, n + 1):
                expected.append(base ** power)
            self.assertListEqual(result, expected)

    def test_a_times_b(self):
        for i in range(TEST_RANGE):
            a = randint(1, TEST_RANGE)
            b = randint(1, TEST_RANGE)
            self.assertEqual(a_times_b(a, b), a * b)

    def test_first_five_powers_of_base(self):
        for i in range(TEST_RANGE):
            base = randint(1, TEST_RANGE)
            result = first_five_powers_of_base(base=base)
            expected = [base, base ** 2, base ** 3, base ** 4, base ** 5]
            self.assertListEqual(result, expected)

    def test_first_seven_fibonnaci(self):
        result = first_seven_fibonnaci()
        expected = [1, 1, 2, 3, 5, 8, 13]
        self.assertListEqual(result, expected)
