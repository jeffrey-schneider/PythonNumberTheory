'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import unittest
from NumberTheory import *
from Primes import *


class Test(unittest.TestCase):


    def setUp(self):
        print("In method: ", self._testMethodName , " " , self._testMethodDoc)
        


    def tearDown(self):
        pass

    def testisEven(self):
        #instance = NumberTheory.NumberTheory(13)   
        instance = NumberTheory(13)
        instance.set_the_number(914)     
        self.assertTrue(instance.is_even())        
        #self.assertTrue(instance.is_even(12))
        
     
    def testIsAbundant(self):
        #instance = NumberTheory.NumberTheory(12)
        instance = NumberTheory(12)
        self.assertTrue(instance.is_abundant())
        self.assertTrue(instance.is_abundant(96))
        self.assertFalse(instance.is_abundant(95))
    
     
        
    def testGetNumber(self):
        instance = NumberTheory(15)                      
        instance.set_the_number(91)
        expected = 91
        result = instance.get_the_number()        
        self.assertEqual(result, expected)
        
        
    def testGetCollatz(self):
        instance = NumberTheory(5)
        expected = [5, 16, 8, 4, 2, 1]
        result = instance.get_collatz()
        self.assertListEqual(expected, result,"Collatz list should be equal")
        self.assertCountEqual(expected, result, "Collatz count should be equal")
     
    def testGetJugglers(self):   
        instance = NumberTheory(5)
        expected = [5, 11, 36, 6, 2, 1]
        result = instance.get_jugglers()
        self.assertListEqual(expected, result,"Jugglers list should be equal")
        self.assertCountEqual(expected, result, "Jugglers count should be equal")
        result = instance.get_jugglers(37)
        expected = [37, 225, 3375, 196069, 86818724, 9317, 899319, 852846071, 24906114455136, 4990602, 2233, 105519, 34276462, 5854, 76, 8, 2, 1]
        self.assertListEqual(expected, result,"Jugglers list should be equal")
        self.assertCountEqual(expected, result, "Jugglers count should be equal")
        
    def testGetPrimeFactors(self):
        instance = NumberTheory(3600)
        expected = [2, 2, 2, 2, 3, 3, 5, 5]
        result = instance.get_prime_factors()
        self.assertListEqual(expected, result,"Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors count should be equal")

    def testGetFactors(self):
        instance = NumberTheory(3600)
        expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36, 40, 45, 48, 50, 60, 72, 75, 80, 90, 100, 120, 144, 150, 180, 200, 225, 240, 300, 360, 400, 450, 600, 720, 900, 1200, 1800, 3600 ]
        result = instance.get_factors()
        self.assertListEqual(expected, result,"Factors list should be equal")
        self.assertCountEqual(expected, result, "Factors count should be equal")

    def testAliquotSum(self):
        instance = NumberTheory(60)
        expected = 108
        result = instance.get_aliquot_sum()
        self.assertEqual(result, expected, "Aliquot sum()")
        
    def testGetReverseNumber(self):
        instance = NumberTheory(34)
        result = instance.get_reverse_number()
        expected = 43
        self.assertEqual(result, expected, "Reversed Number")
        result = instance.get_reverse_number(95)
        expected = 59
        self.assertEqual(result, expected, "Reversed Number")
     
    def testGetReciprocalNumber(self):
        instance = NumberTheory(43)
        result = instance.get_reciprocal_number()
        expected =  0.023255813953488372
        self.assertAlmostEqual(result, expected, 7, "Reciprocal Number", delta=None)  
        result = instance.get_reciprocal_number(4)
        expected =  0.25
        self.assertAlmostEqual(result, expected, 7, "Reciprocal Number", delta=None)
        
        
    def testGetHex(self):
        instance = NumberTheory(76576500)
        result = instance.get_hex()
        expected = "49076F4"
        self.assertEqual(result, expected, "Get Hex")
        result = instance.get_hex(84)
        expected = "54"
        self.assertEqual(result, expected, "Get Hex")
    
    def testGetOctal(self):
        instance = NumberTheory(76576500)
        result = instance.get_octal()
        expected = "444073364"
        self.assertEqual(result, expected, "Get Octal")
        result = instance.get_octal(76576501)
        expected = "444073365"
        self.assertEqual(result, expected, "Get Octal")
        
    
    def testGetBinary(self):  
        instance = NumberTheory(76576500)
        result = instance.get_binary()
        expected = "100100100000111011011110100"
        self.assertEqual(result, expected, "Get Hex")
        result = instance.get_binary(845)
        expected = "1101001101"
        self.assertEqual(result, expected, "Get Hex")
   
    def testIsPerfect(self):
        instance = NumberTheory(8128)        
        self.assertTrue(instance.is_perfect())
        self.assertTrue(instance.is_perfect(496))
        self.assertFalse(instance.is_perfect(495))
        
    def testGetSigma(self):
        instance = NumberTheory(9)
        result = instance.get_sigma()
        expected = 13
        self.assertEqual(result, expected, "Get Sigma")
        result = instance.get_sigma(15)
        expected = 24
        self.assertEqual(result, expected, "Get Sigma")
        
    def testGetKynea(self):
        instance = NumberTheory(5)
        result = instance.get_kynea()
        expected = 1087
        self.assertEqual(result, expected, "Get Kynea")
        result = instance.get_kynea(6)
        expected = 4223
        self.assertEqual(result, expected, "Get Kynea")
        
    def testGetCarol(self):
        instance = NumberTheory(7)
        result = instance.get_carol()
        expected = 16127
        self.assertEqual(result, expected, "Get Carol")
        self.assertEqual(65023, instance.get_carol(8), "Get Carol")   
        self.assertNotEqual(615023, instance.get_carol(7), "Get Carol")
        
        
    def testGetFactorials(self):
        instance = NumberTheory(10)
        result = instance.get_factorial()
        expected = 3628800
        self.assertEqual(result, expected, "Get Factorial")
        result = instance.get_factorial(12)
        expected = 479001600
        self.assertEqual(result,expected,"Get Factorial")
        
    def testGetCatalan(self):
        instance = NumberTheory(20)
        result = instance.get_catalan()
        expected = 6564120420
        self.assertEqual(result, expected, "Get Catalan")
        result = instance.get_catalan(10)
        expected = 16796
        self.assertEqual(result, expected, "Get Catalan")
        
    def testGetFibonacciList(self):
        instance = NumberTheory(20)
        result = instance.get_fibonacci_list()
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        self.assertListEqual(expected, result,"Fibonacci list should be equal")
        self.assertCountEqual(expected, result, "Fibonacci count should be equal")
        result = instance.get_fibonacci_list(15)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        self.assertListEqual(expected, result,"Fibonacci list should be equal")
        self.assertCountEqual(expected, result, "Fibonacci count should be equal")
        
    def testGetMotzkin(self):
        instance = NumberTheory(20)
        result = instance.get_motzkin()
        expected = 50852019
        self.assertEqual(result, expected, "Get Motzkin")
        result = instance.get_motzkin(15)
        expected = 310572
        self.assertEqual(result, expected, "Get Motzkin")
        
    def testGetLucas(self):
        instance = NumberTheory(12)
        result = instance.get_lucas_list()
        expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199,]
        self.assertListEqual(expected, result,"Lucas list should be equal")
        self.assertCountEqual(expected, result, "Lucas count should be equal")
        result = instance.get_lucas_list(33)
        expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364,
                    2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079, 103682, 167761, 271443, 439204, 710647, 1149851,
                    1860498, 3010349, 4870847,]        
        self.assertListEqual(expected, result,"Lucas list should be equal")
        self.assertCountEqual(expected, result, "Lucas count should be equal")
        

    def testPrimitiveAbundant(self):
        instance = NumberTheory(7532)        
        self.assertTrue(instance.is_primitive_abundant())
        self.assertTrue(instance.is_primitive_abundant(3606))
        instance = NumberTheory(2801)
        self.assertFalse(instance.is_primitive_abundant())
        self.assertFalse(instance.is_primitive_abundant(3607))
    
    def testSuperAbundant(self):
        instance = NumberTheory(1260)
        self.assertTrue(instance.is_super_abundant())
        
    def testIsAKeithNumber(self):
        instance = NumberTheory(1104)
        self.assertTrue(instance.is_keith_number())
        self.assertTrue(instance.is_keith_number(7913837))
        self.assertFalse(instance.is_keith_number(7913838))
        
    
    def testAmicableNumber(self):
        instance = NumberTheory(220)
        result = instance.get_amicable_number()
        expected = 284
        self.assertEqual(result, expected, "Get Amicable")
        result = instance.get_amicable_number(12285)
        expected = 14595
        self.assertEqual(result, expected, "Get Amicable")
        
        
    def testBetrothedNumbers(self):
        instance = NumberTheory(9504)        
        result = instance.get_betrothed_number()
        expected = 20735
        self.assertEqual(result, expected, "Get Betrothed")
        result = instance.get_betrothed_number(1050)
        expected = 1925
        self.assertEqual(result, expected, "Get Betrothed")
        
    def testCakeNumbers(self):
        instance = NumberTheory(24)
        result = instance.get_cake_number()
        expected = 2325
        self.assertEqual(result, expected, "Get Cake Number")
        result = instance.get_cake_number(22)
        expected = 1794
        self.assertEqual(result, expected, "Get Cake Number")
        
    def testLazyCaterer(self):
        instance = NumberTheory(24)
        result = instance.get_lazy_caterer()
        expected = 301
        self.assertEqual(result, expected, "Get Lazy Caterer")
        result = instance.get_lazy_caterer(22)
        expected = 254
        self.assertEqual(result, expected, "Get Lazy Caterer")
     
    def testBellNumber(self):
        instance = NumberTheory(20)
        result = instance.get_bell_number()
        expected = 51724158235372
        self.assertEqual(result, expected, "Get Bells Number")
        result = instance.get_bell_number(22)
        expected = 4506715738447323
        self.assertEqual(result, expected, "Get Bells Number")
        
    def testCenteredPolygonalNumber(self):
        instance = NumberTheory(20)
        result = instance.get_centered_polygonal_number(3,2)
        expected = 10
        self.assertEqual(result, expected, "Get Centered Polygonal Number")
        
        result = instance.get_centered_polygonal_number(14)
        expected = 2941
        self.assertEqual(result, expected, "Get Centered Polygonal Number")
        
    def testGetPellList(self):
        instance = NumberTheory(12)
        result = instance.get_pell_list()
        expected = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741]
        self.assertListEqual(expected, result,"Pell list should be equal")
        self.assertCountEqual(expected, result, "Pell count should be equal")
        result = instance.get_pell_list(11)
        expected = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378,]
        self.assertListEqual(expected, result,"Pell list should be equal")
        self.assertCountEqual(expected, result, "Pell count should be equal")

        
    def testGetPell(self):
        instance = NumberTheory(15)
        result = instance.get_pell()
        expected = 80782
        self.assertEqual(result, expected, "Get Pell")        
        result = instance.get_pell(17)
        expected = 470832
        self.assertEqual(result, expected, "Get Pell")        
        
    def testGetJacobsthalList(self):
        instance = NumberTheory(15)
        result = instance.get_jacobsthal_list()
        expected = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731]
        self.assertListEqual(expected, result,"Jacobsthal list should be equal")
        self.assertCountEqual(expected, result, "Jacobsthal count should be equal")
        result = instance.get_jacobsthal_list(14)
        expected = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365]
        self.assertListEqual(expected, result,"Jacobsthal list should be equal")
        self.assertCountEqual(expected, result, "Jacobsthal count should be equal")
    
    def testGetJacobsthal(self):
        instance = NumberTheory(15)
        result = instance.get_jacobsthal()
        expected = 2731
        self.assertEqual(result, expected, "Get Jacobsthal")        
        result = instance.get_jacobsthal(17)
        expected = 10923
        self.assertEqual(result, expected, "Get Jacobsthal")        
           
    def testGetAlternatingFactorial(self):
        #instance = NumberTheory.NumberTheory(15)
        instance = NumberTheory(15)
        result = instance.get_alternating_factorial()
        expected = 1226280710981
        self.assertEqual(result, expected, "Get Alternating Factorial")
        result = instance.get_alternating_factorial(21)
        expected = 48773618881154822981
        self.assertEqual(result, expected, "Get Alternating Factorial")

    def testIsDeficient(self):
        instance = NumberTheory(15)
        self.assertTrue(instance.is_deficient())
        self.assertTrue(instance.is_deficient(9))

    def testIsSuperAbundant(self):
        instance = NumberTheory(360)
        self.assertTrue(instance.is_super_abundant())
        self.assertTrue(instance.is_super_abundant(1260))
        self.assertFalse(instance.is_super_abundant(25))
    
    def testGetCullen(self):    
        instance = NumberTheory(20)
        result = instance.get_cullen()
        expected = 20971521
        self.assertEqual(result, expected, "Get Cullen Numbers")
        result = instance.get_cullen(14)
        expected = 229377
        self.assertEqual(result, expected, "Get Cullen Numbers")
    
    def testCoPrime(self):   
        instance = NumberTheory(18)
        self.assertTrue(instance.is_co_prime(35), "CoPrime")
        self.assertFalse(instance.is_co_prime(150, 295), "CoPrime")
     
    def testCalculateCompositorial(self):
        instance = NumberTheory(9)
        result = instance.calculateCompositorial()
        expected = 696729600
        self.assertEqual(result, expected, "Calculating Compositorial")
        result = instance.calculateCompositorial(9)
        expected = 696729600
        self.assertEqual(result, expected, "Calculating Compositorial")
    
    def testIsCurzon(self):
        instance = NumberTheory(4769)
        self.assertTrue(instance.is_curzon())
        instance = NumberTheory(4770)
        self.assertFalse(instance.is_curzon())
        self.assertTrue(instance.is_curzon(2109))
        self.assertFalse(instance.is_curzon(2119))
     
    def testGetTotatives(self):
        instance = NumberTheory(13)
        expected = instance.get_totatives()
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertListEqual(expected, result,"Totatives list should be equal")
        self.assertCountEqual(expected, result, "Totatives count should be equal")
        expected = instance.get_totatives(20)
        result = [1, 3, 7, 9, 11, 13, 17, 19]           
        self.assertListEqual(expected, result,"Totatives list should be equal")
        self.assertCountEqual(expected, result, "Totatives count should be equal")
        
    def testDePolignac(self):
        instance = NumberTheory(997)
        self.assertTrue(instance.is_de_polignac())
        self.assertTrue(instance.is_de_polignac(959))
        self.assertFalse(instance.is_de_polignac(996))

    def testHappyNumbers(self):
        instance = NumberTheory(989)        
        self.assertTrue(instance.is_happy())
        instance.set_the_number(904)
        self.assertTrue(instance.is_happy(1067))


        
    @unittest.skip("Not ready for testing.")
    def testGetLuckyNumbers(self):
        instance = NumberTheory(150)
        result = instance.get_lucky_number_list()
        expected = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99, 105, 111, 115, 127, 129, 133, 135, 141, 151, 159, 163, 169, 171, 189, 193, 195, 201, 205, 211, 219, 223, 231, 235, 237, 241]        
        self.assertListEqual(expected, result, "Lucky numbers should be equal")
        self.assertCountEqual(expected, result, "Lucky number cound should be equal")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


