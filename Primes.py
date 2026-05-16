import math

from NumberTheory import NumberTheory


class Primes(NumberTheory):
    """
    Recreated 10/22/2023 by 
    @author   Jeffrey Schneider
    """

    def __init__(self, theNumber):
        super().__init__(theNumber)

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
        return Primes.is_prime(self.the_number)
    

    @staticmethod
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
    
    def get_prime_factors(self) -> list[int]:
        return Primes.get_prime_factors(self.the_number)   



    @staticmethod
    def is_semi_prime(v: int) -> bool:        
        if v in (0, 1):
            return False        
        return len(Primes.get_prime_factors(v)) == 2

    def is_semi_prime(self) -> bool:
        return Primes.is_semi_prime(self.the_number)
    

    
    @staticmethod
    def sieve_of_eratosthenes(n: int) -> list[bool]:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                is_prime[p*p::p] = [False] * ((n - p*p) // p + 1)
            p += 1
    
    def sieve_of_eratosthenes(self) -> list[bool]:
        return Primes.sieve_of_eratosthenes(self.the_number)
    

    @staticmethod
    def get_digit_count(v: int) -> int:
        if v <= 0:
            raise ValueError(f"Expected positive integer, got {v}")
        return math.floor(math.log10(v)) + 1

    def get_digit_count(self) -> int:
        return Primes.get_digit_count(self.the_number)    
    

    # Function to check if N is a 
    # Brilliant number        
    @staticmethod
    def is_brilliant(n: int) -> bool:
        """
            A brilliant number is a semiprime where both prime factors
            have the same number of digits.
            https://www.geeksforgeeks.org/brilliant-numbers/
        """
        if n < 4:
            return False
    
        is_prime = Primes.sieve_of_eratosthenes(n)
    
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i] and n % i == 0:
                x = n // i
                if is_prime[x]:
                    if Primes.get_digit_count(i) == Primes.get_digit_count(x):
                        return True
        return False

    def is_brilliant(self) -> bool:
        return Primes.is_brilliant(self.the_number)



    @staticmethod
    def is_emirpimeses(v: int) -> bool:        
        reverse_number = NumberTheory.get_reverse_number(v)
        # print(f"{v}   {reverse_number}")
        if v != reverse_number:
            return Primes.is_semi_prime(v) and Primes.is_semi_prime(reverse_number)
        return False

    def is_emirpimeses(self) -> bool:
        return Primes.is_emirpimeses(self.the_number)


    @staticmethod
    def is_chen_prime(v: int) -> bool:        
        if Primes.is_prime(v):
            return Primes.is_prime(v + 2) or Primes.is_semi_prime(v + 2)
        return False

    def is_chen_prime(self) -> bool:
        return Primes.is_chen_prime(self.the_number)

    @staticmethod
    def is_emirp(v: int) -> bool:
        """An emirp (prime spelled backwards) is a prime number that results
        in a different prime when its decimal digits are reversed. This definition
        excludes this related palindrome primes.
        """
        return Primes.is_prime(v) and Primes.is_prime(Primes.get_reverse_number(v))
    
    @staticmethod
    def is_good_prime(v: int) -> bool:
        """
        A good prime is a prime number whose square is greater than the product of
        any two primes at the same number of positions before and after it in the
        sequence of primes. To solve this, create a list of primes from zero to 3x the
        number. Iterate pointers forwards and backwards in matching jumps through list.
        """
        if not Primes.is_prime(v):
            return False
    
        is_prime_sieve = Primes.sieve_of_eratosthenes(v * 3)
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

    def is_good_prime(self) -> bool:
        return Primes.is_good_prime(self.the_number)

    @staticmethod
    def get_neighbor_prime(v: int, return_next_prime: bool, return_number_if_prime: bool) -> int:
        """
        Args:
            v: The number from which to start.
            return_next_prime: True returns next prime, False returns previous prime.
            return_number_if_prime: True returns v if prime, False looks for neighbor.

        Returns:
            The previous or next prime number. Returns 0 if no previous prime exists.

        Note:
            Base method for get_next_prime(), get_previous_prime(),
            get_next_prime_inclusive(), get_previous_prime_inclusive()
        """
        if return_number_if_prime and Primes.is_prime(v):
            return v
    
        while True:
            if return_next_prime:
                v += 1
            else:
                v -= 1
                if v <= 1:
                    return 0
            if Primes.is_prime(v):
                return v

    def get_neighbor_prime(self, return_next_prime: bool, return_number_if_prime: bool) -> int:
        return Primes.get_neighbor_prime(self.the_number, return_next_prime, return_number_if_prime)


    @staticmethod
    def get_previous_prime(v: int) -> int:
        """
            Finds the prime number <b><i>before</i> v</b>.
            Will not return <b>v</b> whether it is prime or not.
        """
        return Primes.get_neighbor_prime(v, False, False)
    
    def get_previous_prime(self)-> int:
        return Primes.get_previous_prime(self.the_number)

    @staticmethod
    def get_next_prime(v: int) -> int:
        """
            Finds the prime number <b><i>after</i> v</b>.
            Will not return <b>v</b> whether it is prime or not.
        """        
        return Primes.get_neighbor_prime(v, True, False)
    
    def get_next_prime(self)->int:
        return Primes.get_next_prime(self.the_number)

    @staticmethod
    def get_previous_prime_inclusive(v: int) -> int:
        """
            Find the prime number before <b>v</b>. Returns <b>v</b> if prime.
        """
        return Primes.get_neighbor_prime(v, False, True)
    
    def get_previous_prime_inclusive(self) -> int:
        return Primes.get_previous_prime_inclusive(self.the_number)

    @staticmethod
    def get_next_prime_inclusive(v: int) -> int:
        """
            Find the prime number after <b>v</b>. Returns <b>v</b> if prime.
        """
        return Primes.get_neighbor_prime(v, True, True)
    
    def get_next_prime_inclusive(self)->int:
        return Primes.get_next_prime_inclusive(self.the_number)


    @staticmethod
    def is_a_pointer_prime(v: int) -> bool:
        """
        A prime number p is called a-pointer if the next prime number can be obtained
        by adding p to its sum of digits (a stands for additive).
        Example: 293 is an a-pointer prime since the next prime equals 293 + 2 + 9 + 3 = 307.
        """
        if not Primes.is_prime(v):
            return False
    
        next_number = v + Primes.get_sum_of_digits(v)
        return Primes.get_next_prime(v) == next_number

    def is_a_pointer_prime(self) -> bool:
        return Primes.is_a_pointer_prime(self.the_number)
    


    @staticmethod
    def is_m_pointer_prime(v: int) -> bool:
        """
        A prime number p is called m-pointer if the next prime number can be
        obtained by adding p to its product of digits (m stands for multiplicative).
        Example: 1231 is an m-pointer prime since the next prime equals
        1231 + 1 * 2 * 3 * 1 = 1237.
        """
        if not Primes.is_prime(v):
            return False
    
        next_number = v + Primes.get_product_of_digits(v)
        return Primes.get_next_prime(v) == next_number

    def is_m_pointer_prime(self) -> bool:
        return Primes.is_m_pointer_prime(self.the_number)



    @staticmethod
    def is_inter_prime(v: int) -> bool:
        """
        An interprime is a composite number that is the average
        of two consecutive primes.
        Example: 9 is interprime since it is the average of 7 and 11.
        """
        if Primes.is_prime(v):
            return False
    
        prev_prime = Primes.get_previous_prime(v)
        next_prime = Primes.get_next_prime(v)
    
        return prev_prime + next_prime == 2 * v

    def is_inter_prime(self) -> bool:
        return Primes.is_inter_prime(self.the_number)
    


    @staticmethod
    def get_distinct_prime_factors(v: int) -> list[int]:
        """Returns a sorted list of distinct prime factors of v."""
        return sorted(set(Primes.get_prime_factors(v)))

    def get_distinct_prime_factors(self) -> list[int]:
        return Primes.get_distinct_prime_factors(self.the_number)
    
    @staticmethod
    def is_droll(v: int) -> bool:
        """
        A droll number is one where the sum of even prime factors
        equals the sum of odd prime factors.
        Example: 72 = 2*2*2*3*3, even sum = 6, odd sum = 6.
        """
        prime_factors = Primes.get_prime_factors(v)
    
        even_total = sum(p for p in prime_factors if NumberTheory.is_even(p))
        odd_total = sum(p for p in prime_factors if NumberTheory.is_odd(p))
    
        return even_total > 0 and even_total == odd_total

    def is_droll(self) -> bool:
        return Primes.is_droll(self.the_number)
    



    @staticmethod
    def get_prime_lucky_numbers(v: int) -> list[int]:
        """Returns a list of lucky numbers up to v that are also prime."""
        return [n for n in NumberTheory.get_lucky_number_list(v) if Primes.is_prime(n)]

    def get_prime_lucky_numbers(self) -> list[int]:
        return Primes.get_prime_lucky_numbers(self.the_number)
    



    def is_co_prime(v: int) -> bool:
        pass

    def get_prime_list(v: int) -> list[int]:
        pass

    def get_lonely_number(v: int) -> int:
        pass

    def get_fortunate_numbers(v: int) -> int:
        pass

    def is_n_smooth(v: int) -> bool:
        pass

    def is_pierpont_prime(v: int) -> bool:
        pass

    @staticmethod
    def is_sphenic(v: int) -> bool:
        """
        A sphenic number is a product of exactly three distinct prime factors.
        Example: 30 = 2 * 3 * 5 is sphenic.
        """
        return len(Primes.get_prime_factors(v)) == 3 and \
               len(Primes.get_distinct_prime_factors(v)) == 3

    def is_sphenic(self) -> bool:
        return Primes.is_sphenic(self.the_number)