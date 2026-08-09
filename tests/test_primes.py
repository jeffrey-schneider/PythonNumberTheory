import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import primes
import unittest


class TestPrimes(unittest.TestCase):
    
    def test_is_prime_static_true(self):
        self.assertTrue(primes.is_prime(7))
        self.assertTrue(primes.is_prime(2))
        self.assertFalse(primes.is_prime(6))

    
    def test_get_distinct_prime_factors(self):
        self.assertEqual(sorted(primes.get_distinct_prime_factors(12)), [2, 3])

    
    def test_get_prime_factors(self):
        self.assertEqual(sorted(primes.get_prime_factors(12)), [2, 2, 3])

    
    def test_is_semi_prime(self):
        self.assertTrue(primes.is_semi_prime(49))
        self.assertFalse(primes.is_semi_prime(48))

    
    def test_get_digit_count(self):
        self.assertEqual(primes.get_digit_count(123), 3)
        self.assertEqual(primes.get_digit_count(1), 1)

    
    def test_is_brilliant(self):
        self.assertTrue(primes.is_brilliant(299))
        self.assertFalse(primes.is_brilliant(222))

    
    def test_is_emirpimeses(self):
        self.assertTrue(primes.is_emirpimes(205))
        self.assertFalse(primes.is_emirpimes(204))

    
    def test_is_chen_prime(self):
        self.assertTrue(primes.is_chen_prime(251))
        self.assertFalse(primes.is_chen_prime(256))

    
    def test_is_emirp(self):
        self.assertTrue(primes.is_emirp(751)) 
        self.assertFalse(primes.is_emirp(750))

    
    def test_is_good_prime(self):
        self.assertTrue(primes.is_good_prime(599))
        self.assertFalse(primes.is_good_prime(600))

    
    
    
    def test_is_droll(self):
        self.assertTrue(primes.is_droll(72))
        self.assertFalse(primes.is_droll(73))

    
    def test_get_prime_lucky_numbers(self):
        self.assertEqual(sorted(primes.get_prime_lucky_numbers(7)), [3, 7, 13])        
        actual = sorted(primes.get_prime_lucky_numbers(7))
        expected = [3, 7, 13]
        self.assertEqual(actual, expected)

    
    def test_is_sphenic(self):
        self.assertTrue(primes.is_sphenic(30))
        self.assertFalse(primes.is_sphenic(31))
        

    def test_is_inter_prime(self):
        self.assertTrue(primes.is_inter_prime(9))
        self.assertFalse(primes.is_inter_prime(11))

    def test_get_next_prime(self):
        self.assertEqual(primes.get_next_prime(10), 11)
    
    def test_get_previous_prime(self):        
        self.assertEqual(primes.get_previous_prime(10), 7)

    def test_get_previous_prime_of_two(self):
        self.assertEqual(primes.get_previous_prime(2), 0)

    def test_get_next_prime_inclusive(self):
        self.assertEqual(primes.get_next_prime_inclusive(11), 11)
        self.assertEqual(primes.get_next_prime_inclusive(12), 13)

    def test_get_previous_prime_inclusive(self):
        self.assertEqual(primes.get_previous_prime_inclusive(11), 11)
        self.assertEqual(primes.get_previous_prime_inclusive(14), 13)

    def test_is_a_pointer_prime(self):
        self.assertFalse(primes.is_a_pointer_prime(-7))
        self.assertFalse(primes.is_a_pointer_prime(0))
        self.assertFalse(primes.is_a_pointer_prime(1))
        self.assertFalse(primes.is_a_pointer_prime(2))
        self.assertTrue(primes.is_a_pointer_prime(293))
        self.assertFalse(primes.is_a_pointer_prime(294))

    def test_is_m_pointer_prime(self):
        self.assertFalse(primes.is_m_pointer_prime(-7))
        self.assertFalse(primes.is_m_pointer_prime(0))
        self.assertFalse(primes.is_m_pointer_prime(1))
        self.assertTrue(primes.is_m_pointer_prime(1112611))
        self.assertTrue(primes.is_m_pointer_prime(19121))

    def test_is_co_prime(self):
        self.assertTrue(primes.is_co_prime(8, 15))
        self.assertFalse(primes.is_co_prime(12, 18))
        self.assertTrue(primes.is_co_prime(0, 1))
        self.assertFalse(primes.is_co_prime(0, 2))
        self.assertTrue(primes.is_co_prime(8, -25))

    def test_get_lonely_numbers(self):
        expected = [ 0, 23, 53, 120, 211, 1340, 1341, 1342, 1343, 1344, 2179, 3967, 15704, 15705, 16033, 19634, 19635]
        actual = primes.get_lonely_numbers(20000)
        self.assertEqual(actual, expected)   

    def test_distance_to_closest_prime(self):
        expected = 4
        actual = primes.get_distance_to_closest_prime(23)
        self.assertEqual(actual, expected)   

    def test_get_primes_up_to(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        actual =  primes.get_primes_up_to(23)
        self.assertEqual(actual, expected)   

    def test_get_first_n_primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
        actual = primes.get_first_n_primes(23)
        self.assertEqual(actual, expected)  

    def test_is_n_smooth(self):
        self.assertTrue(primes.is_n_smooth(60, 5))    
        self.assertFalse(primes.is_n_smooth(98, 5))
    
    def test_is_pierpont_prime(self):
        self.assertTrue(primes.is_pierpont_prime(109))
        self.assertFalse(primes.is_pierpont_prime(31))
        self.assertFalse(primes.is_pierpont_prime(1))

    def test_generate_primes(self):
        self.assertEqual(primes.generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])  
    

    def test_get_prime_sieve(self):
        sieve = primes.get_prime_sieve(10)
        self.assertFalse(sieve[0])
        self.assertFalse(sieve[1])
        self.assertTrue(sieve[2])
        self.assertTrue(sieve[3])
        self.assertFalse(sieve[4])
        self.assertTrue(sieve[5])
        self.assertFalse(sieve[6])
        self.assertTrue(sieve[7])
        self.assertFalse(sieve[8])
        self.assertFalse(sieve[9])
        self.assertFalse(sieve[10])


    def test_get_fortunate_number(self):
        self.assertEqual(primes.get_fortunate_number(1), 3)
        self.assertEqual(primes.get_fortunate_number(2), 5)
        self.assertEqual(primes.get_fortunate_number(3), 7)
        self.assertEqual(primes.get_fortunate_number(4), 13)
       

if __name__ == '__main__':
    unittest.main()