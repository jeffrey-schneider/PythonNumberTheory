'''
Created on Dec 6, 2022

@author: JCSchneider
'''
from NumberTheory import *
#from test.dtracedata import instance
#from pickle import INST

def main():

    print("In main")
    instance = NumberTheory(9)   
     
    print("Is ", instance.get_the_number(), " even?")
    print(instance.is_even())
    x = 12
    print("Is ", x, " even? ", instance.is_even(x))
          
          
    
    print(instance.get_the_number())
    instance.set_the_number(27)
    print(instance.get_square())
    print("Is prime? " , instance.is_prime())
    
    print("Collatz 27")
    for i in instance.get_collatz():
        print(i, end=" ")
    print()
    print("Collatz 43")
    for i in instance.get_collatz(43):
        print(i, end=" ")
    print()
    
    print("Jugglers 37")
    instance.set_the_number(37)
    for i in instance.get_jugglers():
        print(i, end=" ")
    print()
    print("Jugglers 45")
    for i in instance.get_jugglers(45):
        print(i, end=" ")
    print()
    
    
    print("Prime Factors 3600:")
    instance.set_the_number(3600)    
    for i in instance.get_prime_factors():
        print(i, end=" ")
    print()
    print("Prime Factors 60:")
        
    for i in instance.get_prime_factors(60):
        print(i, end=" ")
    print()
    
    
    print("Factors of 3600")
    for i in instance.get_factors():
        print(i, end=' ')
    print()
    
    print("Factors of 60")
    for i in instance.get_factors(60):
        print(i, end=' ')
    print()
    
    
    print("Reversed 43")
    instance.set_the_number(43)
    print(instance.get_reverse_number())
    
    print("Reciprocal 43")
    print(instance.get_reciprocal_number())
    
    print("To hex 76576500")
    instance.set_the_number(76576500)
    print(instance.get_hex())
    
    print("Is abundant 12")
    instance.set_the_number(12)
    print(instance.is_abundant())
    x = 41
    print(x, " ", instance.is_abundant(x))
    
    
    print(instance.get_the_number(), " ", instance.get_abundance())
    print(x, " ", instance.get_aliquot_sum(x), " ", instance.get_abundance(x))
    
    print("Get factors sum: ", instance.get_factors_sum(x))
    
    x = 9
    instance.set_the_number(x)
    print("Sigma: " , instance.get_sigma())
    print("Sigma: " , instance.get_sigma(x * 10))
    
    instance.set_the_number(20)
    print("Catalan ", instance.get_catalan())
    print("Catalan ", instance.get_catalan(15))
    
    print("get_fibonacci_list", instance.get_fibonacci_list())
    print("get_fibonacci_list", instance.get_fibonacci_list(15))
    
    
    instance.set_the_number(15)
    print("get_motzin", instance.get_motzkin())
    print("get_motzin", instance.get_motzkin(20))
    
    instance.set_the_number(10)
    print("getPellList: " , instance.get_pell_list())
    print("getPellList: " , instance.get_pell_list(12))
    print("getPell: " , instance.get_pell())
    print("getPell: " , instance.get_pell(12))
    
    instance.set_the_number(15)
    print("getJacobsthalList ", instance.get_jacobsthal_list())
    print("getJacobsthalList ", instance.get_jacobsthal_list(12))
    instance.set_the_number(12)
    print("getJacobsthal ", instance.get_jacobsthal())
    print("getJacobsthal ", instance.get_jacobsthal(15))
    
    instance.set_the_number(21)
    print("alternating Factorial: " , instance.get_alternating_factorial())

    instance.set_the_number(16)
    print("is Deficient: ", instance.is_deficient())
    print("is Deficient: ", instance.is_deficient(60))

    print("gcd: ", instance.gcd(8,12))
    print("lcm:  ", instance.lcm(15, 75))

    print("https://stackoverflow.com/questions/51826611/speed-up-a-search-for-carmichael-numbers")
    instance.set_the_number(6601)
    #print(instance.is_carmichael())
    #print(instance.is_carmichael(1105))

    print("D-Numbers")
    for n in range(1,500):
        if instance.isDNum(n):
            print(n, end=' ')
    print()


    print("Cake Number")
    for n in range(1,25):
        print(instance.get_cake_number(n))

    print("Cake Number")
    print(instance.get_the_number(), " ", instance.get_cake_number())

    print("Lazy Caterer")
    for n in range(1,25):
        print(instance.get_lazy_caterer(n))
    print(instance.get_the_number(), " ", instance.get_lazy_caterer())
    
    
    print("Primitive Abundant")    
    print(instance.is_primitive_abundant(24))
    

    print("https://forum.generic-mapping-tools.org/t/how-to-calculate-coordinates-from-bearing-distance/1217")
    lat2, lon2 = instance.get_end_point(lat1 = 50, lon1=8,bearing=310, d=23)
    print(lat2, " ", lon2)

    bearing = instance.get_bearing(lat1 = 50, lon1 = 8, lat2=50.24533,lon2=7.54112)
    print(bearing)

    bearing = instance.get_bearing(lat1 = 30.07134, lon1 = -97.23076,
                                   lat2=30.0709,lon2=-97.22907)
    print(bearing)                               
    
    print()
    instance.set_the_number(30)
    print("is 3 abundant? ", instance.is_abundant(3))
    print("is_primitive_abundant", instance.is_primitive_abundant())
    print("is_primitive_abundant", instance.is_primitive_abundant(3600))
    
    print("Superabundant")
    print("120 is, 5 is not")
    print(instance.is_super_abundant(120))
    print(instance.is_super_abundant(5))
    
    print("Keith Number")
    for i in range(10, 5000):        
        if (instance.is_keith_number(i)):
            print(i)
    
    
    
    print("Betrothed Number")    
    for i in range(48, 1000):
        betrothed = instance.get_betrothed_number(i)
        if betrothed > 0:
            print("Number: {0:3d}  Betrothed: {1:5.0f}".format(i, instance.get_betrothed_number(i)))
    
        
    print("Cake Numbers")
    n = 0
    while n < 5:        
        print("Cuts: {0:3d}  Pieces: {1:5.0f}".format(n, instance.get_cake_number(n)))
        n += 1
        
        
    print("Lazy Caterer's Numbers:");
    n = 0;
    while n < 5 :        
        print("Cuts: {0:3d}  Pieces: {1:5.0f}".format(n, instance.get_lazy_caterer(n)))
        n += 1
    
    print("Bell's Numbers:")
    n = 0;
    while n <= 50:
        print("Number: {0:3d}  Bell: {1:5.0f}".format(n, instance.get_bell_number(n)))
        n += 1
    
    print("Centered polygonal numbers")
    for j in range(3,5):
        print("Sides {0:4d}".format(j))
        for i in range(0,5):
            print("{0:4d}  {1:d}".format(i, instance.get_centered_polygonal_number(j, i))) 
            

    print("Polygonal Numbers")
    for outer in range(2, 25):
            print(" {0:4d} ".format(outer), end = ' ')
            for inner in range(1, 11):            
                print(" {0:.0f} ".format(instance.get_polygonal_number(outer, inner)), end = ' ')
            print()            
        

    print("----Number  -> Factorials -> Primorials")
    print("is 11 prime? ", instance.is_prime(11))
    for i in range(26):
        print("{0}  {1:,} / {2:,}".format(i, instance.get_factorial(i), instance.get_primorial(i)))
    
        
    print("-- Cullen Numbers: ")  
    for i in range(21):
        print("{0}  {1:,}".format(i, instance.get_cullen(i)))
        
        
    print("---Co primes")
    print(instance.is_co_prime(35, 18))
    instance.set_the_number(35)
    print(instance.is_co_prime(18))


    print('--get_compositorial')    
    for n in range(0,21):
        print("{0}  {1:}".format(n,instance.calculateCompositorial(n)))
        
    
    curzon_list = []
    print("---Curzon ")
    counter = 0    
    for x in range(1, 501):
        if instance.is_curzon(x):
            print(x, end=', ')
            counter += 1
            if counter % 20 == 0:
                print()
    print()
                
    print("---Euler's totient function for 75")
    i = 20
    print("get_totiatives(i): " , instance.get_totatives(i))
    
    print('---Phi')
    for i in range(1, 11):
        print("phi({0}) = {1}".format(i, instance.eulersPhi(i)))
    
    print("---DePolignac")    
    for i in range(1,1000):
        if instance.is_de_polignac(i):
            print(i, end = " ")
    print()

    print("---Droll")
    print("48384", instance.is_droll(43834))
    print("72", instance.is_droll(72))


    print("--Happy Numbers!!")    
    for i in range(1,1100):
        if instance.is_happy(i):
            print(f'{i}', end=", ")
    print()

    abc = 343421214
    print(instance.number_to_list(343421214))


    print("Queues")
    print(instance.the_queue())

    '''
    print("--Anti-perfect numbers")

    theNumbers = (6, 244, 285, 133857)
    for i in theNumbers:
        print(instance.is_antiperfect(i))
    '''

    
    

   

    
        
if __name__ == '__main__':
    main()
