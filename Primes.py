import math
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bisect import bisect_left


import NumberTheory
"""
Recreated 10/22/2023 by 
@author   Jeffrey Schneider
"""

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

def generate_primes(limit: int) -> list[int]:
    primes = []

    for value in range(2, limit + 1):
        if is_prime(value):
            primes.append(value)

    return primes
    
def get_prime_factors(v: int) -> list[int]:
    factors = []
    d = 2
    n = v

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //=d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
    
def is_semi_prime(v: int) -> bool:        
    if v in (0, 1):
        return False        
    return len(get_prime_factors(v)) == 2

def get_prime_sieve(n: int) -> list[bool]:
    """
    Constructs a primality sieve for integer values in the interval [0, n].

    Composite values are removed iteratively by marking multiples of
    each discovered prime beginning at p², since smaller multiples
    have already been processed by earlier primes.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            is_prime[p*p::p] = [False] * ((n - p*p) // p + 1)
        p += 1
    return is_prime
    
def get_digit_count(v: int) -> int:
    if v <= 0:
        raise ValueError(f"Expected positive integer, got {v}")
    return math.floor(math.log10(v)) + 1

   

def is_brilliant(n: int) -> bool:
    """
        A brilliant number is a semiprime where both prime factors
        have the same number of digits.
        https://www.geeksforgeeks.org/brilliant-numbers/
    """
    if n < 4:
        return False
    
    is_prime = get_prime_sieve(n)
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i] and n % i == 0:
            x = n // i
            if is_prime[x]:
                if get_digit_count(i) == get_digit_count(x):
                    return True
    return False


def is_emirpimes(v: int) -> bool:
    """
    A number is called emirpimes if it is a semiprime and if its reverse
    is a different semiprime, thus excluding palindromic semiprimes.
    """
    if v <= 0:
        raise ValueError(f"Expected positive integer, got {v}")
    reverse_number = NumberTheory.get_reverse_number(v)

    if v == reverse_number:
        return False

    return is_semi_prime(v) and is_semi_prime(reverse_number)



def is_chen_prime(v: int) -> bool:        
    if is_prime(v):
        if v <= 0:
            raise ValueError(f"Expected positive integer, got {v}")
        return is_prime(v + 2) or is_semi_prime(v + 2)
    return False

   

def is_emirp(v: int) -> bool:
    """An emirp (prime spelled backwards) is a prime number that results
    in a different prime when its decimal digits are reversed. This definition
    excludes this related palindrome 
    """
    if v <= 0:
        raise ValueError(f"Expected positive integer, got {v}")
    return is_prime(v) and is_prime(NumberTheory.get_reverse_number(v))
    

def is_good_prime(v: int) -> bool:
    """
    A good prime is a prime number whose square is greater than the product of
    any two primes at the same number of positions before and after it in the
    sequence of  To solve this, create a list of primes from zero to 3x the
    number. Iterate pointers forwards and backwards in matching jumps through list.
    """
    if not is_prime(v):
        return False
    
    is_prime_sieve = get_prime_sieve(v * 3)
    the_prime_list = [i for i in range(2, v * 3 + 1) if is_prime_sieve[i]]
    
    if v not in the_prime_list:
        return False
    
    ndx = the_prime_list.index(v)
    
    for ndx_counter in range(1, ndx + 1):
        if ndx + ndx_counter >= len(the_prime_list):
            break
        small = the_prime_list[ndx - ndx_counter]
        large = the_prime_list[ndx + ndx_counter]
        if v * v < small * large:
            return False    
    return True

   

def get_next_prime(v: int) -> int:
    """
    Returns the first prime number greater than v.

    Example:
        get_next_prime(10) returns 11.
    """
    candidate = v + 1

    while not is_prime(candidate):
        candidate += 1

    return candidate


def get_previous_prime(v: int) -> int:
    """
    Returns the first prime number less than v.

    Example:
        get_next_prime(10) returns 7.
    """
    candidate = v - 1

    while candidate > 1:
        if is_prime(candidate):
            return candidate

        candidate -= 1

    return 0


def get_next_prime_inclusive(v: int) -> int:
    """
    Returns v if v is prime; otherwise returns the first
    prime number greater than v.

    Example:
        get_next_prime_inclusive(11) returns 11.
        get_next_prime_inclusive(12) returns 13.
    """
    if is_prime(v):
        return v

    return get_next_prime(v)


def get_previous_prime_inclusive(v: int) -> int:
    """
    Returns v if v is prime; otherwise returns the first
    prime number less than v.

    Example:
        get_previous_prime_inclusive(11) returns 11.
        get_previous_prime_inclusive(14) returns 13.
    """
    if is_prime(v):
        return v

    return get_previous_prime(v)

def is_a_pointer_prime(v: int) -> bool:
    """
    A prime number p is called a-pointer if the next prime number can be obtained
    by adding p to its sum of digits (a stands for additive).
    Example: 293 is an a-pointer prime since the next prime equals 293 + 2 + 9 + 3 = 307.
    """
    if v < 0:
        return False
    
    if not is_prime(v):
        return False

    next_number = v + NumberTheory.get_sum_of_digits(v)
    return get_next_prime(v) == next_number

def is_m_pointer_prime(v: int) -> bool:
    """
    A prime number p is called m-pointer if the next prime number can be
    obtained by adding p to its product of digits (m stands for multiplicative).
    Example: 1231 is an m-pointer prime since the next prime equals
    1231 + 1 * 2 * 3 * 1 = 1237.
    """
    if v < 0:
        return False
    if not is_prime(v):
        return False
 
    next_number = v + NumberTheory.get_product_of_digits(v)
    return get_next_prime(v) == next_number
 



def is_inter_prime(v: int) -> bool:
    """
    An interprime is a composite number that is the average
    of two consecutive primes.
    Example: 9 is interprime since it is the average of 7 and 11.
    """
    if is_prime(v):
        return False

    prev_prime = get_previous_prime(v)
    next_prime = get_next_prime(v)

    return prev_prime + next_prime == 2 * v


def get_distinct_prime_factors(v: int) -> list[int]:
    """Returns a sorted set of distinct prime factors of v."""
    return sorted(set(get_prime_factors(v)))
  

def is_droll(v: int) -> bool:
    """
    A droll number is one where the sum of even prime factors
    equals the sum of odd prime factors.

    Example:
        72 = 2 * 2 * 2 * 3 * 3
        even sum = 6
        odd sum = 6
    """
    prime_factors = get_prime_factors(v)

    even_total = sum(p for p in prime_factors if p == 2)
    odd_total = sum(p for p in prime_factors if p != 2)

    return even_total > 0 and even_total == odd_total


def get_prime_lucky_numbers(v: int) -> list[int]:
    """Returns a list of lucky numbers up to v that are also prime."""
    return [n for n in NumberTheory.get_lucky_number_list(v) if is_prime(n)]

def is_co_prime(a: int, b: int) -> bool:
    """
    Two integers are called co-prime (or relatively prime) if their 
    greatest common divisor is 1.
    
    Co-primality is foundational for:
        modular arithmetic
        Euler’s totient function
        RSA cryptography
        reduced fractions
        Diophantine equations
    """
    return math.gcd(a,b) == 1


def get_lonely_numbers(limit: int) -> list[int]:
    """
    Returns all lonely numbers from 0 up to the specified limit.

    A number n is called lonely if its distance to the nearest
    prime number sets a new record.

    The distance for a number n is defined as the minimum distance
    between n and the closest prime different from n itself.

    Examples:
        0 is lonely because its nearest prime is 2, giving distance 2.

        23 is lonely because the surrounding primes are 19 and 29,
        giving a minimum distance of 4.

        120 is lonely because it lies between primes 113 and 127,
        giving a minimum distance of 7.

    Example:
        >>> get_lonely_numbers(100)
        [0, 23, 53]

    Args:
        limit (int):
            The inclusive upper bound to search for lonely numbers.

    Returns:
        list[int]:
            A list containing all lonely numbers less than or equal
            to the specified limit.
    
    """
    primes = get_primes_up_to(limit + 1000)

    lonely_numbers = []
    record_distance = -1

    for n in range(0, limit + 1):
        index = bisect_left(primes, n)

        previous_prime = None
        next_prime = None

        # closest prime below n
        if index > 0:
            previous_prime = primes[index - 1]

        # closest prime above n
        if index < len(primes):
            if primes[index] == n:
                if index + 1 < len(primes):
                    next_prime = primes[index + 1]
            else:
                next_prime = primes[index]

        if previous_prime is None:
            distance = next_prime - n
        elif next_prime is None:
            distance = n - previous_prime
        else:
            distance = min(n - previous_prime, next_prime - n)

        if distance > record_distance:
            lonely_numbers.append(n)
            record_distance = distance

    return lonely_numbers



def get_distance_to_closest_prime(v: int) -> int:
    left_prime = get_previous_prime(v)
    right_prime = get_next_prime(v)
    if left_prime == 0:
        return right_prime - v
    left_distance = v - left_prime
    right_distance = right_prime - v
    return min(left_distance, right_distance)
    

def get_fortunate_number(n: int) -> int:
    """
    Returns the Fortunate number for the primorial
    generated from the first n primes.
    """

    primes = get_first_n_primes(n)

    primorial = 1

    for p in primes:
        primorial *= p

    m = 2

    while True:
        if is_prime(primorial + m):
            return m

        m += 1


def is_n_smooth(value: int, n: int) -> bool:
    """
    In Number Theory  and n-smooth number is an integer whose prime factors are all less than 
    or equal to n.

    Basic Algorithm Idea

    To determine if a number is n-smooth:
        Factor the number.
        Check whether every prime factor is ≤ n.
    """
    if value < 1:
        return False
    
    if value == 1:
        return True   
    
    largest_prime = max(get_prime_factors(value))
    return largest_prime <= n
    

def is_pierpont_prime(v: int) -> bool:
    if v == 1:
        return False
    return is_prime(v) and is_n_smooth(v - 1, 3)



def is_sphenic(v: int) -> bool:
    """
    A sphenic number is a product of exactly three distinct prime factors.
    Example: 30 = 2 * 3 * 5 is sphenic.
    """
    return len(get_prime_factors(v)) == 3 and \
           len(get_distinct_prime_factors(v)) == 3


def get_primes_up_to(limit: int) -> list[int]:
    primes = []

    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)

    return primes


def get_first_n_primes(n: int) -> list[int]:
    primes = []
    candidate = 2

    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)

        candidate += 1

    return primes