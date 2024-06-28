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
    def get_prime_factors(self = None, v: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        retVal = []
        our_number = v
        for i in range(2, v + 1):
            while our_number % i == 0:
                retVal.append(i)
                our_number /= i
        return retVal

    @staticmethod
    def is_semi_prime(self = None, v: int = None) -> bool:
        if v is None:
            v = self.get_the_number()
        another_list = []
        another_list = Primes.get_prime_factors(None, v)
        return len(another_list) == 2

    @staticmethod
    def sieve_of_eratosthenes(n: int, isPrime: bool) -> list[bool]:
        isPrime[0] = isPrime[1] = False
        for i in range(2, n + 1, 1):
            isPrime[i] = True
        p = 2
        while p * p <= n:
            if isPrime[p]:
                for i in range(p * 2, n + 1, p):
                    isPrime[i] = False
            p += 1

    @staticmethod
    def countDigit(n: int) -> float:
        return math.floor(math.log10(n) + 1)

    # Function to check if N is a 
    # Brilliant number
    @staticmethod
    def is_brilliant(self=None, n: int = None) -> bool:
        if n is None:
            n = self.get_the_number()
        """
        https://www.geeksforgeeks.org/brilliant-numbers/
        """
        flag = 0
        # Generating primes using Sieve 
        isPrime = [0] * (n + 1)
        Primes.sieve_of_eratosthenes(n, isPrime)

        # Traversing all numbers 
        # to find first pair 
        for i in range(2, n, 1):
            x = n // i

            if (isPrime[i] and
                    isPrime[x] and x * i == n):
                if Primes.countDigit(i) == Primes.countDigit(x):
                    return True
        return False

    @staticmethod
    def is_emirpimeses(self=None, v: int = None) -> bool:
        if v is None:
            v = self.get_the_number()
        reverse_number = NumberTheory.get_reverse_number(None, v)
        # print(f"{v}   {reverse_number}")
        if v != reverse_number:
            return Primes.is_semi_prime(None, v) and Primes.is_semi_prime(None, reverse_number)
        return False

    @staticmethod
    def is_chen_prime(self=None, v: int = None) -> bool:
        if v is None:
            v = self.get_the_number()
        if Primes.is_prime(None, v):
            return Primes.is_prime(None, v + 2) or Primes.is_semi_prime(None,v + 2)
        return False

    @staticmethod
    def is_emirp(self=None, v: int = None) -> bool:
        """An emirp (prime spelled backwards) is a prime number that results
        in a different prime when its decimal digits are reversed. This definition
        excludes this related palindrome primes.
        """
        if v is None:
            v = self.get_the_number()

        return Primes.is_prime(None, v) and Primes.is_prime(None, Primes.get_reverse_number(None, v))

    @staticmethod
    def is_good_prime(self=None, v: int = None) -> bool:
        """A good prime is a prime number whose square is greater than the product of
        any two primes at the same number of positions before and after it in the
        sequence of primes. To solve this, create a list of primes from zero to 3x the
        number. Iterate pointers forwards and backwards in matching jumps through list.
        """
        if v is None:
            v = self.get_the_number()
        the_prime_list = []
        small = large = 0
        if not Primes.is_prime(None, v):
            return False
        # Create a list of prime numbers up to 3 times v
        for i in range(2, v * 3 + 1):
            if Primes.is_prime(None, i):
                the_prime_list.append(i)

        if v in the_prime_list:
            ndx = the_prime_list.index(v)
            for ndxCounter in range(1, ndx + 1):
                small = the_prime_list[the_prime_list.index(v) - ndxCounter]
                large = the_prime_list[the_prime_list.index(v) + ndxCounter]
                if v * v < small * large:
                    return False
        return True

    @staticmethod
    def get_neighbor_prime(v: int, return_next_prime: int, return_number_if_prime: int) -> int:
        """
          @param v The number from which to start.
          @param returnNextPrime   Boolean -
            True: Return the next prime
            False: Return the previous prime
          @param returnNumberIfPrime Boolean -
            True: Return v if prime
            False: look for next number
          @return The previous or next prime number.
          Base method for get_next_prime(), get_previous_prime(), get_next_prime_inclusive(), get_previous_prime_inclusive()
        """
        if return_number_if_prime:
            if Primes.is_prime(None, v):
                return v
        while True:
            if return_next_prime:
                v += 1
                if Primes.is_prime(None, v):
                    return v
            else:
                v -= 1
                if v == 0:
                    return 0
                if Primes.is_prime(None, v):
                    return v
        return None

    @staticmethod
    def get_previous_prime(self = None, v: int = None) -> int:
        """
            Finds the prime number <b><i>before</i> v</b>.
            Will not return <b>v</b> whether it is prime or not.
        """
        if v is None:
            v = self.get_the_number()
        return Primes.get_neighbor_prime(v, False, False)

    @staticmethod
    def get_next_prime(self=None, v=None) -> int:
        """
            Finds the prime number <b><i>after</i> v</b>.
            Will not return <b>v</b> whether it is prime or not.
        """
        if v is None:
            v = self.get_the_number()
        return Primes.get_neighbor_prime(v, True, False)

    @staticmethod
    def get_previous_prime_inclusive(self=None, v: int = None) -> int:
        """
            Find the prime number before <b>v</b>. Returns <b>v</b> if prime.
        """
        if v is None:
            v = self.get_the_number()
        return Primes.get_neighbor_prime(v, False, True)

    @staticmethod
    def get_next_prime_inclusive(self=None, v: int = None) -> int:
        """
            Find the prime number after <b>v</b>. Returns <b>v</b> if prime.
        """
        if v is None:
            v = self.get_the_number()
        return Primes.get_neighbor_prime(v, True, True)

    @staticmethod
    def is_a_pointer_prime(self=None, v: int = None) -> bool:
        """
           A prime number  'p'  is called a-pointer if the next prime number can be obtained
            adding  'p'  to its sum of digits
            (here the 'a' stands for additive).
            For example, 293 is an a-pointer prime since the next prime is equal to 293 + 2 + 9 + 3 = 307.}
        """
        if v is None:
            v = self.get_the_number()
        if not Primes.is_prime(None, v):
            return False
        the_stack = []
        number = v
        the_stack.append(number)
        while number > 0:
            the_stack.append(number % 10)
            number /= 10
        nextNumber = 0
        while len(the_stack) > 0:
            nextNumber += the_stack.pop()
        if Primes.is_prime(None, nextNumber):
            return True
        return False

    @staticmethod
    def is_m_pointer_prime(self = None, v: int = None) -> bool:
        """
            A prime number  'p'  is called m-pointer if the next prime number can be
            obtained adding  'p'  to its product of digits (here the 'm' stands for
            multiplicative). For example, 1231 is a m-pointer prime since the next
            prime is equal to 1231 + 1 ⋅ 2 ⋅ 3 ⋅ 1= 1237.
        """
        if v is None:
            v = self.get_the_number()
        if not Primes.is_prime(None,v):
            return False
        the_stack = []
        number = v
        the_stack.append(number)
        while number > 0:
            the_stack.append(number % 10)
            number /= 10
        nextNumber = 0
        while len(the_stack) > 0:
            nextNumber *= the_stack.pop()
        return Primes.is_prime(None, nextNumber)

    @staticmethod
    def is_inter_prime(self = None, v: int = None) -> bool:
        if v is None:
            v = self.get_the_number()
        if Primes.is_prime(None,v):
            return False
        the_array = [0, 0]
        counter = v - 1
        while counter > 0:
            if Primes.is_prime(None,counter):
                the_array[0] = counter
                break
            counter -= 1
        counter = v
        while counter < v * 2:
            if Primes.is_prime(None,counter):
                the_array[1] = counter
                break
            counter += 1
        return (the_array[0] + the_array[1]) / 2 == v

    @staticmethod
    def get_distinct_prime_factors(self = None, v: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        theList = theList2 = []
        # theList = Primes.get_prime_factors(v)
        theList = Primes.get_prime_factors(None, v)
        myset = set(())
        for ele in theList:
            myset.add(ele)
        return list(myset)

    @staticmethod
    def is_droll(self = None, v=None) -> bool:
        if v is None:
            v = self.get_the_number()
        primeFactors = Primes.get_prime_factors(None, v)
        evenTotal = 0
        oddTotal = 0
        for p in primeFactors:
            if NumberTheory.is_even(None,p):
                evenTotal += p
            if NumberTheory.is_odd(None,p):
                oddTotal += p
        print("in droll: ", evenTotal, ' ', oddTotal, " ", primeFactors)
        if evenTotal > 0 and evenTotal == oddTotal:
            return True
        return False

    @staticmethod
    def get_prime_lucky_numbers(self = None, v: int = None) -> list[int]:
        if v is None:
            v = self.get_the_number()
        theList = NumberTheory.get_lucky_number_list(v)
        outputList = []
        for theNumber in theList:
            if Primes.is_prime(theNumber):
                outputList.append(theNumber)
        return outputList



    def is_co_prime(self) -> bool:
        pass

    def get_prime_list(self) -> list[int]:
        pass

    def get_lonely_number(self) -> int:
        pass

    def get_fortunate_numbers(self) -> int:
        pass

    def is_n_smooth(self) -> bool:
        pass

    def is_pierpont_prime(self) -> bool:
        pass
