from NumberTheory import NumberTheory
import math


class Primes(NumberTheory):
    '''
    Recreated 10/22/2023 by 
    @author   Jeffrey Schneider
    '''
    def __init__(self, theNumber):
        super().__init__(theNumber)        


    def get_prime_factors(self, v = None):        
        if v == None:
            v = self.get_the_number()
        retVal = []
        our_number = v
        for i in range(2, v+1):
            while our_number % i == 0:
                retVal.append(i)
                our_number /= i
        return retVal
    
    def is_semi_prime(self, v=None):
        if v == None:
            v = self.get_the_number()
        another_list = []
        another_list = self.get_prime_factors(v)
        return len(another_list) == 2


    def sieve_of_eratosthenes( self, n, isPrime):
        isPrime[0] = isPrime[1] = False
        for i in range(2, n+1, 1):
            isPrime[i] = True
        p = 2
        while p * p <= n:
            if isPrime[p] == True:
                for i in range(p * 2, n + 1, p):
                    isPrime[i] = False
            p += 1

    def countDigit(self, n):
        return math.floor(math.log10(n) + 1)

    # Function to check if N is a 
    # Brilliant number 
    def is_brilliant(self, n=None):
        if n == None:
            n = self.get_the_number()
        '''
        https://www.geeksforgeeks.org/brilliant-numbers/
        '''    
        flag = 0   
        # Generating primes using Sieve 
        isPrime = [0] * (n + 1) 
        self.sieve_of_eratosthenes(n, isPrime) 
   
        # Traversing all numbers 
        # to find first pair 
        for i in range(2, n, 1): 
            x = n // i 
   
            if (isPrime[i] and 
                isPrime[x] and x * i == n): 
                if (self.countDigit(i) == self.countDigit(x)):
                    return True   
   
        return False 
    
    def is_emirpimeses(self, v = None):
        if v == None:
            v = self.get_the_number()
        reverse_number = self.get_reverse_number(v)
        #print(f"{v}   {reverse_number}")
        if v != reverse_number:            
            return self.is_semi_prime(v) and self.is_semi_prime(reverse_number)
        return False
    
    def is_chen_prime(self, v = None):
        if v == None:
            v = self.get_the_number()
        if super().is_prime(v):
            return super().is_prime(v + 2) or self.is_semi_prime(v+2)
        return False

    def is_emirp(self, v = None):
        '''An emirp (prime spelled backwards) is a prime number that
	          results in a different prime when its decimal digits are reversed.
	          This definition excludes this related palindrome primes.
        '''
        if v == None:
            v = self.get_the_number()

        return super().is_prime(v) and super().is_prime(super().get_reverse_number(v))



    def is_good_prime(self, v=None):
        '''A good prime is a prime number whose square is greater than the product of
	  any two primes at the same number of positions before and after it in the
	  sequence of primes. To solve this, create a list of primes from zero to 3x
	  the number. Iterate pointers forwards and backwards in matching jumps through
	  list.
        '''
        if v == None:
            v = self.get_the_number()
        the_prime_list = []
        small = large = 0
        if not super().is_prime(v):
            return False
        # Create a list of prime numbers up to 3 times v
        for i in range(2, v * 3 + 1):
            if super().is_prime(i):
                the_prime_list.append(i)

        if v in the_prime_list:
            ndx = the_prime_list.index(v)
            for ndxCounter in range(1, ndx+1):                
                small = the_prime_list[the_prime_list.index(v) - ndxCounter]
                large = the_prime_list[the_prime_list.index(v) + ndxCounter]
                if v*v < small*large:
                    return False
        return True


    def get_neighbor_prime(self, v, return_next_prime, return_number_if_prime):
        '''
          @param v The number from which to start.
		  @param returnNextPrime   Boolean - True: Return the next prime  False: Return the previous prime
		  @param returnNumberIfPrime Boolean - True: Return v if prime   False: look for next number
		  @return The previous or next prime number. 
          Base method for get_next_prime(), get_previous_prime(), get_next_prime_inclusive(), 
          get_previous_prime_inclusive()
        '''        
        if return_number_if_prime:
            if super().is_prime(v):
                return v
        while True:
            if return_next_prime:
                v += 1
                if super().is_prime(v):
                    return v
            else:
                v -= 1
                if v == 0:
                    return 0
                if super().is_prime(v):
                    return v


    def get_previous_prime(self, v=None):
        '''
            Finds the prime number <b><i>before</i> v</b>.  
	        Will not return <b>v</b> whether it is prime or not.	 
        '''  
        if v == None:
            v = self.get_the_number()         
        return self.get_neighbor_prime(v, False, False)
    

    def get_next_prime(self, v=None):
        '''
            Finds the prime number <b><i>after</i> v</b>.  
	        Will not return <b>v</b> whether it is prime or not.	 
        '''  
        if v == None:
            v = self.get_the_number()
        return self.get_neighbor_prime(v, True, False)
    

    def get_previous_prime_inclusive(self, v=None):
        '''
            Find the prime number before <b>v</b>. Returns <b>v</b> if prime.
        '''
        if v == None:
            v = self.get_the_number()         
        return self.get_neighbor_prime(v, False, True)

    def get_next_prime_inclusive(self, v=None):
        '''
            Find the prime number after <b>v</b>. Returns <b>v</b> if prime.
        '''
        if v == None:
            v = self.get_the_number()         
        return self.get_neighbor_prime(v, True, True)

        

    def is_a_pointer_prime(self, v=None):
        '''
           A prime number  'p'  is called a-pointer if the next prime number can be obtained 
	    adding  'p'  to its sum of digits (here the 'a' stands for additive).
	    For example, 293 is an a-pointer prime since the next prime is equal to 
        293 + 2 + 9 + 3 = 307.}	 
        '''
        if v == None:
            v = self.get_the_number()                
        if not super().is_prime(v):
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
        if super().is_prime(nextNumber):
            return True
        return False
        


    def is_m_pointer_prime(self, v=None):
        '''
            A prime number  'p'  is called m-pointer if the next prime number can be obtained 
	    adding  'p'  to its product of digits (here the 'm' stands for multiplicative).
	    For example, 1231 is a m-pointer prime since the next prime is equal to 
        1231 + 1 ⋅ 2 ⋅ 3 ⋅ 1= 1237.	  
        '''
        if v == None:
            v = self.get_the_number()
        if not super().is_prime(v):
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
        if super().is_prime(nextNumber):
            return True
        return False


    def is_inter_prime(self, v=None):
        if v == None:
            v = self.get_the_number()
        if super().is_prime(v):
            return False
        the_array = [0, 0]
        counter = v - 1
        while counter > 0:
            if super().is_prime(counter):
                the_array[0] = counter
                break
            counter -= 1
        counter = v
        while counter < v * 2:
            if super().is_prime(counter):
                the_array[1] = counter
                break
            counter += 1
        return (the_array[0] + the_array[1] )/ 2 == v
        

    
    def get_distinct_prime_factors(self, v=None):
        if v == None:
            v = self.get_the_number()
        theList = theList2 = []
        theList = super().get_prime_factors(v)
        myset = set(())
        for ele in theList:
            myset.add(ele)
        return list(myset)


    def get_prime_lucky_numbers(self, v=None):
        if v == None:
            v = self.get_the_number()
        
        



    def is_co_prime():
        pass

    def get_prime_list():
        pass

    def get_longely_number():
        pass

    

    

    def get_fortunate_numbers():
        pass

    def is_n_smooth():
        pass

    def is_pierpont_prime():
        pass

    






        

    
    
