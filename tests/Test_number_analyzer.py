import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from NumberAnalyzer import NumberAnalyzer

class TestNumberAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = NumberAnalyzer(205)

    def test_constructor_sets_value(self):
        analyzer = NumberAnalyzer(120)
        self.assertEqual(analyzer.value, 120)


    def test_value_property_can_be_changed(self):
        analyzer = NumberAnalyzer(120)
        analyzer.value = 211
        self.assertEqual(analyzer.value, 211)


    def test_is_prime(self):
        analyzer = NumberAnalyzer(23)
        self.assertTrue(analyzer.is_prime)
        analyzer.value = 24
        self.assertFalse(analyzer.is_prime)


    def test_get_distinct_prime_factors(self):
        analyzer = NumberAnalyzer(12)
        self.assertEqual(sorted(analyzer.get_distinct_prime_factors), [2, 3])


    def test_get_prime_factors(self):
        analyzer = NumberAnalyzer(12)
        self.assertEqual(analyzer.get_prime_factors, [2, 2, 3])

    def test_is_semi_prime(self):
        analyzer = NumberAnalyzer(49)
        self.assertTrue(analyzer.is_semi_prime)
        analyzer = NumberAnalyzer(48)
        self.assertFalse(analyzer.is_semi_prime)

    def test_get_digit_count(self):
        analyzer = NumberAnalyzer(123)
        self.assertEqual(analyzer.get_digit_count, 3)
        analyzer.value = 1
        self.assertEqual(analyzer.get_digit_count, 1)

    def test_is_brilliant(self):
        analyzer = NumberAnalyzer(299)
        self.assertTrue(analyzer.is_brilliant)
        analyzer.value = 222
        self.assertFalse(analyzer.is_brilliant)

    def test_is_emirpimeses(self):
        analyzer = NumberAnalyzer(205)
        self.assertTrue(self.analyzer.is_emirpimes)
        self.analyzer.value = 204
        self.assertFalse(self.analyzer.is_emirpimes)

    def test_is_chen_prime(self):
        analyzer = NumberAnalyzer(251)
        self.assertTrue(analyzer.is_chen_prime)
        analyzer.value = 256
        self.assertFalse(analyzer.is_chen_prime)

    def test_is_emirp(self):
        analyzer = NumberAnalyzer(751)
        self.assertTrue(analyzer.is_emirp)    
        analyzer.value = 750
        self.assertFalse(analyzer.is_emirp)    

    def test_is_good_prime(self):
        analyzer = NumberAnalyzer(599)
        self.assertTrue(analyzer.is_good_prime)
        analyzer.value = 600
        self.assertFalse(analyzer.is_good_prime)

    def test_is_droll(self):
        analyzer = NumberAnalyzer(72)
        self.assertTrue(analyzer.is_droll)
        analyzer.value = 73
        self.assertFalse(analyzer.is_droll)


    def test_get_prime_lucky_numbers(self):
        analyzer = NumberAnalyzer(7)
        expected = [3, 7, 13]
        self.assertEqual(sorted(analyzer.get_prime_lucky_numbers), expected)        
        self.assertListEqual(
           sorted(analyzer.get_prime_lucky_numbers),
            expected
        )

    def test_is_sphenic(self):
        analyzer = NumberAnalyzer(30)
        self.assertTrue(analyzer.is_sphenic)
        analyzer.value = 31
        self.assertFalse(analyzer.is_sphenic)
  
    
    def test_is_inter_prime(self):
        analyzer = NumberAnalyzer(9)
        self.assertTrue(analyzer.is_inter_prime)
        analyzer.value = 11
        self.assertFalse(analyzer.is_inter_prime)

    def test_get_next_prime(self):
        analyzer = NumberAnalyzer(10)
        self.assertEqual(analyzer.get_next_prime, 11)

    def test_get_previous_prime_of_two(self):
        analyzer = NumberAnalyzer(2)
        self.assertEqual(analyzer.get_previous_prime,0)

    def test_get_previous_prime(self):
        analyzer = NumberAnalyzer(10)
        self.assertEqual(analyzer.get_previous_prime, 7)    

    def test_get_next_prime_inclusive(self):
        analyzer = NumberAnalyzer(11)
        self.assertEqual(analyzer.get_next_prime_inclusive, 11)
        analyzer.value = 14
        self.assertEqual(analyzer.get_next_prime_inclusive, 17)

    def test_get_previous_prime_inclusive(self):
        analyzer = NumberAnalyzer(11)
        self.assertEqual(analyzer.get_previous_prime_inclusive, 11)
        analyzer.value = 14
        self.assertEqual(analyzer.get_previous_prime_inclusive, 13)


    def test_is_a_pointer_prime(self):
        analyzer = NumberAnalyzer(-7)
        self.assertFalse(analyzer.is_a_pointer_prime)
        analyzer.value = 0
        self.assertFalse(analyzer.is_a_pointer_prime)
        analyzer.value = 1
        self.assertFalse(analyzer.is_a_pointer_prime)
        analyzer.value = 2
        self.assertFalse(analyzer.is_a_pointer_prime)
        analyzer.value = 293
        self.assertTrue(analyzer.is_a_pointer_prime)
        analyzer.value = 294
        self.assertFalse(analyzer.is_a_pointer_prime)

    def test_is_m_pointer_prime(self):
        analyzer = NumberAnalyzer(-7)
        self.assertFalse(analyzer.is_m_pointer_prime)
        analyzer.value = 0
        self.assertFalse(analyzer.is_m_pointer_prime)
        analyzer.value = 1
        self.assertFalse(analyzer.is_m_pointer_prime)
        analyzer.value = 1112611
        self.assertTrue(analyzer.is_m_pointer_prime)
        analyzer.value = 19121
        self.assertTrue(analyzer.is_m_pointer_prime)

    def test_is_co_prime(self):
        analyzer = NumberAnalyzer(8)
        self.assertTrue(analyzer.is_co_prime(15))
        analyzer.value = 12
        self.assertFalse(analyzer.is_co_prime(18))
        analyzer.value = 0
        self.assertTrue(analyzer.is_co_prime(1))        
        self.assertFalse(analyzer.is_co_prime(2))
        analyzer.value = 8
        self.assertTrue(analyzer.is_co_prime(-25))

    def test_get_lonely_numbers(self):
        analyzer = NumberAnalyzer(20000)
        expected = [ 0, 23, 53, 120, 211, 1340, 1341, 1342, 1343, 1344, 2179, 3967, 15704, 15705, 16033, 19634, 19635]
        actual = analyzer.get_lonely_numbers
        self.assertEqual(actual, expected)  

    def test_distance_to_closest_prime(self):
        expected = 4
        analyzer = NumberAnalyzer(23)
        actual = analyzer.get_distance_to_closest_prime
        self.assertEqual(actual, expected)

    def test_get_primes_up_to(self):
        analyzer = NumberAnalyzer(23)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        actual =  analyzer.get_primes_up_to
        self.assertEqual(actual, expected)  

    def test_get_first_n_primes(self):
        analyzer = NumberAnalyzer(23)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
        actual = analyzer.get_first_n_primes
        self.assertEqual(actual, expected)

    def test_is_n_smooth(self):
        analyzer = NumberAnalyzer(60)
        self.assertTrue(analyzer.is_n_smooth(5))    
        analyzer = NumberAnalyzer(98)
        self.assertFalse(analyzer.is_n_smooth(5)) 

    def test_is_pierpont_prime(self):
        analyzer = NumberAnalyzer(109)
        self.assertTrue(analyzer.is_pierpont_prime)
        analyzer.value = 31
        self.assertFalse(analyzer.is_pierpont_prime)
        analyzer.value = 1
        self.assertFalse(analyzer.is_pierpont_prime) 

    def test_generate_primes(self):
        analyzer = NumberAnalyzer(20)
        self.assertEqual(analyzer.generate_primes, [2, 3, 5, 7, 11, 13, 17, 19]) 

    def test_get_prime_sieve(self):        
        analyzer = NumberAnalyzer(10)
        self.assertFalse(analyzer.get_prime_sieve[0])
        self.assertFalse(analyzer.get_prime_sieve[1])
        self.assertTrue(analyzer.get_prime_sieve[2])
        self.assertTrue(analyzer.get_prime_sieve[3])
        self.assertFalse(analyzer.get_prime_sieve[4])
        self.assertTrue(analyzer.get_prime_sieve[5])
        self.assertFalse(analyzer.get_prime_sieve[6])
        self.assertTrue(analyzer.get_prime_sieve[7])
        self.assertFalse(analyzer.get_prime_sieve[8])
        self.assertFalse(analyzer.get_prime_sieve[9])
        self.assertFalse(analyzer.get_prime_sieve[10])

    def test_get_fortunate_number(self):
        analyzer = NumberAnalyzer(1)        
        expected = 3
        self.assertEqual(analyzer.get_fortunate_number, expected)
        analyzer.value = 2
        expected = 5
        self.assertEqual(analyzer.get_fortunate_number, expected)
        analyzer.value = 3
        expected = 7
        self.assertEqual(analyzer.get_fortunate_number, expected)
        analyzer.value = 4
        expected = 13
        self.assertEqual(analyzer.get_fortunate_number, expected)


if __name__ == "__main__":
    unittest.main()