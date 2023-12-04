'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import math
import functools
#from fontTools.misc.textTools import num2binary
#from pkg_resources import _sset_none, _sget_none
#from tkinter.constants import FALSE
from collections import deque
#from test.test_itertools import isEven, isOdd

ITERATIONS = 1000   


class NumberTheory:    
        
    def __init__(self, theNumber):
        self.__theNumber = theNumber
        
    def set_the_number(self, theNumber):
        self.__theNumber = theNumber
        
    def get_the_number(self):
        return self.__theNumber
    
    def get_square(self, v = None):
        if v == None:
            return self.__theNumber * self.__theNumber
        else:
            return v * v
            
    # https://www.scaler.com/topics/function-overloading-in-python/
    def get_cube(self, v = None):
        if v == None:
            return self.__theNumber * self.__theNumber * self.__theNumber
        else:
            return v * v * v
    
    def get_sum_of_squares(self, vList):        
        retVal = 0
        for int in vList:
            retVal += int * int
        return retVal

    def get_product_of_squares(self, vList):
        retVal = 0
        for int in vList:
            retVal *= int * int
        return retVal
    
    def get_sum_of_digits(self, aList):
        retVal = 0
        for integer in aList:
            retVal += integer
        return retVal
    
    def get_product_of_digits(self, aList):
        retVal = 0
        for integer in aList:
            retVal *= integer
        return retVal
   

    def number_to_list(self, the_number):
        '''
        Split an integer into a list of the digits
        ''' 
        retVal = deque([])
        string = str(the_number)
        for i in string:
            retVal.appendleft(int(i))
        return retVal
        
    def get_list_of_digits(self, v = None):
        '''
        Usage: provide java getListOfDigits() equivalency
        '''
        if v == None:
            v = self.get_the_number()
        return self.number_to_list(v)
    '''
    Return sum of a list
    aka sigma of a list
    '''       
    def sum_of_list(self,the_Collection):
        total = 0
        [total := total + x for x in the_Collection]
        return total        
        
    
    def multiple_of_list(self,the_Collection):
        total = 1
        [total := total * x for x in the_Collection]
        return total
    
    def is_prime(self, v = None):
        if v == None:
            v = self.get_the_number()
        stopVal = int(math.sqrt(v))         
        i = 2
        while i <= stopVal:
            if v % i == 0:
                return False
            i+=1
        return True

    def get_collatz(self, v = None):
        retVal = []
        if v == None:
            retVal.append(self.get_the_number())
            counter = self.get_the_number()
        else:
            retVal.append(int (v));
            counter = int(v)
        while counter > 1:
            if counter % 2 == 0:
                counter /= 2;
                counter = int(counter)
            else:
                counter = int(math.floor(3.0*counter+1))
            retVal.append(counter)
        return retVal
    
    def get_jugglers(self, v = None):
        factr = 0.0
        retVal = []
        if v == None:
            retVal.append(self.get_the_number())
            counter = self.get_the_number()
        else:
            retVal.append(v)
            counter = v
        while counter > 1:
            if counter % 2 == 0 :
                factr = .5
            else:
                factr = 1.5
            counter = int(math.floor(math.pow(counter, factr)))
            retVal.append(counter)
        return retVal
 
    
    
    def get_prime_factors(self, v = None):
        retVal = []
        if v == None:
            v = self.get_the_number()         
        for i in range(2, v):
            while v % i == 0:
                retVal.append(i)
                v /= i
        return retVal
    


    """ Starting to modify code to use list comprehensions"""
    def get_factors(self, v=None):  
        if v == None:
            v = self.get_the_number()        
        #numbers = range(1, v+1)        
        #factors = [i for i in numbers if v % i == 0]
        #factors = [i for i in range(1, v+1) if v % i == 0]
        return [i for i in range(1, v+1) if v % i == 0]
    
    
    
    """
    This could have been done with SUM, but then I wouldn't have 
    learned about list comprehensions
    """
    def get_factors_sum(self, v=None):
        total = 0
        if v == None:
            v = self.get_the_number()
        return [total := total + x for x in self.get_factors(v)]    
    
    """
    @author: Jeffrey Schneider    
    Sum of all proper divisors (factors) except itself, hence the subtraction.
    """    
    def get_aliquot_sum(self, v=None):
        total = 0
        if v == None:
            v = self.get_the_number()
        [total:= total + x for x in self.get_factors(v)]
        return total - v
    
    

    def get_reverse_number(self, v=None):
        rev = 0
        digit = 0
        if v == None:
            num = self.get_the_number()
        else:
            num = v
        
        while num != 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10
        return rev


    def get_reciprocal_number(self, v=None):
        if v == None:
            v = self.get_the_number()
        return 1.0 / v        
    
    
    
    def get_hex(self, v=None):
        retVal = ""
        hexList = [ "0","1","2","3","4","5","6","7","8", "9", "A", "B", "C", "D","E","F"]
        rem = 0
        if v == None:
            buffer = self.get_the_number()
        else:
            buffer = v
        while buffer > 0:
            rem = buffer % 16
            retVal = hexList[rem] + retVal
            buffer //= 16
            
        return retVal
     
    def get_octal(self, v=None):
        retVal= ""
        dlg  = [ "0", "1","2","3","4","5","6","7"]
        rem = 0
        if v == None:
            buffer = self.get_the_number()
        else:
            buffer = v 
        while buffer > 0:
            rem = buffer % 8
            retVal = dlg[rem] + retVal
            buffer //= 8
        return retVal
            
        
    def get_binary(self, v=None):
        if v == None:
            v = self.get_the_number()        
        retVal = '{0:b}'.format(v)
        return retVal
        
        
    def is_abundant(self, v=None):
        """
        Boolean.
        Is the number's aliquot sum greater than the number?
        """
        if v == None:
            v = self.get_the_number()   
        return self.get_aliquot_sum(v) > v
        

    def get_proper_divisors(self, v=None):
        retVal = []
        if v == None:
            v = self.get_the_number()
        for i in range(1,v+1):
            if v % i == 0:
                retVal.append(i)
        return retVal
            

    

    def get_abundance(self, v=None):
        if v==None:
            v = self.get_the_number()
        return self.get_aliquot_sum(v) - v
   
    
        
    def is_even(self, v=None):
        if v == None:
            v = self.get_the_number()        
        return v % 2 ==0  
        
        
    def is_perfect(self, v= None):
        if v == None:
            v = self.get_the_number()
        return self.get_abundance(v) == 0   
        
   
    def get_kynea(self, v = None):
        if v == None:
            v = self.get_the_number()
            
        kyneaA = math.pow(4.0, v)
        kyneaB = math.pow(2.0, v +1.0)
        kyneaFinal = kyneaA + kyneaB - 1.0
        return int(kyneaFinal)
            
            
    def get_carol(self, v = None):
        if v == None:
            v = self.get_the_number()
        carolA = math.pow(4.0, v )
        carolB = math.pow(2.0, v + 1)
        carolFinal = carolA - carolB - 1.0
        return int(carolFinal)
    
    #@functools.cache
    def get_factorial(self, v=None):
        retVal = 1
        if v == None:
            v = self.get_the_number()
        [retVal := retVal * i for i in range(1,v+1)]
        return retVal    
 
    def get_sigma(self, v=None):
        if v == None:
            v = self.get_the_number()
        if v == 1:
            return 1
        result = 0
        [result := result + x for x in range(1, v+1) if v % x == 0]
        return result    
        
    def get_catalan(self, v=None):
        if v == None:
            v = self.get_the_number()        
        catA = self.get_factorial(2*v)
        catB = self.get_factorial(v + 1)
        catC = self.get_factorial(v )
        catFinal = catA / (catB * catC);
        return catFinal
        
     
    def get_fibonacci_list(self, v=None):
        if v == None:
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
    
    def get_fibonacci_like(self, v=None, number1=None, number2=None):
        if v == None:
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
        
    def isFiboDiv(self,v=None):
        if v == None:
            v = self.get_the_number()
        for i in range(1,len(v)):
           left = v[:i]
           right = v[i:]
           print(left, " ", right)
           return self.get_fibonacci_like(v, left, right)
           

       # sb = []
       # sb.append(v)
       # left = 0
       # right = 0
       # for i in range(1,len(sb)+1):
        #    left = 
            
            
             
    def get_lucas_list(self, v = None):
        retList = []
        if v == None:
            v = self.get_the_number()
        num1 = 2;
        num2 = 1;
        counter = 0
        
        while counter < v:
            retList.append(num1)
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            counter+=1
        return retList
            
            
    def get_motzkin(self, v=None):
        memo = {}
          
        if v == None:
            v = self.get_the_number()
         
        if (v == 0) or ( v == 1):
            return 1
        
        if v in memo:
            return memo.get(v)
        
        m1 = self.get_motzkin(v - 1)
        m2 = self.get_motzkin(v - 2)  
        
        firstPart = (2 * v + 1) * m1
        secondPart = (3 * v - 3) * m2
        lastPart = v + 2
        retVal = (firstPart + secondPart) / lastPart
        memo[v] = retVal
        
        return retVal
     
    def is_primitive_abundant(self, v=None):
        if v == None:
            v = self.get_the_number() 
        properDivisorList = []           
                      
        if not self.is_abundant(v):        
            return False
        else:
            properDivisorList = self.get_factors(v)
            ''' get_factors includes the number at the end.  We don't want the number included, lets pop() it off'''
            properDivisorList.pop()            
            for i in properDivisorList:
                if self.is_abundant(i):         
                    return False
        return True           
       
    '''
    @author: Jeffrey Schneider
    @see https://www.youtube.com/watch?v=uuMwz47LV_w
    '''
    def is_keith_number(self, v=None):
        if v == None:
            v = self.get_the_number()
        buffer_sum_of_digits = 0
        #list_of_digits is a deque
        list_of_digits = self.number_to_list(v)
        while buffer_sum_of_digits < v:
            buffer_sum_of_digits = self.sum_of_list(list_of_digits)
            if buffer_sum_of_digits == v:
                return True
            list_of_digits.appendleft(buffer_sum_of_digits)
            list_of_digits.pop()    #Throw away this value
        return False
    
     
    def get_amicable_number(self, v=None):   
        if v == None:
            v = self.get_the_number()
        first_divisor_sum = self.get_aliquot_sum(v)
        second_divisor_sum = self.get_aliquot_sum(first_divisor_sum)
        if second_divisor_sum == v :
            return first_divisor_sum
    
    def get_betrothed_number(self, v=None):
        if v == None:
            v = self.get_the_number()
        thisNumber = self.sum_of_list(self.get_non_trivial_divisors(v))
        thatNumber = self.sum_of_list(self.get_non_trivial_divisors(thisNumber))
        if thatNumber == v:
            return thisNumber
        return 0

    
    def get_non_trivial_divisors(self, v=None):
        if v == None:
            v = self.get_the_number()
        my_list = sorted(self.get_factors(v))         
        my_list = my_list[1:-1]    
        return my_list
    
    
    def get_cake_number(self, v=None):
        if v == None:
            v = self.get_the_number()        
        return int ((1.0 / 6.0) * (pow(v, 3) + 5 * v + 6))
    
    
       
    '''https://codereview.stackexchange.com/questions/12119/printing-nth-bell-number'''
    def get_bell_number(self, v=None):
        if v == None:
            v = self.get_the_number()
        return (1/math.e) * sum([(k**v)/(math.factorial(k)) for k in range(ITERATIONS)])
        
    def get_centered_polygonal_number(self, sideNumber, v=None):
        if v == None:
            v = self.get_the_number()            
        return int(sideNumber * v * (v + 1) / 2 + 1)
    
    
    def get_polygonal_number(self, sides=None, number=None):
        if sides == None:
            sides = self.get_the_number()
        if number == None:
            number = 10
        s_minus_two = sides - 2
        s_minus_four = sides - 4
        return (1 / 2.0) * (s_minus_two * pow(number, 2.0) - s_minus_four * number);
        
        
        
        
    def get_primorial(self, v=None):
        if v == None:
            v = self.get_the_number()  
        summary = 1
        counter = 1
        number_of_primes = 0
        while number_of_primes <= v:
            if self.is_prime(counter):
                summary *= counter
                number_of_primes += 1
            counter += 1
        return summary
    
    

    def get_pell_list(self, v=None):
        if v == None:
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
     
    def get_pell(self, v=None):
        theList = []        
        if v == None:
            v = self.get_the_number()
        theList = self.get_pell_list(v)
        theStack = [x for x in theList]
        return theStack.pop()

    
    def get_jacobsthal_list(self, v=None):
        if v == None:
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
    
    def get_jacobsthal(self, v=None):        
        if v == None:
            v = self.get_the_number()
        theList = []
        theList = self.get_jacobsthal_list(v)
        theStack = [x for x in theList]
        return theStack.pop()
    
    
    def get_alternating_factorial(self, v=None):
        if v == None:
            v = self.get_the_number()
        theDictionary = {}
        theDictionary[1] = 1
        theDictionary[2] = 1
        for i in range(3,v+1):
            theDictionary[i] = self.get_factorial(i) - theDictionary[i-1]
        return theDictionary.get(v)
        
    def is_deficient(self, v=None):
        if v == None:
            v = self.get_the_number()
        return self.get_aliquot_sum(v) < v

    
    def is_super_abundant(self, v=None):
        if v == None:
            v = self.get_the_number()
        M = 0.0
        N = self.get_sigma(v) / v
        for i in range(1,v):
            M = self.get_sigma(i)/i
        if M >= N:
            return False
        return True

    def gcd(self, b, n):
        if n == 0:
            return b
        return self.gcd(n, b%n)

    def lcm(self, a, b=None):
        if b == None:
            b = self.get_the_number()
        return a * (b / self.gcd(a,b))
    
    def power(self, b, exp, n):
        if exp == 0:
            return 1
        result = self.power(b, exp/2, n) % n
        result = ( result * result) %n
        if exp %2 == 1:
            result = (result * b) %n
        return result

    def is_carmichael(self, v=None):
        if v == None:
            v = self.get_the_number()
        for b in range(2,v+1):
            if (self.gcd(b, v) == 1) and (self.power(b, v-1, v) != 1):
                return False
        return True

    # Function to find the N-th
    # icosikaipentagon number
    def isDNum(self,n):
        if n == None:
            n = self.get_the_number()
        # number should be
            # greater than 3
        if n < 4:
            return False
     
        # Check every k in range 2 to n-1
        for k in range(2, n):
            numerator = pow(k, n - 2) - k
            #print("Numerator: " , numerator)
            hcf = math.gcd(n, k)
     
            # condition for D-Number
            if(hcf ==1 and (numerator % n) != 0):
                return False
        return True
 
    
    def get_lazy_caterer(self, v=None):
        if v == None:
            v = self.get_the_number()
        return (v * v + v + 2) / 2
        
    def get_cullen(self, v=None):
        if v == None:
            v = self.get_the_number()
        return v * math.pow(2, v) + 1
    
    def is_co_prime(self, bNumber, v=None):   
        if v == None:
            v = self.get_the_number()
        
        if self.gcd(bNumber, v) == 1:
            return True
        return False
    
    #https://www.geeksforgeeks.org/compositorial-of-a-number/
    # Python3 program to find Compositorial
# of composite numbers

# Function to check
# if a number is composite.
    def isComposite(self,n=None):
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
        while(i * i <= n):            
            if (n % i == 0\
                or n % (i + 2) == 0):
                return True
            i = i + 6
            
        return False
    
# This function stores all
# Composite numbers less than N
    def Compositorial_list(self,n=None):
        if n == None:
            n = self.get_the_number()
        myList = []
        l = 0
        for i in range(4, 10**6):
            if l < n:
                if self.isComposite(i):
                    myList.append(i)
                    l+= 1
        return myList
    
    
    
# Function to calculate the
# Compositorial of n
    def calculateCompositorial(self,n = None):
        if n == None:
            n = self.get_the_number()
        total = 1
        myList = self.Compositorial_list(n)
        return self.multiple_of_list(myList)
        
    
        
    def is_curzon(self, v=None):
        if v == None:
            v = self.get_the_number()
        a = 2 ** v + 1
        b = 2 * v + 1
        return a % b == 0 
        

    
    def get_totatives(self, v=None):
        if v == None:
            v = self.get_the_number()
        retList = []
        counter = 1
        while counter <= v:
            if self.is_co_prime(v, counter):
                retList.append(counter)
            counter += 1
        return retList
            
        

    def eulersPhi(self,v=None):
        if v == None:
            v = self.get_the_number()
        result = 1  
        for i in range(2, v):
            if(self.gcd(i, v) == 1):
                result += 1
        return result

   
    def is_de_polignac(self,v=None):
        if v == None:
            v = self.get_the_number()
        if not self.is_even(v):
            for p in range(1, v):
                if self.is_prime(p):
                    for k in range (1, p):
                        if v - p == 2**k:
                            return False
            return True
        return False  
        
   
   #get_prime_factors 
    def is_droll(self, v=None):
        if v == None:
            v = self.get_the_number()
        primeFactors = self.get_prime_factors(v)
        evenTotal= 0
        oddTotal = 0
        for p in primeFactors:
            if self.is_even(p):
                evenTotal += p  
            if self.is_odd(p):
                oddTotal += p
        print("in droll: ", evenTotal , ' ' , oddTotal, " ", primeFactors)
        if evenTotal > 0 and evenTotal == oddTotal:
                return True
        return False


    def is_odd(self, v = None):
        if v == None:
            v = self.get_the_number()
        return v % 2 != 0
             

    def is_happy(self, v=None):
        the_set = set([])
        if v == None:
            v = self.get_the_number()
        a = self.get_sum_of_squares(self.get_list_of_digits(v))
        while a != 1:
            a = self.get_sum_of_squares(self.get_list_of_digits(a))
            if a in the_set:
                return False
            the_set.add(a)
        return True


    
    #Line 3505 from NumberTHeory.java
    def get_lucky_number_list(self, stop_value=None):
        pass
        if stop_value == None:
            stop_value = self.get_the_number()            
        theList = list()
        retVal = list()
        retVal.append(1) #force the first lucky number in
        next_surviving_number = 1
        pass_number = 1
        for i in range(1, stop_value+1):
            theList.append(i)
        #2 is not a lucky number
        next_surviving_number = 2
        theList = self.getSievedList(theList, next_surviving_number)

        while pass_number < len(theList) + 1:
            next_surviving_number = theList[pass_number + 1]
            retVal.append(next_surviving_number)
            theList = self.getSievedList(theList, next_surviving_number)

        return retVal
    
    #Line 3544 from NumberTheory.java
    def getSievedList(self, theList, sieveFactor):
        returnList = []
        counter = 1
        for number in range(theList):
            if counter % sieveFactor != 0:
                returnList.append(number)
            counter += 1
        return returnList
        
    def get_double_factorial():
        pass

    def get_rep_unit():
        pass

    def is_honaker_prime():
        pass

    def get_ormiston():
        pass

    def split_the_number_in_two():
        pass

    def get_dicksons_method():
        pass

    def get_factor_pairs():
        pass

    def get_divisor_function():
        pass

    def get_fermat_primes():
        pass

    def get_junction_numbers():
        pass

    def get_pell_list02():
        pass

    def get_powerful_number():
        pass


    def get_pronic():
        pass

    def permute():
        pass

    def get_leyland():
        pass


    def get_saint_exupery():
        pass


    def get_string_list_of_digits():
        pass

    def is_achilles():
        pass

    def is_admirable():
        pass

    def is_alternating():
        pass

    def is_amenable():
        pass

    def the_queue(self):            
        queue = []
        theList = self.get_factors(3600)
        for i in theList:
            queue.append(i)
        while len(queue) > 0:
            print(queue.pop(), end=' ')        
        print()


    '''
    def is_antiperfect(self, v=None):        
        if v == None:
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

    def isApocalyptic():
        pass

    def isArithmetic():
        pass
		
    def isAstonishing():
        pass
    def isAutomorphic():
        pass 
    def isBalancedPrime():
        pass
    def isCanadaNumber():
        pass
    def isCarmichael():
        pass
    def isCurzon():
        pass
    def isCyclic():
        pass
    def isDNumber():
        pass
    def isDPowerful():
        pass
    def	isDeceptive():pass
    def	isDeficient():pass
    def	isDicksonsMethod():pass
    def	isDigitsSorted():pass
    def	isDivisibleBy():pass
    def	isDroll():pass
    def	isDuffinian():pass
    def	isEconomical():pass
    def	isEnlightened():pass
    def	isEquidigital():pass
    def	isEsthetic():pass
    def	isEven():pass
    def	isEvil():pass
    def	isFiboDiv():pass
    def	isFrugal():pass
    def	isGapful():pass
    def	isGilda():pass
    def	isGiuga():pass
    def	isHappy():pass
    def	isHarmonicDivisorNumber():pass
    def	isHarshad():pass
    def	isHighlyComposite():pass
    def	isHoaxNumber():pass
    def	isHungry():pass
    def	isHyperPerfect():pass
    def	isIdoneal():pass
    def	isInsolite():pass
    def	isKaprekar():pass
    def	isKatadrome():pass
    def	isLynchBell():pass
    def	isMagnanimous():pass
    def	isMetadrome():pass
    def	isModest():pass
    def	isMoran():pass
    def	isNarcissistic():pass
    def	isNude():pass
    def	isPalPrime():pass
    def	isPalindromic():pass
    def	isPerfect():pass
    def	isPerfectPower():pass
    def	isPernicious():pass
    def	isPoulet():pass
    def	isPowerOfTwo():pass
    def	isPowerful():pass
    def	isPractical():pass
    def	isPrimitiveAbundant():pass
    def	isPrimitiveAbundantBkup():pass
    def	isPronic():pass
    def	isProthNumber():pass
    def	isRare():pass
    def	isSastry():pass
    def	isSastry():pass
    def	isSphenic():pass
    def	isSquareFree():pass
    def	isSuperD():pass
    def	isSuperabundant():pass
    def	getHarmonicMean():pass
    def	getPolygonalNumber():pass
    def	getReciprocalNumber():pass
    def	abs():pass







 















                 
    #sum_of_list                
            
            
            
                
##################################################################
    def get_end_point(self,lat1,lon1,bearing,d):
        R = 6371                     #Radius of the Earth
        brng = math.radians(bearing) #convert degrees to radians
        d = d*1.852                  #convert nautical miles to km
        lat1 = math.radians(lat1)    #Current lat point converted to radians
        lon1 = math.radians(lon1)    #Current long point converted to radians
        lat2 = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng))
        lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
        lat2 = math.degrees(lat2)
        lon2 = math.degrees(lon2)
        return (lat2, lon2)


    def get_bearing(self,lat1, lon1, lat2, lon2):
        dLon = (lon2 - lon1)
        x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
        y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) -\
            math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) *\
            math.cos(math.radians(dLon))
        brng = math.atan2(x,y)
        brng = math.degrees(brng)
        return brng

        

