#K:\JCSCHNEIDER\Courses\CITC 2375 Inet Software Dev\
#LectureForSpring23Source\SharedFolder\
#localFunctions.py

import functools
import timeit
import locale
import math
import random


@functools.lru_cache(maxsize=128)
def jugglersSequence(v):
    """Return a list of jugglers sequence calculated from passed number"""
    powerFactor = 0.0
    retVal = []
    while v > 1 :
        retVal.append(v)
        if(v%2 == 0):
            powerFactor = 0.5
        else:
            powerFactor = 1.5
        v = math.floor(v**powerFactor)
    retVal.append(1)
    return retVal


def jugglersSequenceAll(v):
    """Return a list of jugglers sequence, high water mark and number of steps calculated from passed number"""
    test = jugglersSequence(v)
    highWaterMark = getHighWater(test)
    countOfElements = len(test)
    return test, highWaterMark, countOfElements

    
def jugglersDictionary(v):
    """ Return the juggler's sequence in a dictionary with high water and steps """
##    retVal = {}
    x = jugglersSequence(v)
    y = getHighWater(x)
    z = len(x)
       
    retVal = { 'theNumber' : v,
                'seq' : x,
               'highWater' : y,
               'steps' : len(x) }               
    return retVal


    
def getHighWater(v):
    """ Return largest number from a list """
    maxValue = -1
    for i in v:    
        if(i > maxValue) :
            maxValue = i
    return(maxValue)



@functools.lru_cache(maxsize=128)
def collatzBkup(v):
    """Return the collatz conjecture list """
    retVal = []
    while v > 1 :
        retVal.append(v)
        if(v % 2 == 0):
            v=math.floor(v/2)
        else:
            v = math.floor(3.0*v+1)
    retVal.append(1)
    return retVal



@functools.lru_cache(maxsize=128)          
def isPrime(number):
    """Test to determine if number is prime"""
    isPrime = True
    for num in range(2,int(number ** 0.5) + 1):
        if number % num == 0:
            isPrime = False
            break
    return(isPrime)


@functools.lru_cache(maxsize=128)
def factorList(number):
    factorList = []
    for i in range(1,number+1):
        if(number %i == 0):
            factorList.append(i)
    return factorList


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


@functools.lru_cache(maxsize=128)
def findFib(n):
    #retVal = round(((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n  /  math.sqrt(5),0)
    retVal = math.floor(((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n  /  math.sqrt(5))
    return retVal


@functools.lru_cache(maxsize=128)
def getFactorSet(theNumber):
    counter = 1
    a = {1,}
    while counter <= theNumber:
        if theNumber % counter == 0:
            a.add(counter)
        counter += 1
    return a


def get_carol_numbers01(stop_value):
    '''One way to work with a list '''
    ret_list = []
    for the_value in range (stop_value):
        ret_list.append(get_carol_number(the_value))
    return ret_list


##def get_carol_number(theNumber):
def get_carol_number(theNumber):
    """ Return the carol number in the equation of 4^n - 2^n+1 -1"""
    carol_number = math.floor(4** theNumber - 2 ** (theNumber+1) -1)
    if carol_number > 0:
        return carol_number        


@functools.lru_cache(maxsize=128)    
def get_carol_number_list(stop_value):
    #the get_carol_number(0) and (1) return -2 and -1.
    # This won't work, ergo filter them out.
    ret_list = []
    for x in range(stop_value):
        testVal = get_carol_number(x)
        if testVal :
            ret_list.append(testVal)    
    return ret_list


def get_kynea_number(theNumber):
    """ Return the Kynea number in the equation of 4^n - 2^n+1 -1"""
    if theNumber > 0:        
        kynea_number = math.floor(4** theNumber + 2 ** (theNumber+1) -1)            
        return math.floor(kynea_number)
    return


@functools.lru_cache(maxsize=128)    
def get_kynea_number_list(stop_value):
    '''Rewrite above as a list comprehension'''
    ret_list = []
    for x in range(stop_value):
        testVal = get_kynea_number(x)
        if testVal : 
            ret_list.append(testVal)
    return ret_list




@functools.lru_cache(maxsize=128)
def get_leyland_number(the_number):
    ans = []
    x = 2
    y = 2
    #Outer loop for x from 2 to n
    while x <= the_number:
        #Inner loop for y from 2 to x
        while y <= x:
            temp = pow(x,y) + pow(y,x)
            ans.append(temp)
            y += 1
        x += 1
    return ans


## This code is contributed by rishabh_jain
## https://www.geeksforgeeks.org/leyland-number/
'''Print first n Leyland Number.'''
def leyland(n): 
    ans = [] 
    x = 2
    y = 2
  
    # Outer loop for x from 2 to n. 
    while x <= n : 
  
        # Inner loop for y from 2 to x. 
        y = 2
        while y <= x : 
  
            # Calculating x^y + y^x 
            temp = pow(x, y) + pow(y, x) 
  
            ans.append(temp); 
            y = y + 1
        x = x + 1
  
    # Sorting the all Leyland Number. 
    ans.sort(); 
  
    i = 0
  
    # Printing first n Leyland number.
    return_list = []
    while i < n : 
##        print(ans[i], end = " ")
        return_list.append(ans[i])
        i = i + 1
    return return_list
  
 
def get_prime_list(the_list):
    ret_list = []
    for x in range(len(the_list)):
        if isPrime(abs(the_list[x])):
            ret_list.append(the_list[x])
    return ret_list
    

def base_convert(n, basex=2):    
    sign = '-' if n<0 else ''
    n = abs(n)
    if n < basex:
        return str(n)
    s = ''
    while n != 0:
        s = str(n%basex) + s
        n = n//basex
    return sign+s


def area(a, b):
    return a * b


def hypotenuse(a, b):
    return math.hypot(a,b)

def rectangle(a,b):
    areaBuffer = area(a, b)
    perimeter = 2 * (a + b)
    hypot = hypotenuse(a,b)
    return areaBuffer, perimeter, hypot
    

def search4vowels(phrase:str)->set:
    """Display any vowels found in an inputted word """
    vowels = set('aeiou')    
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))



    
#value returning functions
def dice(numberOfDice,numberOfSides):
    """
    dice(numberOfDice, numberOfSides)
    
     Return the accumulated value of numberOfDice of 
    numberOfSides sided dice"""
    accumulator = 0
    x = numberOfDice
    while x > 0:
        accumulator += random.randint(1,numberOfSides)
        x -= 1
    return accumulator
    
    
        
def dice2(numberOfSides):
    """
        dice2(number of sides) 
         Return two random values, x and y """
    x = random.randint(1,numberOfSides)
    y = random.randint(1,numberOfSides)
    return x, y
    

def rectangleMeasurements(length, width):
    """
    rectangleMeasurements(number, number)
    Returns: Length, Width, Perimeter, Angle1, Angle2, Hypotenuse """
        
    perimeter = (2*length + 2*width)
    angle1 = math.degrees(math.atan(width/length))
    angle2 = math.degrees(math.atan(length/width))
    hyp = hypotenuse(length,width)
    return length, width, perimeter, angle1, angle2, hyp
        

def factorsFlask(number):
    """\nfactors(number)
     Returns a list of a number's factors and
     the number of factors and the sum of factors """
    i = 1
    summaryFactors = 0
    isPrime = False
    abundance = 0    
    isAbundant = False
    retVal = []  #List
    while i <= number:
        if number % i == 0:
            retVal.append(i)
            if i < number:
                summaryFactors += i
        i+=1
    if len(retVal) < 3:
        isPrime = True 

    abundance = summaryFactors
    if abundance > number:
        isAbundant = True
    if abundance == number:
        #abundance = "PERFECT" 
        isAbundant = ''
    abundance = abundance - int(number)
    if abundance == 0: abundance = "PERFECT"
    return retVal, len(retVal), summaryFactors, isPrime, abundance, isAbundant



    
def jugglers(compareNumber):
    """\njugglers(number)
     Return list of Juggler's sequence for a single number """    
    
    powerFactor = 0.0
    retVal = [] 
    while compareNumber > 1:
        retVal.append(compareNumber)
        if compareNumber % 2 == 0:
            powerFactor = 1/2
        else:
            powerFactor = 3/2
        compareNumber = math.floor(math.pow(compareNumber, powerFactor))
    retVal.append(1)
    return retVal, max(retVal), len(retVal)



    
def collatz(compareNumber):
    """\n collatz(number)
    Return list of Collatz Conjecture sequence for a single number """
    retVal = [] 
    while compareNumber > 1:
        retVal.append(compareNumber)
        if compareNumber % 2 == 0:
           compareNumber = math.floor(compareNumber / 2)
        else:
            compareNumber = math.floor(3.0*compareNumber + 1)
        
    retVal.append(1)
    #print(retVal)
    return retVal, max(retVal), len(retVal)


def randomValue():
    """ 
    randomValue()
    Return a random floating point number N such that 
    a <= N <= b for a <= b and b <= N <= a for b < a."""
    return random.uniform(1.0,10001.0)
    

def variableNumberOfArguments(*argv):
    """
    variableNumberOfArguments(*argv):
    Python program to illustrate   
    *args for variable number of arguments 
    Note: python does not support method overloading.
    """
    for arg in argv:  
        print (arg) 




def variableNumberOfArguments(arg1,*argv):   
# Python program to illustrate  
# *args with first extra argument 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 



"""
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
We use the name kwargs with the double star. The reason is because the double star allows us to pass through
keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
"""
def funWithDictionaries(**kwargs):
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
  

# Python program to illustrate  **kargs for  
# variable number of keyword arguments with 
# one extra argument. 
  
def funWithDictionaries02(arg1, **kwargs): 
    print(arg1, end=" ") 
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  


def averages(*argv):
    counter = summary = 0
    """Find average of a indeterminate group of numbers"""
    for arg in argv:
        counter += 1
        summary += arg
    
    return summary / counter 


"""
You may want to accept nearly-arbitrary named arguments for a series of reasons -- and that's what the **kw form lets you do.

The most common reason is to pass the arguments right on to some other function you're wrapping (decorators are one case of this,
but FAR from the only one!) -- in this case, **kw loosens the coupling between wrapper and wrappee, as the wrapper doesn't have
to know or care about all of the wrappee's arguments. Here's another, completely different reason:

d = dict(a=1, b=2, c=3, d=4)
if all the names had to be known in advance, then obviously this approach just couldn't exist, right? And btw, when applicable,
I much prefer this way of making a dict whose keys are literal strings to:

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

simply because the latter is quite punctuation-heavy and hence less readable.

When none of the excellent reasons for accepting **kwargs applies, then don't accept it: it's as simple as that.
IOW, if there's no good reason to allow the caller to pass extra named args with arbitrary names, don't allow that to
happen -- just avoid putting a **kw form at the end of the function's signature in the def statement.

As for using **kw in a call, that lets you put together the exact set of named arguments that you must pass,
each with corresponding values, in a dict, independently of a single call point, then use that dict at the single
calling point. Compare:

if x: kw['x'] = x
if y: kw['y'] = y
f(**kw)
to:

if x:
  if y:
    f(x=x, y=y)
  else:
    f(x=x)
else:
  if y:
    f(y=y)
  else:
    f()
Even with just two possibilities (and of the very simplest kind!), the lack of **kw is aleady making the second option absolutely untenable and intolerable -- just imagine how it plays out when there half a dozen possibilities, possibly in slightly richer interaction... without **kw, life would be absolute hell under such circumstances!
"""


"""
https://betterprogramming.pub/
how-you-make-sure-input-is-the-type-you-want-it-to-be-in-python-521f3565a66d
"""

'''
This means all characters in the string are letters.
Not even a space is allowed here.
'''
def is_string_only(check_input):
    if check_input.isalpha():
        return True
    return False

'''
    Use thusly:
    user_input = input(`')
    if user_input.isalpha():
        #do something
'''

"""
I’m using it to check if there are any spaces in the string and at the same time if the rest are letters.
"""
def is_string_with_space(check_input):
    valid = False
    if ' ' in check_input:
        for char in check_input:
            if char.isdigit():
                valid = False
            elif char.isalpha() or char.isspace():
                valid = True
    return valid

"""
Check for both letters and/or numbers
"""
def is_string_or_num(check_input):
    if check_input.isalnum():
        return True
    return False

"""
Check for integer
"""
def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

"""
Check for a floating point
"""
def is_float(check_input):
    if '.' in check_input:
        split_number = check_input.split('.')
        if len(split_number) == 2 and split_number[0].isdigit() and \
        split_number[1].isdigit():
            return True
    return False


def inputTester():
    while True:
        temp = input("Enter an integer")
        if lF.is_digit(temp):
            break
