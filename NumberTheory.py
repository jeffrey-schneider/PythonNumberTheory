'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import math
import functools
# from fontTools.misc.textTools import num2binary
# from pkg_resources import _sset_none, _sget_none
# from tkinter.constants import FALSE
from collections import deque
from typing import override, List, Any

# from test.test_itertools import isEven, isOdd
# import Primes


ITERATIONS = 1000


def get_sum_of_squares(vList: list[int]) -> int:
    retVal = 0
    for v in vList:
        retVal += v * v
    return retVal


class NumberTheory:

    def __init__(self, theNumber: int) -> None:
        self.__theNumber = theNumber

    def set_the_number(self, theNumber: int) -> None:
        self.__theNumber = theNumber

    def get_the_number(self) -> int:
        return self.__theNumber

    @staticmethod
    def get_square(self=None, v: int = None) -> int:
        if v is None:
            v = self.get_the_number()
        return v * v

    @staticmethod
    def get_cube(self=None, v: int = None) -> int:
        if v is None:
            v = self.get_the_number()
        return v * v * v

    @staticmethod
    def get_product_of_squares(vList) -> int:
        retVal = 0
        for the_int in vList:
            retVal *= the_int * the_int
        return retVal

    @staticmethod
    def get_sum_of_digits(aList) -> int:
        retVal = 0
        for integer in aList:
            retVal += integer
        return retVal

    @staticmethod
    def get_product_of_digits(aList) -> int:
        retVal = 0
        for integer in aList:
            retVal *= integer
        return retVal

    @staticmethod
    def number_to_list(the_number) -> list[int]:
        '''
        Split an integer into a list of the digits
        '''
        retVal = deque([])
        string = str(the_number)
        for i in string:
            retVal.appendleft(int(i))
        return list(retVal)

    @staticmethod
    def get_list_of_digits(self=None, v: int = None) -> list[int]:
        '''
        Usage: provide java getListOfDigits() equivalency
        '''
        if v is None:
            v = self.get_the_number()
        return NumberTheory.number_to_list(v)

    '''
    Return sum of a list
    aka sigma of a list
    '''

    @staticmethod
    def sum_of_list(the_Collection) -> int:
        total = 0
        [total := total + x for x in the_Collection]
        return total

    @staticmethod
    def multiple_of_list(the_Collection) -> int:
        total = 1
        [total := total * x for x in the_Collection]
        return total

    @staticmethod
    def is_prime(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        stopVal = int(math.sqrt(v))
        i = 2
        while i <= stopVal:
            if v % i == 0:
                return False
            i += 1
        return True

    @staticmethod
    def get_collatz(self=None, v: int = None) -> list[int]:
        retVal = []
        if v is None:
            v = self.get_the_number()
        retVal.append(int(v))
        counter = int(v)
        while counter > 1:
            if counter % 2 == 0:
                counter /= 2;
                counter = int(counter)
            else:
                counter = int(math.floor(3.0 * counter + 1))
            retVal.append(counter)
        return retVal

    @staticmethod
    def get_jugglers(self=None, v=None) -> list[int]:
        retVal = []
        if v is None:
            v = self.get_the_number()
        retVal.append(v)
        counter = v
        while counter > 1:
            if counter % 2 == 0:
                factr = .5
            else:
                factr = 1.5
            counter = int(math.floor(math.pow(counter, factr)))
            retVal.append(counter)
        return retVal

    """ Starting to modify code to use list comprehensions"""

    @staticmethod
    def get_factors(self=None, v: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        return [i for i in range(1, v + 1) if v % i == 0]

    """
    This could have been done with SUM, but then I wouldn't have 
    learned about list comprehensions
    """

    @staticmethod
    def factors_generator(n: int) -> List[int]:
        for i in range(1, n + 1):
            if n % i == 0:
                yield i

    @staticmethod
    def get_factors_sum(self=None, v: int = None) -> int:
        total = 0
        if v is None:
            v = self.get_the_number()
        total_list = NumberTheory.factors_generator(v)
        return NumberTheory.sum_of_list(total_list)

    """
    @author: Jeffrey Schneider    
    Sum of all proper divisors (factors) except itself, hence the subtraction.
    """

    @staticmethod
    def get_aliquot_sum(self=None, v: int = None) -> int:
        total = 0
        if v is None:
            v = self.get_the_number()
        total_list = NumberTheory.factors_generator(v)
        return NumberTheory.sum_of_list(total_list) - v

    @staticmethod
    def get_reverse_number(self=None, v=None) -> int:
        rev = 0
        digit = 0
        if v is None:
            num = self.get_the_number()
        else:
            num = v
        while num != 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10
        return rev

    @staticmethod
    def get_reciprocal_number(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return 1.0 / v

    @staticmethod
    def get_hex(self=None, v=None) -> str:
        retVal = ""
        hexList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        rem = 0
        if v is None:
            buffer = self.get_the_number()
        else:
            buffer = v
        while buffer > 0:
            rem = buffer % 16
            retVal = hexList[rem] + retVal
            buffer //= 16
        return retVal

    @staticmethod
    def get_octal(self=None, v=None) -> str:
        retVal = ""
        dlg = ["0", "1", "2", "3", "4", "5", "6", "7"]
        rem = 0
        if v is None:
            buffer = self.get_the_number()
        else:
            buffer = v
        while buffer > 0:
            rem = buffer % 8
            retVal = dlg[rem] + retVal
            buffer //= 8
        return retVal

    @staticmethod
    def get_binary(self=None, v=None) -> str:
        if v is None:
            v = self.get_the_number()
        retVal = '{0:b}'.format(v)
        return retVal

    @staticmethod
    def is_abundant(self=None, v: int = None) -> bool:
        """
        Boolean.
        Is the number's aliquot sum greater than the number?
        """
        if v is None:
            v = self.get_the_number()
        return NumberTheory.get_aliquot_sum(None, v) > v

    @staticmethod
    def get_proper_divisors(self=None, v=None) -> list[int]:
        retVal = []
        if v is None:
            v = self.get_the_number()
        for i in range(1, v + 1):
            if v % i == 0:
                retVal.append(i)
        return retVal

    @staticmethod
    def get_abundance(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return NumberTheory.get_aliquot_sum(None, v) - v

    @staticmethod
    def is_even(self=None, v: int = None) -> bool:
        if v is None:
            v = self.get_the_number()
        return v % 2 == 0

    @staticmethod
    def is_perfect(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        return NumberTheory.get_abundance(None, v) == 0

    @staticmethod
    def get_kynea(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()

        kyneaA = math.pow(4.0, v)
        kyneaB = math.pow(2.0, v + 1.0)
        kyneaFinal = kyneaA + kyneaB - 1.0
        return int(kyneaFinal)

    @staticmethod
    def get_carol(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        carolA = math.pow(4.0, v)
        carolB = math.pow(2.0, v + 1)
        carolFinal = carolA - carolB - 1.0
        return int(carolFinal)

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * NumberTheory.factorial(n - 1)

    # @functools.cache
    @staticmethod
    def get_factorial(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return NumberTheory.factorial(v)

    @staticmethod
    def get_sigma(self: object = None, v: object = None) -> int:
        if v is None:
            v = self.get_the_number()
        if v == 1:
            return 1
        result = 0
        the_total = sum(x for x in range(1, v + 1) if v % x == 0)
        return the_total

    @staticmethod
    def get_catalan(self=None, v: int = None) -> int:
        if v is None:
            v = self.get_the_number()
        catA = NumberTheory.get_factorial(None, 2 * v)
        catB = NumberTheory.get_factorial(None, v + 1)
        catC = NumberTheory.get_factorial(None, v)
        catFinal = catA / (catB * catC);
        return catFinal

    @staticmethod
    def get_fibonacci_list(self=None, v: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        num1 = 0
        num2 = 1
        counter = 0
        retList = []
        while counter < v:
            retList.append(num1)
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            counter += 1
        return retList

    def get_fibonacci_like(self=None, v: int = None, number1: int = None, number2: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        if number1 == None:
            num1 = 1
        else:
            num1 = number1
        if number2 == None:
            num2 = 1
        else:
            num2 = number2
        num3 = 0
        retList = []
        while num1 <= v:
            retList.append(num1)
            num3 = num2 + num1
            num1 = num2
            num2 = num3
        return retList

    def isFiboDiv(self=None, v: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        for i in range(1, len(v)):
            left = v[:i]
            right = v[i:]
            print(left, " ", right)
            return self.get_fibonacci_like(None, v, left, right)

    # sb = []
    # sb.append(v)
    # left = 0
    # right = 0
    # for i in range(1,len(sb)+1):
    #    left =

    def get_lucas_list(self, v=None) -> list[int]:
        retList = []
        if v is None:
            v = self.get_the_number()
        num1 = 2;
        num2 = 1;
        counter = 0

        while counter < v:
            retList.append(num1)
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            counter += 1
        return retList

    @staticmethod
    def get_motzkin(self=None, v=None):
        memo = {}

        if v is None:
            v = self.get_the_number()

        if (v == 0) or (v == 1):
            return 1

        if v in memo:
            return memo.get(v)

        m1 = NumberTheory.get_motzkin(None, v - 1)
        m2 = NumberTheory.get_motzkin(None, v - 2)

        firstPart = (2 * v + 1) * m1
        secondPart = (3 * v - 3) * m2
        lastPart = v + 2
        retVal = (firstPart + secondPart) / lastPart
        memo[v] = retVal

        return retVal

    @staticmethod
    def is_primitive_abundant(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        properDivisorList = []

        if not NumberTheory.is_abundant(None, v):
            return False
        else:
            properDivisorList = NumberTheory.get_factors(None, v)
            ''' get_factors includes the number at the end.  We don't want the number included, lets pop() it off'''
            properDivisorList.pop()
            for i in properDivisorList:
                if NumberTheory.is_abundant(None, i):
                    return False
        return True

    '''
    @author: Jeffrey Schneider
    @see https://www.youtube.com/watch?v=uuMwz47LV_w
    '''

    @staticmethod
    def is_keith_number(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        buffer_sum_of_digits = 0
        # list_of_digits is a deque
        #list_of_digits = NumberTheory.number_to_list(v)
        list_of_digits = deque(NumberTheory.number_to_list(v))
        while buffer_sum_of_digits < v:
            buffer_sum_of_digits = NumberTheory.sum_of_list(list_of_digits)
            if buffer_sum_of_digits == v:
                return True
            list_of_digits.appendleft(buffer_sum_of_digits)
            list_of_digits.pop()  # Throw away this value
        return False

    @staticmethod
    def get_amicable_number(self, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        first_divisor_sum = NumberTheory.get_aliquot_sum(None, v)
        second_divisor_sum = NumberTheory.get_aliquot_sum(None, first_divisor_sum)
        if second_divisor_sum == v:
            return first_divisor_sum

    @staticmethod
    def get_betrothed_number(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        thisNumber = NumberTheory.sum_of_list(NumberTheory.get_non_trivial_divisors(None, v))
        thatNumber = NumberTheory.sum_of_list(NumberTheory.get_non_trivial_divisors(None, thisNumber))
        if thatNumber == v:
            return thisNumber
        return 0

    @staticmethod
    def get_non_trivial_divisors(self=None, v=None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        my_list = sorted(NumberTheory.get_factors(None, v))
        my_list = my_list[1:-1]
        return my_list

    @staticmethod
    def get_cake_number(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return int((1.0 / 6.0) * (pow(v, 3) + 5 * v + 6))

    '''https://codereview.stackexchange.com/questions/12119/printing-nth-bell-number'''

    @staticmethod
    def get_bell_number(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return (1 / math.e) * sum([(k ** v) / (math.factorial(k)) for k in range(ITERATIONS)])

    @staticmethod
    def get_centered_polygonal_number(self=None, sideNumber=None, layers=None) -> int:
        if layers is None:
            layers = self.get_the_number()
        return int(sideNumber * layers * (layers + 1) / 2 + 1)

    @staticmethod
    def get_polygonal_number(self=None, sides=None, layers=None) -> int:
        if sides == None:
            sides = self.get_the_number()
        if layers == None:
            layers = 10
        s_minus_two = sides - 2
        s_minus_four = sides - 4
        return (1 / 2.0) * (s_minus_two * pow(layers, 2.0) - s_minus_four * layers);

    @staticmethod
    def get_primorial(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        summary = 1
        counter = 1
        number_of_primes = 0
        while number_of_primes <= v:
            if NumberTheory.is_prime(None, counter):
                summary *= counter
                number_of_primes += 1
            counter += 1
        return summary

    @staticmethod
    def get_pell_list(self=None, v=None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        num1 = 0
        num2 = 1
        counter = 0
        retList = []
        while counter < v:
            retList.append(num1)
            num3 = 2 * num2 + num1
            num1 = num2
            num2 = num3
            counter += 1
        return retList

    @staticmethod
    def get_pell(self=None, v: int = None) -> list[int]:
        theList = []
        if v is None:
            v = self.get_the_number()
        theList = NumberTheory.get_pell_list(None, v)
        theStack = [x for x in theList]
        return theStack.pop()

    @staticmethod
    def get_jacobsthal_list(self=None, v=None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        theList = []
        num1 = 0
        num2 = 1
        counter = 1
        while counter < v:
            theList.append(num1)
            num3 = num2 + 2 * num1
            num1 = num2
            num2 = num3
            counter += 1
        return theList

    @staticmethod
    def get_jacobsthal(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        theList = []
        theList = NumberTheory.get_jacobsthal_list(None, v)
        theStack = [x for x in theList]
        return theStack.pop()

    @staticmethod
    def get_alternating_factorial(self=None, v: int = None):
        if v is None:
            v = self.get_the_number()
        total = 0
        sign = 1  #Start wtih positive sign
        for i in range(v, 0, -1):
            total += sign * NumberTheory.factorial(i)
            sign *= -1  #Alternate the sign
        return total

    @staticmethod
    def get_alternating_factorial02(self=None, v: int = None):
        if v is None:
            v = self.get_the_number()
        theDictionary = {}
        theDictionary[1] = 1
        theDictionary[2] = 1
        for i in range(3, v + 1):
            theDictionary[i] = self.get_factorial(None, i) - theDictionary[i - 1]
        return theDictionary.get(v)

    @staticmethod
    def is_deficient(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        return NumberTheory.get_aliquot_sum(None, v) < v

    @staticmethod
    def is_super_abundant(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        M = 0.0
        N = NumberTheory.get_sigma(None, v) / v
        for i in range(1, v):
            M = NumberTheory.get_sigma(None,i) / i
        if M >= N:
            return False
        return True

    @staticmethod
    def gcd(b, n) -> int:
        if n == 0:
            return b
        return NumberTheory.gcd(n, b % n)

    @staticmethod
    def lcm(self=None, a=None, b=None) -> int:
        if b == None:
            b = self.get_the_number()
        return a * (b / NumberTheory.gcd(a, b))

    @staticmethod
    def power(self, b, exp, n) -> float:
        if exp == 0:
            return 1
        result = self.power(b, exp / 2, n) % n
        result = (result * result) % n
        if exp % 2 == 1:
            result = (result * b) % n
        return result

    @staticmethod
    def is_carmichael(self, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        for b in range(2, v + 1):
            if (self.gcd(b, v) == 1) and (self.power(b, v - 1, v) != 1):
                return False
        return True

    @staticmethod
    # Function to find the N-th
    # icosikaipentagon number
    def isDNum(self, n) -> bool:
        if n == None:
            n = self.get_the_number()
        # number should be
        # greater than 3
        if n < 4:
            return False

        # Check every k in range 2 to n-1
        for k in range(2, n):
            numerator = pow(k, n - 2) - k
            # print("Numerator: " , numerator)
            hcf = math.gcd(n, k)

            # condition for D-Number
            if (hcf == 1 and (numerator % n) != 0):
                return False
        return True

    @staticmethod
    def get_lazy_caterer(self, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return (v * v + v + 2) / 2

    @staticmethod
    def get_cullen(self, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        return v * math.pow(2, v) + 1

    @staticmethod
    def is_co_prime(self=None, bNumber=None, v=None) -> bool:
        if bNumber is None:
            bNumber = self.get_the_number()
        if v is None:
            v = self.get_the_number()

        if NumberTheory.gcd(bNumber, v) == 1:
            return True
        return False

    @staticmethod
    # https://www.geeksforgeeks.org/compositorial-of-a-number/
    # Python3 program to find Compositorial
    # of composite numbers

    # Function to check
    # if a number is composite.
    def isComposite(self=None, n=None) -> bool:
        if n == None:
            n = self.get_the_number()
        # Corner cases
        if (n <= 3):
            return False

        # This is checked so that we can
        # skip the middle five numbers
        # in the below loop
        if (n % 2 == 0 or n % 3 == 0):
            return True
        i = 5
        while (i * i <= n):
            if (n % i == 0 \
                    or n % (i + 2) == 0):
                return True
            i = i + 6

        return False

    @staticmethod
    # This function stores all
    # Composite numbers less than N
    def Compositorial_list(self=None, n=None) -> list[int]:
        if n == None:
            n = self.get_the_number()
        myList = []
        l = 0
        for i in range(4, 10 ** 6):
            if l < n:
                if NumberTheory.isComposite(None, i):
                    myList.append(i)
                    l += 1
        return myList

    @staticmethod
    # Function to calculate the
    # Compositorial of n
    def calculateCompositorial(self=None, n=None):
        if n == None:
            n = self.get_the_number()
        total = 1
        myList = NumberTheory.Compositorial_list(None, n)
        return NumberTheory.multiple_of_list(myList)

    @staticmethod
    def is_curzon(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        a = 2 ** v + 1
        b = 2 * v + 1
        return a % b == 0

    @staticmethod
    def get_totatives(self=None, v=None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        retList = []
        counter = 1
        while counter <= v:
            if NumberTheory.is_co_prime(None, v, counter):
                retList.append(counter)
            counter += 1
        return retList

    @staticmethod
    def eulersPhi(self=None, v=None) -> int:
        if v is None:
            v = self.get_the_number()
        result = 1
        for i in range(2, v):
            if NumberTheory.gcd(i, v) == 1:
                result += 1
        return result

    @staticmethod
    def is_de_polignac(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        if not NumberTheory.is_even(None, v):
            for p in range(1, v):
                if NumberTheory.is_prime(None, p):
                    for k in range(1, p):
                        if v - p == 2 ** k:
                            return False
            return True
        return False

    @staticmethod
    def is_odd(self=None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        return v % 2 != 0

    @staticmethod
    def is_happy(self=None, v=None) -> bool:
        the_set = set([])
        if v is None:
            v = self.get_the_number()
        a = get_sum_of_squares(NumberTheory.get_list_of_digits(None, v))
        while a != 1:
            a = get_sum_of_squares(NumberTheory.get_list_of_digits(None, a))
            if a in the_set:
                return False
            the_set.add(a)
        return True

    @staticmethod
    def get_lucky_number_list(self=None, v=None):
        if v is None:
            v = self.get_the_number()
        '''https://www.w3resource.com/python-exercises/math/python-math-exercise-17.php'''
        the_list = range(-1, v * v + 9, 2)
        i = 2
        while the_list[i:]:
            the_list = sorted(set(the_list) - set(the_list[the_list[i]::the_list[i]]));
            i += 1
        #print(the_list[1:v + 1])
        return (the_list[1:v + 1])

    # Line 3544 from NumberTheory.java

    def get_double_factorial(self):
        pass

    def get_rep_unit(self):
        pass

    def is_honaker_prime(self):
        pass

    def get_ormiston(self):
        pass

    def split_the_number_in_two(self):
        pass

    def get_dicksons_method(self):
        pass

    def get_factor_pairs(self):
        pass

    def get_divisor_function(self):
        pass

    def get_fermat_primes(self):
        pass

    def get_junction_numbers(self):
        pass

    def get_pell_list02(self):
        pass

    def get_powerful_number(self):
        pass

    def get_pronic(self):
        pass

    def permute(self):
        pass

    def get_leyland(self):
        pass

    def get_saint_exupery(self):
        pass

    def get_string_list_of_digits(self):
        pass

    def is_achilles(self):
        pass

    def is_admirable(self):
        pass

    def is_alternating(self):
        pass

    def is_amenable(self):
        pass

    staticmethod

    def the_queue() -> None:
        queue = []
        theList = NumberTheory.get_factors(None, 3600)
        for i in theList:
            queue.append(i)
        while len(queue) > 0:
            print(queue.pop(), end=' ')
        print()

    @staticmethod
    def sum_of_factors(self=None, v: int = None) -> int:
        # Get the list of factors
        factors = NumberTheory.get_factors(v)
        # Calculate the sum of factors
        total_sum = sum(factors)
        return total_sum

    '''
    def is_antiperfect(self, v=None):        
        if v is None:
            v = self.get_the_number
        the_list = self.get_factors(v)
        last_element = len(the_list) - 1
        list.remove(last_element)
        sum = 0
        for int in the_list:
            sum += self.get_reverse_number(int)

        if sum == v:
            return True
        return False
    '''

    ''' 
    def get_partition_number(self, v=None) -> int:
        pass
        # Create a list to store the partition numbers
        partitions = [0] * (v + 1)
        partitions[0] = 1  # Base case p(0) = 1

        # Calculatte partition numbers for each number from 1 to n
        for i in range(1, v + 1):
            for j in range(i, v + 1):
                partitions[j] += partitions[j - i]

        return partitions[v]
    '''

    def isApocalyptic(self):
        pass

    def isArithmetic(self):
        pass

    def isAstonishing(self):
        pass

    def isAutomorphic(self):
        pass

    def isBalancedPrime(self):
        pass

    def isCanadaNumber(self):
        pass

    def isCarmichael(self):
        pass

    def isCurzon(self):
        pass

    def isCyclic(self):
        pass

    def isDNumber(self):
        pass

    def isDPowerful(self):
        pass

    def isDeceptive(self):
        pass

    def isDeficient(self):
        pass

    def isDicksonsMethod(self):
        pass

    def isDigitsSorted(self):
        pass

    def isDivisibleBy(self):
        pass

    def isDroll(self):
        pass

    def isDuffinian(self):
        pass

    def isEconomical(self):
        pass

    def isEnlightened(self):
        pass

    def isEquidigital(self):
        pass

    def isEsthetic(self):
        pass

    def isEven(self):
        pass

    def isEvil(self):
        pass

    def isFiboDiv(self):
        pass

    def isFrugal(self):
        pass

    def isGapful(self):
        pass

    def isGilda(self):
        pass

    def isGiuga(self):
        pass

    def isHappy(self):
        pass

    def isHarmonicDivisorNumber(self):
        pass

    def isHarshad(self):
        pass

    def isHighlyComposite(self):
        pass

    def isHoaxNumber(self):
        pass

    def isHungry(self):
        pass

    def isHyperPerfect(self):
        pass

    def isIdoneal(self):
        pass

    def isInsolite(self):
        pass

    def isKaprekar(self):
        pass

    def isKatadrome(self):
        pass

    def isLynchBell(self):
        pass

    def isMagnanimous(self):
        pass

    def isMetadrome(self):
        pass

    def isModest(self):
        pass

    def isMoran(self):
        pass

    def isNarcissistic(self):
        pass

    def isNude(self):
        pass

    def isPalPrime(self):
        pass

    def isPalindromic(self):
        pass

    def isPerfect(self):
        pass

    def isPerfectPower(self):
        pass

    def isPernicious(self):
        pass

    def isPoulet(self):
        pass

    def isPowerOfTwo(self):
        pass

    def isPowerful(self):
        pass

    def isPractical(self):
        pass

    def isPrimitiveAbundant(self=None, v: int = None):
        pass

    def isPrimitiveAbundantBkup(self=None, v: int = None):
        pass

    def isPronic(self):
        pass

    def isProthNumber(self):
        pass

    def isRare(self):
        pass

    def isSastry(self):
        pass

    def isSastry(self):
        pass

    def isSphenic(self):
        pass

    def isSquareFree(self):
        pass

    def isSuperD(self):
        pass

    def isSuperabundant(self):
        pass

    def getHarmonicMean(self):
        pass

    def getPolygonalNumber(self):
        pass

    def getReciprocalNumber(self):
        pass

    def abs(self):
        pass

    ##################################################################
    def get_end_point(self, lat1, lon1, bearing, d):
        R = 6371  # Radius of the Earth
        brng = math.radians(bearing)  # convert degrees to radians
        d = d * 1.852  # convert nautical miles to km
        lat1 = math.radians(lat1)  # Current lat point converted to radians
        lon1 = math.radians(lon1)  # Current long point converted to radians
        lat2 = math.asin(math.sin(lat1) * math.cos(d / R) + math.cos(lat1) * math.sin(d / R) * math.cos(brng))
        lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(lat1),
                                 math.cos(d / R) - math.sin(lat1) * math.sin(lat2))
        lat2 = math.degrees(lat2)
        lon2 = math.degrees(lon2)
        return (lat2, lon2)

    def get_bearing(self, lat1, lon1, lat2, lon2):
        dLon = (lon2 - lon1)
        x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
        y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - \
            math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
            math.cos(math.radians(dLon))
        brng = math.atan2(x, y)
        brng = math.degrees(brng)
        return brng
