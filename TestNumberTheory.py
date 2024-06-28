"""
Created on Dec 6, 2022

@author: JCSchneider
"""
# from NumberTheory import *


# from test.dtracedata import instance
# from pickle import INST
from NumberTheory import NumberTheory


def main():
    print("In main")
    instance = NumberTheory(9)

    print("Is ", instance.get_the_number(), " even?")
    print(NumberTheory.is_even(instance,None))
    x = 12
    print("Is ", x, " even? ", NumberTheory.is_even(None,x))

    print(instance.get_the_number())

    print("Get Square ")
    print(f'{NumberTheory.get_square(None,8) = }')
    instance.set_the_number(9)
    print(f'{NumberTheory.get_square(instance, None) = }')

    print("Get Cube ")
    print(f'{NumberTheory.get_cube(None, 8) = }')
    instance.set_the_number(9)
    print(NumberTheory.get_cube(instance, None))


    print("Primes: ")
    print(f'{NumberTheory.is_prime(None, 32) = }')
    print(f'{NumberTheory.is_prime(instance, None) = }')

    print("Collatz 27")
    for i in NumberTheory.get_collatz(None, 27):
        print(i, end=" ")
    print()
    print("Collatz 43")
    instance.set_the_number(43)
    for i in NumberTheory.get_collatz(instance, None):
        print(i, end=" ")
    print()

    print("Jugglers 37")
    for i in NumberTheory.get_jugglers(None,37):
        print(i, end=" ")
    print()

    print("Jugglers 45")
    instance.set_the_number(45)
    for i in NumberTheory.get_jugglers(instance, None):
        print(i, end=" ")
    print()

    print("Factors of 60")
    for i in NumberTheory.get_factors(None, 60):
        print(i, end=' ')
    print()

    print("Factors of 3600")
    instance.set_the_number(3600)
    for i in NumberTheory.get_factors(instance, None):
        print(i, end=' ')
    print()

    # --------
    print("Reversed 43")
    instance.set_the_number(43)
    print(NumberTheory.get_reverse_number(instance,None))

    print("Reciprocal 43")
    print(NumberTheory.get_reciprocal_number(None, 43))

    print("To hex 76576500")
    instance.set_the_number(76576500)
    print(NumberTheory.get_hex(instance, None))

    print("Is abundant 12")
    instance.set_the_number(12)
    print(NumberTheory.is_abundant(instance, None))
    x = 41
    print(x, " ", NumberTheory.is_abundant(None, x))

    print(instance.get_the_number(), " ", NumberTheory.get_abundance(instance,None))
    print(x, " ", NumberTheory.get_aliquot_sum(None, x), " ", NumberTheory.get_abundance(None, x))

    print("Get factors sum: ", NumberTheory.get_factors_sum(None, x))
    x = 9
    instance.set_the_number(x)
    print("Sigma: ", NumberTheory.get_sigma(instance,None))
    print("Sigma: ", NumberTheory.get_sigma(None, x * 10))

    instance.set_the_number(20)
    print("Catalan ", NumberTheory.get_catalan(instance, None))
    print("Catalan ", NumberTheory.get_catalan(None,15))

    print("get_fibonacci_list", NumberTheory.get_fibonacci_list(instance, None))
    print("get_fibonacci_list", NumberTheory.get_fibonacci_list(None, 15))

    instance.set_the_number(15)
    print("get_motzin", NumberTheory.get_motzkin(instance, None))
    print("get_motzin", NumberTheory.get_motzkin(None, 20))

    instance.set_the_number(10)
    print("getPellList: ", NumberTheory.get_pell_list(instance,None))
    print("getPellList: ", NumberTheory.get_pell_list(None, 12))
    print("getPell: ", NumberTheory.get_pell(instance, None))
    print("getPell: ", NumberTheory.get_pell(None,12))

    instance.set_the_number(15)
    print("getJacobsthalList ", NumberTheory.get_jacobsthal_list(instance,None))
    print("getJacobsthalList ", NumberTheory.get_jacobsthal_list(None,12))
    instance.set_the_number(12)
    print("getJacobsthal ", NumberTheory.get_jacobsthal(instance, None))
    print("getJacobsthal ", NumberTheory.get_jacobsthal(None,15))

    instance.set_the_number(21)
    print("alternating Factorial: ", NumberTheory.get_alternating_factorial(instance, None))

    instance.set_the_number(16)
    print("is Deficient: ", NumberTheory.is_deficient(instance,None))
    print("is Deficient: ", NumberTheory.is_deficient(None,60))

    print("gcd: ", NumberTheory.gcd(12, 8))
    print("lcm:  ", NumberTheory.lcm(None, 15, 75))

    print("https://stackoverflow.com/questions/51826611/speed-up-a-search-for-carmichael-numbers")
    instance.set_the_number(6601)
    # print(instance.is_carmichael())
    # print(instance.is_carmichael(1105))

    print("D-Numbers")
    for n in range(1, 500):
        if NumberTheory.isDNum(None,n):
            print(n, end=' ')
    print()

    """
        TODO 
    print("Cake Number")
    for n in range(1, 25):
        print(NumberTheory.get_cake_number(None,n))
    """
    # print("Cake Number")
    # print(instance.get_the_number(), " ", NumberTheory.get_cake_number())

    print("Lazy Caterer")
    for n in range(1, 25):
        print(NumberTheory.get_lazy_caterer(None, n))
    #print(instance.get_the_number(), " ", NumberTheory.get_lazy_caterer())

    print("Primitive Abundant")
#    print(NumberTheory.is_primitive_abundant(None,24))

    print("https://forum.generic-mapping-tools.org/t/how-to-calculate-coordinates-from-bearing-distance/1217")
    lat2, lon2 = instance.get_end_point(lat1=50, lon1=8, bearing=310, d=23)
    print(lat2, " ", lon2)

    bearing = instance.get_bearing(lat1=50, lon1=8, lat2=50.24533, lon2=7.54112)
    print(bearing)

    bearing = instance.get_bearing(lat1=30.07134, lon1=-97.23076,
                                   lat2=30.0709, lon2=-97.22907)
    print(bearing)

    print()
    instance.set_the_number(30)
 #   print("is 3 abundant? ", NumberTheory.is_abundant(None,3))
 #   print("is_primitive_abundant", instance.is_primitive_abundant(instance, None))
#    print("is_primitive_abundant", instance.is_primitive_abundant(None, 3600))

    print("Superabundant")
    print("120 is, 5 is not")
  #  print(instance.is_super_abundant(120))
  #  print(instance.is_super_abundant(5))

    print("Keith Number")
    for i in range(10, 5000):
        if (NumberTheory.is_keith_number(None,  i)):
            print(i)

    print("Betrothed Number")
    for i in range(48, 1000):
        betrothed = NumberTheory.get_betrothed_number(None,i)
        if betrothed > 0:
            print("Number: {0:3d}  Betrothed: {1:5.0f}".format(i, NumberTheory.get_betrothed_number(None,i)))

    print("Cake Numbers")
    n = 0
    while n < 5:
        print("Cuts: {0:3d}  Pieces: {1:5.0f}".format(n, NumberTheory.get_cake_number(None, n)))
        n += 1

    print("Lazy Caterer's Numbers:");
    n = 0;
    while n < 5:
        print("Cuts: {0:3d}  Pieces: {1:5.0f}".format(n, NumberTheory.get_lazy_caterer(None, n)))
        n += 1

    print("Bell's Numbers:")
    n = 0;
    while n <= 50:
        print("Number: {0:3d}  Bell: {1:5.0f}".format(n, NumberTheory.get_bell_number(None, n)))
        n += 1

    print("Centered polygonal numbers")
    for j in range(3, 5):
        print("Sides {0:4d}".format(j))
        for i in range(0, 5):
            print("{0:4d}  {1:d}".format(i, NumberTheory.get_centered_polygonal_number(None, j, i)))

    print("Polygonal Numbers")
    for outer in range(2, 25):
        print(" {0:4d} ".format(outer), end=' ')
        for inner in range(1, 11):
            print(" {0:.0f} ".format(instance.get_polygonal_number(None, outer, inner)), end=' ')
        print()

    print("----Number  -> Factorials -> Primorials")
    print("is 11 prime? ", NumberTheory.is_prime(None,11))
    for i in range(26):
        print("{0}  {1:,} / {2:,}".format(i, instance.get_factorial(None, i), instance.get_primorial(None, i)))

    print("-- Cullen Numbers: ")
    for i in range(21):
        print("{0}  {1:,}".format(i, instance.get_cullen(None, i)))

    print("---Co primes")
    print(NumberTheory.is_co_prime(  instance, 35, 18))
    instance.set_the_number(35)
    print(NumberTheory.is_co_prime(instance, 18))

    print('--get_compositorial')
    for n in range(0, 21):
        print("{0}  {1:}".format(n, NumberTheory.calculateCompositorial(None, n)))

    curzon_list = []
    print("---Curzon ")
    counter = 0
    for x in range(1, 501):
        if NumberTheory.is_curzon(None, x):
            print(x, end=', ')
            counter += 1
            if counter % 20 == 0:
                print()
    print()

    print("---Euler's totient function for 75")
    i = 20
    # print("get_totiatives(i): ", instance.get_totatives(i))
    print(f"{NumberTheory.get_totatives(None, i) = }")

    print('---Phi')
    for i in range(1, 11):
        print("phi({0}) = {1}".format(i, NumberTheory.eulersPhi(None, i)))

    print("---DePolignac")
    for i in range(1, 1000):
        if NumberTheory.is_de_polignac(None, i):
            print(i, end=" ")
    print()

    instance.set_the_number(150)
    print("--Happy Numbers!!")
    for i in range(1, 1100):
        if NumberTheory.is_happy(None, i):
            print(f'{i}', end=", ")
    print()

    abc = 343421214
    print(NumberTheory.number_to_list(343421214))

    print("Queues")
    print(NumberTheory.the_queue())

    '''
       print("--Anti-perfect numbers")

       theNumbers = (6, 244, 285, 133857)
       for i in theNumbers:
           print(instance.is_antiperfect(i))
    '''

#    print(f'Lucky number list')
#    print(f'{NumberTheory.get_lucky_number_list(10)}')
#    instance.set_the_number(15)
#    print(f'{NumberTheory.get_lucky_number_list(None, instance)}')


if __name__ == '__main__':
    main()
