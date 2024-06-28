'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import unittest

import NumberTheory
from NumberTheory import *
from Primes import *


class Test(unittest.TestCase):

    def setUp(self):
        print("In method: ", self._testMethodName, " ", self._testMethodDoc)

    def tearDown(self):
        pass

    def testisEven(self):
        # instance = NumberTheory.NumberTheory(13)
        instance = NumberTheory(13)
        instance.set_the_number(914)
        self.assertTrue(NumberTheory.is_even(instance,None))
        # self.assertTrue(instance.is_even(12))

    def testIsAbundant(self):
        # instance = NumberTheory.NumberTheory(12)
        instance = NumberTheory(12)
        self.assertTrue(NumberTheory.is_abundant(instance,None))
        self.assertTrue(NumberTheory.is_abundant(None, 96))
        self.assertFalse(NumberTheory.is_abundant(None,95))

    def testGetNumber(self):
        instance = NumberTheory(15)
        instance.set_the_number(91)
        expected = 91
        result = instance.get_the_number()
        self.assertEqual(result, expected)

    def testGetCollatz(self):
        instance = NumberTheory(5)
        expected = [5, 16, 8, 4, 2, 1]
        result = NumberTheory.get_collatz(instance,None)
        self.assertListEqual(expected, result, "Collatz list should be equal")
        self.assertCountEqual(expected, result, "Collatz count should be equal")

    def testGetJugglers(self):
        instance = NumberTheory(5)
        expected = [5, 11, 36, 6, 2, 1]
        result = NumberTheory.get_jugglers(instance,None)
        self.assertListEqual(expected, result, "Jugglers list should be equal")
        self.assertCountEqual(expected, result, "Jugglers count should be equal")
        result = NumberTheory.get_jugglers(None,37)
        expected = [37, 225, 3375, 196069, 86818724, 9317, 899319, 852846071, 24906114455136, 4990602, 2233, 105519,
                    34276462, 5854, 76, 8, 2, 1]
        self.assertListEqual(expected, result, "Jugglers list should be equal")
        self.assertCountEqual(expected, result, "Jugglers count should be equal")

    def testGetPrimeFactors(self):
        #TODO fix after primes update
        # instance = NumberTheory(3600)
        instance = Primes(3600)
        expected = [2, 2, 2, 2, 3, 3, 5, 5]
        result = Primes.get_prime_factors(instance,None)
        self.assertListEqual(expected, result, "Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors count should be equal")

    def testGetFactors(self):
        instance = NumberTheory(3600)
        expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36, 40, 45, 48, 50, 60, 72, 75, 80, 90,
                    100, 120, 144, 150, 180, 200, 225, 240, 300, 360, 400, 450, 600, 720, 900, 1200, 1800, 3600]
        result = NumberTheory.get_factors(instance)
        self.assertListEqual(expected, result, "Factors list should be equal")
        self.assertCountEqual(expected, result, "Factors count should be equal")

    def testAliquotSum(self):
        instance = NumberTheory(60)
        expected = 108
        result = NumberTheory.get_aliquot_sum(instance)
        self.assertEqual(result, expected, "Aliquot sum()")

    def testGetReverseNumber(self):
        instance = NumberTheory(34)
        result = NumberTheory.get_reverse_number(instance)
        expected = 43
        self.assertEqual(result, expected, "Reversed Number")
        result = NumberTheory.get_reverse_number(None, 95)
        expected = 59
        self.assertEqual(result, expected, "Reversed Number")

    def testGetReciprocalNumber(self):
        instance = NumberTheory(43)
        result = NumberTheory.get_reciprocal_number(instance)
        expected = 0.023255813953488372
        self.assertAlmostEqual(result, expected, 7, "Reciprocal Number", delta=None)
        result = NumberTheory.get_reciprocal_number(None, 4)
        expected = 0.25
        self.assertAlmostEqual(result, expected, 7, "Reciprocal Number", delta=None)

    def testGetHex(self):
        instance = NumberTheory(76576500)
        result = NumberTheory.get_hex(instance)
        expected = "49076F4"
        self.assertEqual(result, expected, "Get Hex")
        result = NumberTheory.get_hex(None, 84)
        expected = "54"
        self.assertEqual(result, expected, "Get Hex")

    def testGetOctal(self):
        instance = NumberTheory(76576500)
        result = NumberTheory.get_octal(instance)
        expected = "444073364"
        self.assertEqual(result, expected, "Get Octal")
        result = NumberTheory.get_octal(None, 76576501)
        expected = "444073365"
        self.assertEqual(result, expected, "Get Octal")

    def testGetBinary(self):
        instance = NumberTheory(76576500)
        result = NumberTheory.get_binary(instance)
        expected = "100100100000111011011110100"
        self.assertEqual(result, expected, "Get Hex")
        result = NumberTheory.get_binary(None, 845)
        expected = "1101001101"
        self.assertEqual(result, expected, "Get Hex")

    def testIsPerfect(self):
        instance = NumberTheory(8128)
        self.assertTrue(NumberTheory.is_perfect(instance))
        self.assertTrue(NumberTheory.is_perfect(None,496))
        self.assertFalse(NumberTheory.is_perfect(None, 495))

    def testGetSigma(self):
        instance = NumberTheory(9)
        result = NumberTheory.get_sigma(instance)
        expected = 13
        self.assertEqual(result, expected, "Get Sigma")
        result = NumberTheory.get_sigma(None, 15)
        expected = 24
        self.assertEqual(result, expected, "Get Sigma")

    def testGetKynea(self):
        instance = NumberTheory(5)
        result = NumberTheory.get_kynea(instance)
        expected = 1087
        self.assertEqual(result, expected, "Get Kynea")
        result = NumberTheory.get_kynea(None, 6)
        expected = 4223
        self.assertEqual(result, expected, "Get Kynea")

    def testGetCarol(self):
        instance = NumberTheory(7)
        result = NumberTheory.get_carol(instance)
        expected = 16127
        self.assertEqual(result, expected, "Get Carol")
        self.assertEqual(65023, NumberTheory.get_carol(None, 8), "Get Carol")
        self.assertNotEqual(615023, NumberTheory.get_carol(None, 7), "Get Carol")

    def testGetFactorials(self):
        instance = NumberTheory(10)
        result = NumberTheory.factorial(instance.get_the_number())
        expected = 3628800
        self.assertEqual(result, expected, "Get Factorial")
        result = NumberTheory.factorial(12)
        expected = 479001600
        self.assertEqual(result, expected, "Get Factorial")

    def testGetCatalan(self):
        instance = NumberTheory(20)
        result = NumberTheory.get_catalan(instance)
        expected = 6564120420
        self.assertEqual(result, expected, "Get Catalan")
        result = NumberTheory.get_catalan(None, 10)
        expected = 16796
        self.assertEqual(result, expected, "Get Catalan")

    def testGetFibonacciList(self):
        instance = NumberTheory(20)
        result = NumberTheory.get_fibonacci_list(instance)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        self.assertListEqual(expected, result, "Fibonacci list should be equal")
        self.assertCountEqual(expected, result, "Fibonacci count should be equal")
        result = NumberTheory.get_fibonacci_list(None, 15)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        self.assertListEqual(expected, result, "Fibonacci list should be equal")
        self.assertCountEqual(expected, result, "Fibonacci count should be equal")

    def testGetMotzkin(self):
        instance = NumberTheory(20)
        result = NumberTheory.get_motzkin(instance)
        expected = 50852019
        self.assertEqual(result, expected, "Get Motzkin")
        result = NumberTheory.get_motzkin(None,15)
        expected = 310572
        self.assertEqual(result, expected, "Get Motzkin")

    def testGetLucas(self):
        instance = NumberTheory(12)
        result = NumberTheory.get_lucas_list(instance)
        expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, ]
        self.assertListEqual(expected, result, "Lucas list should be equal")
        self.assertCountEqual(expected, result, "Lucas count should be equal")
        result = NumberTheory.get_lucas_list(None, 33)
        expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364,
                    2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079, 103682, 167761, 271443, 439204, 710647, 1149851,
                    1860498, 3010349, 4870847, ]
        self.assertListEqual(expected, result, "Lucas list should be equal")
        self.assertCountEqual(expected, result, "Lucas count should be equal")

    def testPrimitiveAbundant(self):
        instance = NumberTheory(7532)
        self.assertTrue(NumberTheory.is_primitive_abundant(instance))
        self.assertTrue(NumberTheory.is_primitive_abundant(None, 3606))
        instance = NumberTheory(2801)
        self.assertFalse(NumberTheory.is_primitive_abundant(instance))
        self.assertFalse(NumberTheory.is_primitive_abundant(None, 3607))

    def testSuperAbundant(self):
        instance = NumberTheory(1260)
        self.assertTrue(NumberTheory.is_super_abundant(instance))

    def testIsAKeithNumber(self):
        instance = NumberTheory(1104)
        self.assertTrue(NumberTheory.is_keith_number(instance))
        self.assertTrue(NumberTheory.is_keith_number(None, 7913837))
        self.assertFalse(NumberTheory.is_keith_number(None,7913838))

    def testAmicableNumber(self):
        instance = NumberTheory(220)
        result = NumberTheory.get_amicable_number(instance)
        expected = 284
        self.assertEqual(result, expected, "Get Amicable")
        result = NumberTheory.get_amicable_number(None, 12285)
        expected = 14595
        self.assertEqual(result, expected, "Get Amicable")

    def testBetrothedNumbers(self):
        instance = NumberTheory(9504)
        result = NumberTheory.get_betrothed_number(instance)
        expected = 20735
        self.assertEqual(result, expected, "Get Betrothed")
        result = NumberTheory.get_betrothed_number(None,1050)
        expected = 1925
        self.assertEqual(result, expected, "Get Betrothed")

    def testCakeNumbers(self):
        instance = NumberTheory(24)
        result = NumberTheory.get_cake_number(instance)
        expected = 2325
        self.assertEqual(result, expected, "Get Cake Number")
        result = NumberTheory.get_cake_number(None, 22)
        expected = 1794
        self.assertEqual(result, expected, "Get Cake Number")

    def testLazyCaterer(self):
        instance = NumberTheory(24)
        result = NumberTheory.get_lazy_caterer(instance)
        expected = 301
        self.assertEqual(result, expected, "Get Lazy Caterer")
        result = NumberTheory.get_lazy_caterer(None, 22)
        expected = 254
        self.assertEqual(result, expected, "Get Lazy Caterer")

    def testBellNumber(self):
        instance = NumberTheory(20)
        result = NumberTheory.get_bell_number(instance)
        expected = 51724158235372
        self.assertEqual(result, expected, "Get Bells Number")
        result = NumberTheory.get_bell_number(None, 22)
        expected = 4506715738447323
        self.assertEqual(result, expected, "Get Bells Number")

    def testCenteredPolygonalNumber(self):
        # Instance holds the numbers of layers
        instance = NumberTheory(10)
        result = NumberTheory.get_centered_polygonal_number(instance, 10)
        expected = 551
        self.assertEqual(result, expected, "Get Centered Polygonal Number")


        result = instance.get_centered_polygonal_number(None,7, 10)
        expected = 386
        self.assertEqual(result, expected, "Get Centered Polygonal Number")

    def testGetPellList(self):
        instance = NumberTheory(12)
        result = NumberTheory.get_pell_list(instance)
        expected = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741]
        self.assertListEqual(expected, result, "Pell list should be equal")
        self.assertCountEqual(expected, result, "Pell count should be equal")

        result = NumberTheory.get_pell_list(None, 11)
        expected = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, ]
        self.assertListEqual(expected, result, "Pell list should be equal")
        self.assertCountEqual(expected, result, "Pell count should be equal")

    def testGetPell(self):
        instance = NumberTheory(15)
        result = NumberTheory.get_pell(instance)
        expected = 80782
        self.assertEqual(result, expected, "Get Pell")
        result = NumberTheory.get_pell(None, 17)
        expected = 470832
        self.assertEqual(result, expected, "Get Pell")

    def testGetJacobsthalList(self):
        instance = NumberTheory(15)
        result = NumberTheory.get_jacobsthal_list(instance)
        expected = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731]
        self.assertListEqual(expected, result, "Jacobsthal list should be equal")
        self.assertCountEqual(expected, result, "Jacobsthal count should be equal")

        result = NumberTheory.get_jacobsthal_list(None,14)
        expected = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365]
        self.assertListEqual(expected, result, "Jacobsthal list should be equal here")
        self.assertCountEqual(expected, result, "Jacobsthal count should be equal hers")

    def testGetJacobsthal(self):
        instance = NumberTheory(15)
        result = NumberTheory.get_jacobsthal(instance)
        expected = 2731
        self.assertEqual(result, expected, "Get Jacobsthal")
        result = NumberTheory.get_jacobsthal(None, 17)
        expected = 10923
        self.assertEqual(result, expected, "Get Jacobsthal")

    def testGetAlternatingFactorial(self):
        # instance = NumberTheory.NumberTheory(15)
        instance = NumberTheory(5)
        result = NumberTheory.get_alternating_factorial(instance)
        expected = 101
        self.assertEqual(result, expected, "Get Alternating Factorial")
        result = NumberTheory.get_alternating_factorial(None, 6)
        expected = 619
        self.assertEqual(result, expected, "Get Alternating Factorial")

    def testIsDeficient(self):
        instance = NumberTheory(15)
        self.assertTrue(NumberTheory.is_deficient(instance))
        self.assertTrue(NumberTheory.is_deficient(None, 9))

    def testIsSuperAbundant(self):
        instance = NumberTheory(360)
        self.assertTrue(NumberTheory.is_super_abundant(instance))
        self.assertTrue(NumberTheory.is_super_abundant(None, 1260))
        self.assertFalse(NumberTheory.is_super_abundant(None, 25))

    def testGetCullen(self):
        instance = NumberTheory(20)
        result = NumberTheory.get_cullen(instance)
        expected = 20971521
        self.assertEqual(result, expected, "Get Cullen Numbers")
        result = NumberTheory.get_cullen(None, 14)
        expected = 229377
        self.assertEqual(result, expected, "Get Cullen Numbers")

    def testCoPrime(self):
        instance = NumberTheory(18)
        self.assertTrue(NumberTheory.is_co_prime(instance,35), "CoPrime")
        self.assertTrue(NumberTheory.is_co_prime(None, 3, 20), "CoPrime")
        self.assertFalse(NumberTheory.is_co_prime(None, 150, 295), "CoPrime")

    def testCalculateCompositorial(self):
        instance = NumberTheory(9)
        result = NumberTheory.calculateCompositorial(instance)
        expected = 696729600
        self.assertEqual(result, expected, "Calculating Compositorial")
        result = NumberTheory.calculateCompositorial(None,9)
        expected = 696729600
        self.assertEqual(result, expected, "Calculating Compositorial")

    def testIsCurzon(self):
        instance = NumberTheory(4769)
        self.assertTrue(NumberTheory.is_curzon(instance))
        instance = NumberTheory(4770)
        self.assertFalse(NumberTheory.is_curzon(instance))
        self.assertTrue(NumberTheory.is_curzon(None,2109))
        self.assertFalse(NumberTheory.is_curzon(None,2119))

    def testGetTotatives(self):
        instance = NumberTheory(13)
        expected = NumberTheory.get_totatives(instance)
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertListEqual(expected, result, "Totatives list should be equal")
        self.assertCountEqual(expected, result, "Totatives count should be equal")
        expected = NumberTheory.get_totatives(instance, 20)
        result = [1, 3, 7, 9, 11, 13, 17, 19]
        self.assertListEqual(expected, result, "Totatives list should be equal")
        self.assertCountEqual(expected, result, "Totatives count should be equal")

    def testDePolignac(self):
        instance = NumberTheory(997)
        self.assertTrue(NumberTheory.is_de_polignac(None,959))
        self.assertTrue(NumberTheory.is_de_polignac(instance))
        self.assertFalse(NumberTheory.is_de_polignac(None,996))

    def testHappyNumbers(self):
        instance = NumberTheory(989)
        self.assertTrue(NumberTheory.is_happy(instance))
        instance.set_the_number(904)
        self.assertTrue(NumberTheory.is_happy(None, 1067))

    def testGetLuckyNumbers(self):
        instance = NumberTheory(15)
        result = NumberTheory.get_lucky_number_list(instance)
        """expected = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99, 105, 111,
                    115, 127, 129, 133, 135, 141, 151, 159, 163, 169, 171, 189, 193, 195, 201, 205, 211, 219, 223, 231,
                    235, 237, 241]
        """
        expected = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63]
        self.assertListEqual(expected, result, "Lucky numbers should be equal")
        self.assertCountEqual(expected, result, "Lucky number count should be equal")
        result = NumberTheory.get_lucky_number_list(None, 15)
        self.assertListEqual(expected, result, "Lucky numbers should be equal")
        self.assertCountEqual(expected, result, "Lucky number count should be equal")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
