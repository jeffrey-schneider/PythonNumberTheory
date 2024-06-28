import unittest
from NumberTheory import *
from Primes import *


class Test(unittest.TestCase):

    def setUp(self):
        print("In method: ", self._testMethodName, " ", self._testMethodDoc)

    def tearDown(self):
        pass

    def test_is_semi_prime(self):
        instance = Primes(74)
        self.assertTrue(Primes.is_semi_prime(instance))
        instance.set_the_number(92)
        self.assertFalse(Primes.is_semi_prime(instance))
        self.assertTrue(Primes.is_semi_prime(None, 15))
        self.assertFalse(Primes.is_semi_prime(None, 84))

    def test_get_prime_factors(self):
        instance = Primes(3600)
        result = Primes.get_prime_factors(instance)
        expected = [2, 2, 2, 2, 3, 3, 5, 5]
        self.assertListEqual(expected, result, "Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors list count should be equal")
        result = Primes.get_prime_factors(None, 42)
        expected = [2, 3, 7]
        self.assertListEqual(expected, result, "Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors list count should be equal")

    def test_countDigit(self):
        instance = Primes(3600)
        result = Primes.countDigit(3600)
        expected = 4
        self.assertEqual(result, expected)

    def test_is_brilliant(self):
        instance = Primes(209)
        self.assertTrue(Primes.is_brilliant(instance))
        self.assertTrue(Primes.is_brilliant(None, 247))
        instance.set_the_number(189)
        self.assertFalse(Primes.is_brilliant(instance))
        self.assertFalse(Primes.is_brilliant(None, 120))

    def test_is_emirpimeses(self):
        instance = Primes(143)
        self.assertTrue(Primes.is_emirpimeses(instance))
        self.assertTrue(Primes.is_emirpimeses(None, 205))
        instance.set_the_number(154)
        self.assertFalse(Primes.is_emirpimeses(instance))
        self.assertFalse(Primes.is_emirpimeses(None, 5130))

    def test_is_chen_prime(self):
        instance = Primes(257)
        self.assertTrue(Primes.is_chen_prime(instance))
        self.assertTrue(Primes.is_chen_prime(None, 9209))
        instance.set_the_number(234)
        self.assertFalse(Primes.is_chen_prime(instance))
        self.assertFalse(Primes.is_chen_prime(None, 3776))

    def test_is_emirp(self):
        instance = Primes(311)
        self.assertTrue(Primes.is_emirp(instance))
        self.assertTrue(Primes.is_emirp(None, 12149))
        self.assertTrue(Primes.is_emirp(None, 7219))
        instance.set_the_number(7756)
        self.assertFalse(Primes.is_emirp(instance))
        self.assertFalse(Primes.is_emirp(None,35))
        self.assertFalse(Primes.is_emirp(None, 11954))

    def test_is_good_prime(self):
        instance = Primes(853)
        self.assertTrue(Primes.is_good_prime(instance))
        self.assertTrue(Primes.is_good_prime(None, 84053))
        self.assertTrue(Primes.is_good_prime(None, 10847))
        instance = Primes(3000)
        self.assertFalse(Primes.is_good_prime(instance))
        self.assertFalse(Primes.is_good_prime(None, 7521))
        self.assertFalse(Primes.is_good_prime(None, 113))

    def test_get_previous_prime(self):
        instance = Primes(199)
        expected = 197
        result = Primes.get_previous_prime(None, 199)
        self.assertEqual(expected, result)
        expected = 1181
        result = Primes.get_previous_prime(None, 1187)
        self.assertEqual(expected, result)

    def test_get_previous_prime_inclusive(self):
        instance = Primes(199)
        expected = 199
        result = Primes.get_previous_prime_inclusive(instance)  # passed number is prime
        self.assertEqual(expected, result)
        expected = 211
        result = Primes.get_previous_prime_inclusive(None, 211)  # passed number is prime
        self.assertEqual(expected, result)
        result = Primes.get_previous_prime_inclusive(None, 230)  # passed number is not prime
        expected = 229
        self.assertEqual(expected, result)
        expected = 230
        self.assertNotEqual(expected, result)

    def test_get_next_prime(self):
        instance = Primes(199)
        expected = 211
        result = Primes.get_next_prime(instance)
        self.assertEqual(expected, result)
        result = Primes.get_next_prime(None, 211)
        expected = 223
        self.assertEqual(expected, result)
        expected = 211
        self.assertNotEqual(expected, result)

    def test_get_next_prime_inclusive(self):
        instance = Primes(198)
        expected = 199
        result = Primes.get_next_prime_inclusive(instance)
        self.assertEqual(expected, result)

        result = Primes.get_next_prime_inclusive(None, 211)
        expected = 211
        self.assertEqual(expected, result)

    def test_a_pointer_prime(self):
        instance = Primes(293)
        self.assertTrue(Primes.is_a_pointer_prime(instance))
        self.assertTrue(Primes.is_a_pointer_prime(None, 3221))
        self.assertTrue(Primes.is_a_pointer_prime(None, 149033))
        self.assertFalse(Primes.is_a_pointer_prime(None, 121508))

        instance.set_the_number(161123)
        self.assertTrue(Primes.is_a_pointer_prime(instance))
        instance.set_the_number(294)
        self.assertFalse(Primes.is_a_pointer_prime(instance))

    def test_m_pointer_prime(self):
        instance = Primes(1231)
        self.assertTrue(Primes.is_m_pointer_prime(instance))
        self.assertTrue(Primes.is_m_pointer_prime(None, 611113))
        self.assertTrue(Primes.is_m_pointer_prime(None, 13121117))
        self.assertTrue(Primes.is_m_pointer_prime(None, 1123))
        self.assertFalse(Primes.is_m_pointer_prime(None, 294))

    def test_is_interprime(self):
        instance = Primes(120)
        self.assertTrue(Primes.is_inter_prime(instance))
        self.assertTrue(Primes.is_inter_prime(None, 1482))
        self.assertTrue(Primes.is_inter_prime(None, 2802))
        instance.set_the_number(1020)
        self.assertTrue(Primes.is_inter_prime(instance))

        self.assertFalse(Primes.is_inter_prime(None, 1101))
        self.assertFalse(Primes.is_inter_prime(None,121))

    def test_get_prime_factors(self):
        instance = Primes(12)
        result = Primes.get_distinct_prime_factors(instance)
        expected = [2, 3, ]
        self.assertListEqual(expected, result, "Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors count should be equal")

        result = Primes.get_distinct_prime_factors(None, 60)
        expected = [2, 3, 5, ]
        self.assertListEqual(expected, result, "Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors count should be equal")

    @unittest.skip("Not ready to test, skipping")
    def test_get_prime_lucky_numbers(self):
        test_desc = "Get Prime Lucky Numbers "
        instance = Primes(150)
        result = Primes.get_prime_lucky_numbers()
        expected = [1, 3, 7, 13, 31, 37, 43, 67, 73, 79, 127]
        self.assertListEqual(expected, result, test_desc + " list should be equal")
        self.assertCountEqual(expected, result, test_desc + " count should be equal")

    @unittest.skip("Not ready to test, skipping")
    def test_to_skip(self):
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
