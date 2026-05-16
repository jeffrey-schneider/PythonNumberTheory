'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import Primes
import math
import warnings
from collections.abc import Iterator
import functools
# from fontTools.misc.textTools import num2binary
# from pkg_resources import _sset_none, _sget_none
# from tkinter.constants import FALSE
from collections import deque
from typing import override, List, Any

'''
Purpose of this Class.
This project is not to show the best in programming code or style,
    it is only to assist the end user in problem solving.

It was a way to combine library and class.

It started by the desire to calculate latitude and longitude from inside
    of a object to a destination and then evolved 
    into a library of functions that can be used to calculate latitude
    and longitude between two objects. 
'''

"""
get_divisors(v)              # All divisors including 1 and v
get_proper_divisors(v)       # All divisors excluding v
get_non_trivial_divisors(v)  # All divisors excluding 1 and v
get_prime_factors(v)         # Prime factors with repetition
get_distinct_prime_factors(v)# Prime factors without repetition
"""

ITERATIONS = 1000

@staticmethod
def get_sum_of_squares(vList: list[int]) -> int:
    retVal = 0
    for v in vList:
        retVal += v * v
    return retVal


class NumberTheory:

    def __init__(self, theNumber: int) -> None:
        self._the_number = theNumber

    @property
    def the_number(self) -> int:
        return self._the_number

    @the_number.setter
    def the_number(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value).__name__}")
        self._the_number = value

    @staticmethod
    def get_square(v: int) -> int:
        # Reference implementation demonstrating instance/static delegation pattern        
        return v * v
    
    def get_square(self)->int:
        return NumberTheory.get_square(self.the_number)
    
    @staticmethod
    def get_cube(v: int) -> int:
        return v * v * v
    
    def get_cube(self)->int:
        return NumberTheory.get_cube(self.the_number)
    

    @staticmethod
    def get_product_of_squares(v_list: list[int]) -> int:
       return math.prod(x * x for x in v_list)

    @staticmethod
    def get_sum_of_digits(v: int) -> int:
        return sum(int(d) for d in str(v))
    
    def get_sum_of_digits(self) -> int:
        return NumberTheory.get_sum_of_digits(self.the_number)
    
    
    @staticmethod
    def get_product_of_digits(v: int) -> int:
        return math.prod(int(d) for d in str(v))
    
    def get_product_of_digits(self)->int:
        return NumberTheory.get_product_of_digits(self.the_number)
    


    @staticmethod
    def number_to_list(the_number: int) -> list[int]:
        '''
        Split an integer into a list of the digits left to right
        '''
        return [int(d) for d in str(the_number)]
    
    def number_to_list(self)-> list[int]:
        return NumberTheory.number_to_list(self.the_numer)
    

    @staticmethod
    def get_list_of_digits(self=None, v: int = None) -> list[int]:
        '''
        Usage: provide java getListOfDigits() equivalency
        '''
        if v is None:
            v = self.the_number()
        return NumberTheory.number_to_list(v)

    '''
    Return sum of a list
    aka sigma of a list
    '''

    @staticmethod
    def sum_of_list(the_collection) -> int:
        '''Wrapper for Python built-in sum(). 
        Retained for compatibility with dependent methods.'''
        return sum(the_collection)

    @staticmethod
    def multiple_of_list(the_collection) -> int:
        '''Wrapper for Python built-in sum(). 
        Retained for compatibility with dependent methods.'''
        return math.prod(the_collection)

    @staticmethod
    def is_prime(v: int) -> bool:  
        if v < 2 :
            return False      
        if v == 2:
            return True
        if v % 2 == 0:
            return False
        
        stop_val = int(math.sqrt(v))+1        
        for i in range(3, stop_val, 2):
            if v % i == 0:
                return False
        return True
    
    def is_prime(self) -> bool:
        return NumberTheory.is_prime(self.the_number)
    

    @staticmethod
    def get_collatz(v: int) -> list[int]:
        """
        Returns the Collatz sequence starting from v.
        If v is even divide by 2.
        If v is odd multiply by 3 and add 1.
        Sequence ends when it reaches 1.
        """
        if v < 1:
            raise ValueError(f"Collatz sequence requires positive integer, got {v}")
        sequence = [v]
        counter = v
    
        while counter > 1:
            if counter % 2 == 0:
                counter //= 2
            else:
                counter = 3 * counter + 1
            sequence.append(counter)    
        return sequence

    def get_collatz(self) -> list[int]:
        return NumberTheory.get_collatz(self.the_number)


    @staticmethod
    def get_jugglers(v: int) -> list[int]:
        """
        Returns the Juggler sequence starting from v.
        If v is even next term is floor(v^0.5).
        If v is odd next term is floor(v^1.5).
        Sequence ends when it reaches 1.
        """
        if v < 1:
            raise ValueError(f"Juggler sequence requires positive integer, got {v}")
    
        sequence = [v]
        counter = v
    
        while counter > 1:
            if counter % 2 == 0:
                counter = math.isqrt(counter)
            else:
                counter = int(counter ** 1.5)
            sequence.append(counter)
            return sequence

    def get_jugglers(self) -> list[int]:
        return NumberTheory.get_jugglers(self.the_number)


    """ Starting to modify code to use list comprehensions"""

    @staticmethod
    def get_divisors(v: int) -> list[int]:        
        """
        This could have been done with SUM, but then I wouldn't have 
        learned about list comprehensions
        """
        return [i for i in range(1, v + 1) if v % i == 0]

    def get_divisors(self)->list[int]:
        return NumberTheory.get_divisors(self.the_number)
    

    @staticmethod
    def factors_generator(n: int) -> Iterator[int]:
        """Generates all factors of n in ascending order."""
        if n < 1:
            raise ValueError(f"Expected positive integer, got {n}")
    
        small_factors = []
        large_factors = []
    
        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                small_factors.append(i)
                if i != n // i:
                    large_factors.append(n // i)
    
        yield from small_factors
        yield from reversed(large_factors)

    def factors_generator(self) -> Iterator[int]:
        return NumberTheory.factors_generator(self.the_number)


    @staticmethod
    def get_factors_sum(v: int) -> int:  
        """
        Returns the sum of all factors of v including v itself.
        Equivalent to get_sigma().

        Args:
            v: A positive integer.

        Returns:
            Sum of all positive factors of v.

        Example:
            get_factors_sum(12) returns 28  (1+2+3+4+6+12)

        Note:
            To sum only proper divisors excluding v itself
            use get_proper_divisors_sum() instead.
            This method is equivalent to get_sigma() and may
            be deprecated in a future version.
        """                      
        return NumberTheory.sum_of_list(NumberTheory.factors_generator(v))

    def get_factors_sum(self)->int:
        return NumberTheory.get_factors_sum(self.the_number)
    
    """
    @author: Jeffrey Schneider    
    Sum of all proper divisors (factors) except itself, hence the subtraction.
    """

    @staticmethod
    def get_aliquot_sum(v: int) -> int:        
        return NumberTheory.sum_of_list(NumberTheory.factors_generator(v)) - v
    
    def get_aliquot_sum(self) -> int:
        return NumberTheory.get_aliquot_sum(self.the_number)
    


    @staticmethod
    def get_reverse_number(v: int) -> int:
        """Returns the reverse of integer v."""
        return int(str(v)[::-1])
    
    def get_reverse_number(self) -> int:
        return NumberTheory.get_reverse_number(self.the_number)
    

    @staticmethod
    def get_reciprocal(v: int) -> float:        
        return 1 / v
    
    def get_reciprocal(self) -> float:
        return NumberTheory.get_reciprocal(self.the_number)
    


    @staticmethod
    def get_hex(v: int) -> str:
        """Returns the hexadecimal representation of v as an uppercase string."""
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        return format(v, 'X')

    def get_hex(self) -> str:
        return NumberTheory.get_hex(self.the_number)



    @staticmethod
    def get_octal(v: int) -> str:
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        return format(v, 'o')
    
    def get_octal(self)->str:
        return NumberTheory.get_octal(self.the_number)
        

    @staticmethod
    def get_binary(v: int) -> str:
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        return format(v, 'b')
    
    def get_binary(self)-> str:
        return NumberTheory.get_binary(self.the_number)


    @staticmethod
    def is_abundant(v: int) -> bool:
        """
        Boolean.
        Is the number's aliquot sum greater than the number?
        """        
        return NumberTheory.get_aliquot_sum(v) > v
    
    def is_abundant(self)-> bool:
        return NumberTheory.is_abundant(self.the_number)


    @staticmethod
    def get_proper_divisors(v:int) -> list[int]:
        """
        Returns all proper divisors of v exluding v itself.
        
        .. deprecated::
        Use get_divisors() and filter manually or use 
        factors_generator() directly.
        """
        warnings.warn(
            "get_proper_divisors is deprecated. "
            "Use factors_generator() directly instead.",
            DeprecationWarning,
            stacklevel=2
        )
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        return NumberTheory.factors_generator(v)

    def get_proper_divisors(self):
        return NumberTheory.get_proper_divisors(self.the_number)
    


    @staticmethod
    def get_abundance(v:int) -> int:        
        return NumberTheory.get_aliquot_sum(v) - v
    
    def get_abundance(self) -> int:
        return NumberTheory.get_abundance(self.the_number)
    


    @staticmethod
    def is_even(v: int) -> bool:        
        return v % 2 == 0
    
    def is_even(self)->bool:
        return NumberTheory.is_even(self.the_number)
    


    @staticmethod
    def is_perfect(v: int) -> bool:        
        return NumberTheory.get_abundance(v) == 0
    
    def is_perfect(self)->bool:
        return NumberTheory.is_perfect(self.the_number)
    

    @staticmethod
    def get_kynea(v: int) -> int:
        """
        Returns the nth Kynea number.
        Formula: (2^n + 1)^2 - 2
        """
        return (2 ** v + 1) ** 2 - 2

    def get_kynea(self) -> int:
        return NumberTheory.get_kynea(self.the_number)
    
    
    @staticmethod
    def get_carol(v: int) -> int:  
        """
        Returns the nth Carol number.
        Formula: (2^n - 1)^2 - 2
        """  
        carolA = 4 ** v
        carolB = 2 ** (v + 1)
        carolFinal = carolA - carolB - 1
        return carolFinal

    def get_carol(self) -> int:
        return NumberTheory.get_carol(self.the_number)



    @staticmethod    
    @functools.cache
    def factorial(n: int) -> int:
        """Returns n factorial recursively with caching."""
        if n < 0:
            raise ValueError(f"Factorial undefined for negative integers, got {n}")
        if n <= 1:
            return 1
        return n * NumberTheory.factorial(n - 1)
    

    def factorial(self) -> int:
        return NumberTheory.factorial(self.the_number)

    
    @staticmethod
    @functools.cache
    def get_factorial(v:int) -> int:        
        """
        Returns n factorial.
        Uses Python's built in math.factorial for arbitrary precision.
        """
        if v < 0:
            raise ValueError(f"Factorial undefined for negative integers, got {n}")
        return math.factorial(v)
    


    @staticmethod
    def get_sigma(v: int) -> int:
        """
        Returns sigma(v), the sum of ALL positive divisors of v
        including v itself.
        Also known as the divisor function σ(n).

        Args:
            v: A positive integer.

        Returns:
            Sum of all positive divisors of v.

        Example:
            get_sigma(12) returns 28  (1+2+3+4+6+12)

        Note:
            To sum only proper divisors excluding v itself
            use get_proper_divisors_sum() instead.
            To get the list of divisors rather than their sum
            use get_divisors() or factors_generator() instead.
        """

        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        return sum(NumberTheory.factors_generator(v))

    def get_sigma(self) -> int:
        return NumberTheory.get_sigma(self.the_number)
    

    @staticmethod
    def get_catalan( v: int ) -> int: 
        """
        Returns the nth Catalan number.
        Formula: (2n)! / ((n+1)! * n!)
        """       
        catA = NumberTheory.get_factorial(2 * v)
        catB = NumberTheory.get_factorial(v + 1)
        catC = NumberTheory.get_factorial(v)
        cat_final = catA // (catB * catC)
        return cat_final
    
    def get_catalan(self)->int:
        NumberTheory.get_catalan(self.the_number)



    @staticmethod
    def get_fibonacci_list(v: int) -> list[int]:
        """
        Returns a list of the first v Fibonacci numbers.
        Sequence starts 0, 1, 1, 2, 3, 5, 8, 13...

        Args:
            v: The number of terms to generate.

        Returns:
            A list of v Fibonacci numbers starting from 0.

        Example:
            get_fibonacci_list(6) returns [0, 1, 1, 2, 3, 5]

        Note:
        To generate terms up to a maximum value rather than
        a fixed count use get_fibonacci_like() instead.

        The for _ in range(v) pattern.
        The underscore signals that the loop variable is intentionally 
        unused. We only care about the count not the index. Pythonic 
        convention for this situation.
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")        
    
        a, b = 0, 1
        sequence = []
        for _ in range(v):
            sequence.append(a)
            a, b = b, a+b                        
        return sequence
    
    def get_fibonacci_list(self)-> list[int]:
        return NumberTheory.get_fibonacci_list(self.the_number)
    

    @staticmethod
    def fibonacci_generator(v: int):
        """Generates the first v Fibonacci numbers."""
        a, b = 0, 1
        for _ in range(v):
            yield a
            a, b = b, a+b

    @staticmethod
    def fibonacci_generated(v: int) -> list[int]:
        """
            Returns a list of the first v Fibonacci numbers.
            Uses the fibonacci_generator
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}") 
        return list(NumberTheory.fibonacci_generator(v))       

    def fibonacci_generated(self) -> list[int]:
        return NumberTheory.fibonacci_generated(self.the_number)
    

    @staticmethod  
    def get_fibonacci_like(v: int, number1: int = 1, number2: int = 1) -> list[int]:
        """
            Returns a Fibonacci-like sequence containing all terms up to and
            including v. Unlike get_fibonacci_list() which generates a fixed
            number of terms this method generates terms until the value v is reached.

            Args:
                v: The maximum value. Sequence stops when next term exceeds v.
                number1: First term of the sequence. Defaults to 1.
                number2: Second term of the sequence. Defaults to 1.

            Returns:
                A list of Fibonacci-like numbers where all terms are <= v.

            Example:
                get_fibonacci_like(20) returns [1, 1, 2, 3, 5, 8, 13]
                get_fibonacci_like(20, 2, 5) returns [2, 5, 7, 12]

            Note:
                To generate a fixed number of terms regardless of value
                use get_fibonacci_list() instead.
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
    
        sequence = []
        a, b = number1, number2
    
        while a <= v:
            sequence.append(a)
            a, b = b, a + b
    
        return sequence
    
    def get_fibonacci_like(self, number1: int = 1, number2: int = 1) -> list[int]:
        return NumberTheory.get_fibonacci_like(self.the_number, number1, number2)



    @staticmethod
    def get_lucas_list(v: int) -> list[int]:
        """
        Returns a list containing exactly v terms of the Lucas sequence.
        Sequence begins 2, 1, 3, 4, 7, 11, 18...

        Args:
            v: The number of terms to generate

        Returns:
            A list of v Lucas numbers starting from 2.

        Example:
            get_lucas_list(6) returns [2, 1, 3, 4, 7, 11]
        
        Note:
            The Lucas sequence uses the same recurrence relaation
            as Fibonacci but starts with 2, 1 instead of 0, 1.
            For the Fibonacci sequence use get_fibonacci_list() instead.
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        sequence = []        
        a, b = 2, 1               
        for _ in range(v):
            sequence.append(a)
            a, b = b, a + b
        return sequence
    
    def get_lucas_list(self)-> list[int]:
        return NumberTheory.get_lucas_list(self.the_number)
    
    
    @staticmethod
    @functools.cache
    def get_motzkin(v: int) -> int:
        """
        Returns the nth Motzkin number.
        Motzkin numbers count the number of ways to draw
        non-crossing chords on a circle with n points.
        Formula: M(n) = ((2n+1)*M(n-1) + (3n-3)*M(n-2)) / (n+2)

        Args:
            v: A non-negative integer.

        Returns:
            The nth Motzkin number.

        Example:
            get_motzkin(0) returns 1
            get_motzkin(4) returns 9
            get_motzkin(7) returns 127
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        if v <= 1:
            return 1
    
        m1 = NumberTheory.get_motzkin(v - 1)
        m2 = NumberTheory.get_motzkin(v - 2)
    
        return ((2 * v + 1) * m1 + (3 * v - 3) * m2) // (v + 2)
    

    def get_motzkin(self) -> int:
        return NumberTheory.get_motzkin(self.the_number)
    
    

    @staticmethod
    def is_primitive_abundant(v:int) -> bool: 
        """
        Returns True if v is a primitive abundant number.
        A primitive abundant number is an abundant number where
        none of its proper divisors are abundant.

        Args:
            v: A positive integer.

        Returns:
            True if v is a primitive abundant number, False otherwise.

        Example:
            is_primitive_abundant(20) returns True
            is_primitive_abundant(40) returns False (20 is an abundant divisor)

        Note:
            All primitive abundant numbers are abundant but not all
            abundant numbers are primitive abundant.
            See also is_abundant().
        """   
        if v < 1:
            raise ValueError(f"Expected non-negative integer, got {v}")    
        
        if not NumberTheory.is_abundant(v):
            return False
        
        return not any(
            NumberTheory.is_abundant(i) 
            for i in NumberTheory.get_proper_divisors(v)
        )

    def is_primitive_abundant(self) -> bool:
        return NumberTheory.is_primitive_abundant(self.the_number)
    '''
    @author: Jeffrey Schneider
    @see https://www.youtube.com/watch?v=uuMwz47LV_w
    '''

    @staticmethod
    def is_keith_number(v:int) -> bool:        
        current_sum = 0    
        # deque chosen for O(1) appendleft performance    
        list_of_digits = deque(NumberTheory.number_to_list(v))
        while current_sum < v:
            current_sum = NumberTheory.sum_of_list(list_of_digits)
            if current_sum == v:
                return True
            list_of_digits.appendleft(current_sum)            
        return False
    
    def is_keith_number(self)->bool:
        return NumberTheory.is_keith_number(self.the_number)
    



    @staticmethod
    def get_amicable_number(v:int) -> int|None: 
        """
        Returns the amicable pair of v if one exists otherwise None.
        Two numbers are amicable if each equals the sum of the
        proper divisors of the other.

        Args:
            v: A positive integer.

        Returns:
            The amicable pair of v or None if v has no amicable pair.

        Example:
            get_amicable_number(220) returns 284
            get_amicable_number(284) returns 220
            get_amicable_number(6) returns None   (perfect number)
            get_amicable_number(5) returns None   (no amicable pair)

        Note:
            Perfect numbers return None since they are not
            considered amicable with themselves.
            See also is_amicable() to test if v is amicable
            without retrieving the pair.
        """     
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")  
        first_divisor_sum = NumberTheory.get_aliquot_sum(v)
        if first_divisor_sum == v:
            return None
        second_divisor_sum = NumberTheory.get_aliquot_sum(first_divisor_sum)
        if second_divisor_sum == v:
            return first_divisor_sum

    def get_amicable_number(self) -> int|None:
        return NumberTheory.get_amicable_number(self.the_number)
    

    @staticmethod
    def is_amicable(v:int)->bool:
        """ 
        Returns True if v is part of an amicable pair.
         """
        return NumberTheory.get_amicable_number(v) is not None
    
    def is_amicable(self) -> bool:
        return NumberTheory.is_amicable(self.the_number)


    @staticmethod
    def get_non_trivial_divisors(v: int) -> list[int]:
        """
        Returns all divisors of v excluding 1 and v itself.
        Also known as proper divisors excluding unity.

        Args:
            v: A positive integer.

        Returns:
            A sorted list of divisors of v excluding 1 and v.

        Example:
            get_non_trivial_divisors(12) returns [2, 3, 4, 6]
            get_non_trivial_divisors(6) returns [2, 3]

        Note:
            To include 1 in the divisor list use
            get_proper_divisors() instead.
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        proper = NumberTheory.get_proper_divisors(v)
        return [d for d in proper if d != 1]

    def get_non_trivial_divisors(self) -> list[int]:
        return NumberTheory.get_non_trivial_divisors(self.the_number)


    @staticmethod
    def get_betrothed_number(v: int) -> int | None:
        """
        Returns the betrothed pair of v if one exists otherwise None.
        Two numbers m and n are betrothed if the sum of non trivial
        divisors of m equals n and vice versa.

        Args:
            v: A positive integer.

        Returns:
            The betrothed pair of v or None if no pair exists.

        Example:
            get_betrothed_number(48) returns 75
            get_betrothed_number(75) returns 48
            get_betrothed_number(5) returns None

        Note:
            Similar to amicable numbers but uses non trivial
            divisors excluding both 1 and v instead of proper
            divisors excluding only v.
            See also get_amicable_number().
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
    
        this_number = sum(NumberTheory.get_non_trivial_divisors(v))
        that_number = sum(NumberTheory.get_non_trivial_divisors(this_number))
    
        if that_number == v:
            return this_number
    
        return None

    def get_betrothed_number(self) -> int | None:
        return NumberTheory.get_betrothed_number(self.the_number)


    @staticmethod
    def get_cake_number(v: int) -> int:
        """
        Returns the nth Cake number.
        The maximum number of pieces a cake can be cut into
        with v planar cuts.
        Formula: (v^3 + 5v + 6) / 6

        Args:
            v: A non-negative integer representing the number of cuts.

        Returns:
            The nth Cake number.

        Example:
            get_cake_number(0) returns 1
            get_cake_number(3) returns 8
            get_cake_number(5) returns 26

        Note:
            Related to the Lazy Caterer sequence which counts
            maximum pieces from cuts of a circle.
        """
        if v < 0:            
            raise ValueError(f"Expected non-negative integer, got {v}")
        return (v**3 + 5 * v + 6) // 6

    def get_cake_number(self) -> int:
        return NumberTheory.get_cake_number(self.the_number)


    '''https://codereview.stackexchange.com/questions/12119/printing-nth-bell-number'''

    @staticmethod
    def get_bell_number(v: int) -> int:
        """
        Returns the nth Bell number using the Bell triangle method.
        Bell numbers count the number of ways to partition a set of n elements.

        Args:
            v: A non-negative integer.

        Returns:
            The nth Bell number.

        Example:
            get_bell_number(0) returns 1
            get_bell_number(4) returns 15
            get_bell_number(6) returns 203

        Note:
            Uses Bell triangle construction for exact integer arithmetic.
            The Dobinski series approximation is avoided due to
            floating point precision issues for large v.
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
    
        # Build Bell triangle row by row
        current_row = [1]
    
        for _ in range(v):
            next_row = [current_row[-1]]
            for j in range(len(current_row)):
                next_row.append(next_row[j] + current_row[j])
            current_row = next_row
    
        return current_row[0]

    def get_bell_number(self) -> int:
        return NumberTheory.get_bell_number(self.the_number)


    @staticmethod
    def get_centered_polygonal_number(side_number:int, layers:int) -> int:
        if side_number < 1:
            raise ValueError(f"Expected non-negative integer, got {side_number}")        
        if layers < 1:
            raise ValueError(f"Expected non-negative integer, got {layers}")        
        return int(side_number * layers * (layers + 1) / 2 + 1)

    @staticmethod
    def get_polygonal_number(sides:int, layers:int) -> int:        
        s_minus_two = sides - 2
        s_minus_four = sides - 4
        return (1 // 2) * (s_minus_two * layers ** 2) - s_minus_four * layers;


    @staticmethod
    def get_primorial(v: int) -> int:
        """
        Returns the primorial of v defined as the product of
        the first v prime numbers.
    
        Args:
            v: A non-negative integer.

        Returns:
            The product of the first v primes.

        Example:
            get_primorial(1) returns 2
            get_primorial(4) returns 210  (2 * 3 * 5 * 7)
            get_primorial(0) returns 1    (empty product)

        Note:
            This implementation computes the product of the first
            v primes. For the alternate definition multiplying all
            primes up to and including v use a different method.
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        if v == 0:
            return 1
    
        product = 1
        prime_count = 0
        candidate = 2
    
        while prime_count < v:
            if Primes.is_prime(candidate):
                product *= candidate
                prime_count += 1
            candidate += 1
    
        return product

    def get_primorial(self) -> int:
        return NumberTheory.get_primorial(self.the_number)
    


    @staticmethod
    def get_pell_list(v: int) -> list[int]:
        """
        Returns a list containing exactly v terms of the Pell sequence.
        Sequence begins 0, 1, 2, 5, 12, 29, 70...
        Recurrence: P(n) = 2 * P(n-1) + P(n-2)

        Args:
            v: The number of terms to generate.

        Returns:
            A list of v Pell numbers starting from 0.

        Example:
            get_pell_list(6) returns [0, 1, 2, 5, 12, 29]

        Note:
            Similar to Fibonacci but uses 2 * previous term
            instead of 1 * previous term in the recurrence.
            For Fibonacci sequence use get_fibonacci_list() instead.
            For Lucas sequence use get_lucas_list() instead.
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
    
        sequence = []
        a, b = 0, 1
    
        for _ in range(v):
            sequence.append(a)
            a, b = b, 2 * b + a
    
        return sequence

    def get_pell_list(self) -> list[int]:
        return NumberTheory.get_pell_list(self.the_number)




    @staticmethod
    def get_jacobsthal_list( v: int) -> list[int]:        
        """
        Returns a list containing exactly v terms of the Jacobsthal sequence.
        Sequence begins 0, 1, 1, 3, 5, 11, 21, 43...
        Recurrence: J(n) = J(n-1) + 2 * J(n-2)

        Args:
            v: The number of terms to generate.

        Returns:
            A list of v Jacobsthal numbers starting from 0.

        Example:
            get_jacobsthal_list(6) returns [0, 1, 1, 3, 5, 11]

        Note:
            Similar to Fibonacci but multiplies the second previous
            term by 2 instead of 1.
            J(n) = J(n-1) + 2 * J(n-2)
            For Fibonacci use get_fibonacci_list() instead.
            For Pell sequence use get_pell_list() instead.
            For Lucas sequence use get_lucas_list() instead.
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
    
        sequence = []
        a, b = 0, 1       
        
        for _ in range(v):        
            sequence.append(a)
            a, b = b, b + 2 * a                       
        return sequence
        
        def get_jacobsthal_list(self):
            return NumberTheory.get_jacobsthal(self.the_nunumber)
        



    @staticmethod
    def get_jacobsthal(v: int) -> int:
        """Returns the nth Jacobsthal number."""
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        if v == 0:
            return 0
        if v == 1:
            return 1
        a, b = 0, 1
        for _ in range(v - 1):
            a, b = b, b + 2 * a
        return b

    def get_jacobsthal(self) -> int:
        return NumberTheory.get_jacobsthal(self.the_number)



    @staticmethod
    def get_alternating_factorial(v:int) -> int:        
        """
        Returns the alternating factorial of v.
        Defined as v! - (v-1)! + (v-2)! - ... + (-1)^(v-1) * 1!

        Args:
            v: A positive integer.

        Returns:
            The alternating factorial of v.

        Example:
            get_alternating_factorial(1) returns 1
            get_alternating_factorial(3) returns 5   (6 - 2 + 1)
            get_alternating_factorial(5) returns 101 (120 - 24 + 6 - 2 + 1)
        """
        if v < 0:
            raise ValueError(f"Expected non-negative integer, got {v}")
        total = 0
        sign = 1  #Start wit positive sign
        for i in range(v, 0, -1):
            total += sign * NumberTheory.factorial(i)
            sign *= -1  #Alternate the sign
        return total

    def get_alternating_factorial(self) -> int:        
        return NumberTheory.get_alternating_factorial(self.the_number)


    
    @staticmethod
    def is_deficient(v:int) -> bool:        
        return NumberTheory.get_aliquot_sum(v) < v

    def is_deficient(self)-> bool:
        return NumberTheory.is_deficient(self.the_number)
    

    @staticmethod
    def is_super_abundant(v: int) -> bool:
        """
        Returns True if v is a superabundant number.
        A superabundant number has a higher ratio of sigma(n)/n
        than all smaller positive integers.
        sigma(v)/v > sigma(i)/i for all 1 <= i < v.

        Args:
            v: A positive integer.

        Returns:
            True if v is superabundant, False otherwise.

        Example:
            is_super_abundant(1) returns True
            is_super_abundant(2) returns True
            is_super_abundant(4) returns True
            is_super_abundant(3) returns False

        Note:
            All superabundant numbers are abundant numbers
            but not all abundant numbers are superabundant.
            See also is_abundant().
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
    
        sigma_v = NumberTheory.get_sigma(v)
    
        return all(
            sigma_v * i > NumberTheory.get_sigma(i) * v
            for i in range(1, v)
        )

    def is_super_abundant(self) -> bool:
        return NumberTheory.is_super_abundant(self.the_number)



    @staticmethod
    def gcd(b: int, n: int) -> int:
        if n == 0:
            return b
        return NumberTheory.gcd(n, b % n)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        return a * (b / NumberTheory.gcd(a, b))
    

    @staticmethod
    def is_carmichael(v: int) -> bool:
        """
        Returns True if v is a Carmichael number.
        A Carmichael number is a composite number n where
        b^(n-1) ≡ 1 (mod n) for all integers b coprime to n.
        Carmichael numbers are sometimes called absolute
        pseudoprimes.

        Args:
            v: A positive integer.

        Returns:
            True if v is a Carmichael number, False otherwise.

        Example:
            is_carmichael(561) returns True
            is_carmichael(1105) returns True
            is_carmichael(7) returns False  (prime not composite)
            is_carmichael(4) returns False  (not pseudoprime)

        Note:
            Carmichael numbers fool the Fermat primality test.
            They are composite but behave like primes under
            Fermat's little theorem.
            See also is_prime().
        """
        if v < 2:
            raise ValueError(f"Expected integer >= 2, got {v}")
    
        if Primes.is_prime(v):
            return False
    
        return all(
            pow(b, v - 1, v) == 1
            for b in range(2, v)
                if NumberTheory.gcd(b, v) == 1
        )

    def is_carmichael(self) -> bool:
        return NumberTheory.is_carmichael(self.the_number)
    
    

    @staticmethod
    # Function to find the N-th
    # icosikaipentagon number
    def isDNum(n: int) -> bool:        
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
            v = self.the_number()
        return (v * v + v + 2) / 2

    @staticmethod
    def get_cullen(self, v=None) -> int:
        if v is None:
            v = self.the_number()
        return v * math.pow(2, v) + 1

    @staticmethod
    def is_co_prime(bNumber:int, v:int) -> bool:  
        """
        Returns True if bNumber and v share no common factors other than 1.
        Example: is_co_prime(8, 9) returns True
        """      
        return NumberTheory.gcd(bNumber, v) == 1
    
    def is_co_prime(self, other: int) -> bool:
        return NumberTheory.is_co_prime(self.the_number, other)
            

    @staticmethod
    # https://www.geeksforgeeks.org/compositorial-of-a-number/
    # Python3 program to find Compositorial
    # of composite numbers

    # Function to check
    # if a number is composite.
    def is_composite(n:int) -> bool:        
        # Corner cases
        if n <= 3:
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
            i += 6
        return False

    def is_composite(self) -> bool:
        return NumberTheory.is_composite(self.the_number)

    @staticmethod
    def compositorial_list(n: int) -> list[int]:
        """
        Returns a list of the first n composite numbers.
        Example: compositorial_list(5) returns [4, 6, 8, 9, 10]
        """
        result = []
        count = 0
        i = 4
        while count < n:
            if NumberTheory.is_composite(i):
                result.append(i)
                count += 1
            i += 1
        return result
    
    def compositorial_list(self) -> list[int]:
        return NumberTheory.compositorial_list(self.the_number)

        
    @staticmethod
    def calculate_compositorial(n: int) -> int:
        """
        Returns the compositorial of n, defined as the product
        of the first n composite numbers.
        Example: calculate_compositorial(3) returns 192  (4 * 6 * 8)
        """
        return NumberTheory.multiple_of_list(NumberTheory.compositorial_list(n))

    def calculate_compositorial(self) -> int:
        return NumberTheory.calculate_compositorial(self.the_number)
    
    
    @staticmethod
    def is_curzon(v: int) -> bool: 
        """
        A Curzon number is a positive integer n where 2^n + 1 is 
        divisible by 2n + 1.
        Example: 5 is Curzon since 2^5 + 1 = 33, and 33 / 11 = 3.
        """       
        a = 2 ** v + 1
        b = 2 * v + 1
        return a % b == 0

    def is_curzon(self) -> bool:
        return NumberTheory.is_curzon(self.the_number)    



    @staticmethod
    def get_totatives(v:int) -> list[int]: 
        """
        Returns a list of all totatives of v — positive integers
        less than or equal to v that are coprime to v.
        Example: get_totatives(9) returns [1, 2, 4, 5, 7, 8]
        """       
        retList = []
        counter = 1
        while counter <= v:
            if NumberTheory.is_co_prime(v, counter):
                retList.append(counter)
            counter += 1
        return retList
    
    def get_totatives(self) -> list[int]:
        return NumberTheory.get_totatives(self.the_number)
    

    @staticmethod
    def eulers_phi(v: int) -> int:
        """
        Returns Euler's totient φ(v), the count of integers from 1 to v
        that are coprime to v.
        Example: eulers_phi(9) returns 6  (1, 2, 4, 5, 7, 8)
        Example: eulers_phi(1) returns 1
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        return sum(1 for i in range(1, v + 1) if NumberTheory.gcd(i, v) == 1)

    def eulers_phi(self) -> int:
        return NumberTheory.eulers_phi(self.the_number)
    

    @staticmethod
    def is_de_polignac(v: int) -> bool:
        """
        A de Polignac number is an odd number that cannot be expressed
        as 2^k + p for any prime p and positive integer k.
        Example: 127 is a de Polignac number.
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        if NumberTheory.is_even(v):
            return False
        for p in range(2, v):
            if NumberTheory.is_prime(p):
                remainder = v - p
                if remainder > 0 and (remainder & (remainder - 1)) == 0:
                    return False
        return True

    def is_de_polignac(self) -> bool:
        return NumberTheory.is_de_polignac(self.the_number)
    

    @staticmethod
    def is_odd(v:int) -> bool:    
        return v % 2 != 0
    
    def is_odd(self)-> bool:
        return NumberTheory.is_odd(self.the_number)
    


    @staticmethod
    def is_happy(v: int) -> bool:
        """
        A happy number is defined by the following process: starting with any
        positive integer, replace the number by the sum of the squares of its
        digits, and repeat until the number equals 1 (happy) or loops endlessly
        in a cycle that never reaches 1 (unhappy).
        Example: 19 is happy since 1²+9²=82, 8²+2²=68, 6²+8²=100, 1²+0²+0²=1
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        seen = set()
        while v != 1:
            v = sum(int(d) ** 2 for d in str(v))
            if v in seen:
                return False
            seen.add(v)
        return True

    def is_happy(self) -> bool:
        return NumberTheory.is_happy(self.the_number)
    


    @staticmethod
    def get_lucky_number_list(v: int) -> list[int]:
        """
        Returns the first v lucky numbers using a sieve method.
        Lucky numbers are generated by iteratively eliminating every
        nth element from a sequence of odd numbers.
        Example: get_lucky_number_list(6) returns [1, 3, 7, 9, 13, 15]
        https://www.w3resource.com/python-exercises/math/python-math-exercise-17.php
        """
        if v < 1:
            raise ValueError(f"Expected positive integer, got {v}")
        the_list = list(range(-1, v * v + 9, 2))
        i = 2
        while the_list[i:]:
            the_list = sorted(set(the_list) - set(the_list[the_list[i]::the_list[i]]))
            i += 1
        return the_list[1:v + 1]

    def get_lucky_number_list(self) -> list[int]:
        return NumberTheory.get_lucky_number_list(self.the_number)


    @staticmethod
    def get_double_factorial(v):        
        if v == 0 or v == -1:
            return 1

        if v < -1:
            raise ValueError("Double factorial not defined for v < -1")

        retVal = 1
        for i in range(v, 0, -2):
            retVal *= i

        return retVal
    
    def get_double_factorial_self(self):        
        return NumberTheory.get_double_factorial(self.the_number)


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

    #work on this 
    def is_achilles(v: int) -> int:        
        return (NumberTheory.is_powerful(None,v) and not NumberTheory.isPerfectPower(None, v))


    def is_admirable(self):
        pass

    def is_alternating(self):
        pass

    def is_amenable(self):
        pass

    @staticmethod
    def the_queue() -> None:
        queue = []
        theList = NumberTheory.get_divisors(3600)
        for i in theList:
            queue.append(i)
        while len(queue) > 0:
            print(queue.pop(), end=' ')
        print()

    @staticmethod
    def sum_of_factors(v: int) -> int:
        # Get the list of factors
        factors = NumberTheory.get_divisors(v)
        # Calculate the sum of factors
        total_sum = sum(factors)
        return sum(NumberTheory.get_divisors(v))

    '''
    def is_antiperfect(self, v=None):        
        if v is None:
            v = self.the_number
        the_list = self.get_divisors(v)
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

    '''
    public static boolean isApocalyptic(int exponent) {
		String getTestNumber = getBigIntegerPower(2, exponent);
		return getTestNumber.contains("666");
	}'''


    @staticmethod
    def is_apocalyptic(v: int) -> bool:        
        test_result = str(pow(2, v))        
        return "666" in test_result

    def is_apocalyptic(self) -> bool:
        return NumberTheory.is_apocalyptic(self.the_number)


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

    def is_fibo_div(self):
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

    #def isPerfect(self):
    #    pass

    @staticmethod
    def is_perfect_power(n: int)-> bool:
        '''
        		  Tests whether an integer n is a perfect power, perfect powers are any integer
        		  that is an integer power of another integer for example 4(2^2) 9(3^2) 27(3^3)
        		  243(3^5) are all perfect powers Returns a pair of integers [a,b] such that n
        		  = a^b. (If multiple possible values for a and b exist, the pair with the
        		  smallest a value is returned)
        '''        
        if n < 1:
            return False
        for a in range(2, int(math.sqrt(n)) + 1):
            b = 2
            power = a ** b
            while power <= n:
                if power == n:                    
                    return True
                b += 1
                power = a ** b
        return False

    def is_perfect_power(self)-> bool:
        return  NumberTheory.is_perfect_power(self.the_number)
    


    def isPernicious(self):
        pass

    def isPoulet(self):
        pass

    def isPowerOfTwo(self):
        pass



    @staticmethod
    def prime_factors_with_exponents(v: int) -> dict[int,int]:        
        # OpenAI. (2024). Python code to determine if a number is powerful. Retrieved June 26, 2024, from https://chat.openai.com
        factors = {}
        divisor = 2
        while v > 1:
            count = 0
            while(v % divisor) == 0:
                v //=divisor
                count += 1
            if count > 0:
                factors[divisor] = count
            divisor += 1
        return factors
    
    def prime_factors_with_exponents(self) -> dict[int, int]:
        return NumberTheory.prime_factors_with_exponents(self.the_number)

    @staticmethod
    def is_powerful(self = None, v: int=None) -> bool:
        if v is None:
            v = self.the_number()
        # OpenAI. (2024). Python code to determine if a number is powerful. Retrieved June 26, 2024, from https://chat.openai.com
        # Determines if a number is powerful
        if v == 1:
            return True
        factors = NumberTheory.prime_factors_with_exponents(None, v)
        for exponent in factors.values():
            if exponent < 2:
                return False
        return True


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


    @staticmethod
    def is_sastry(v: int) -> bool:        
        """
        A Sastry number is one where concatenating v and v+1 produces a perfect square.
        Example: 183 is Sastry since 183184 = 428^2.
        """
        x: int = v + 1
        z = int(str(v) + str(x))
        root = math.isqrt(z)
        return root * root == z
        """
        math.isqrt(z) returns the integer square root, 
        then root * root == z confirms it exactly — 
        no floating point involved at all.
        """
            
    def is_sastry(self) -> bool:
        return NumberTheory.is_sastry(self.the_number)



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
