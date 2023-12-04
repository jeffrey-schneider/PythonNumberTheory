from Primes import Primes

def main():
    instance = Primes(8)
    print(instance.get_the_number())
    instance.set_the_number(3600)
    print(instance.get_the_number())

    print("Get Prime Factors")
    print(instance.get_prime_factors())

    print('Semi Primes ')
    i = 2
    line_counter = 0
    while i < 100:
        if instance.is_semi_prime(i):
            print(f'{i}', end = ' ')
            line_counter += 1
            if line_counter % 10 == 0:
                print()
        i += 1
    print()

    print('Is Brilliant')
    for i in range(4, 400):
        if instance.is_brilliant(i) :
            print(f'{i}', end=" ")
    print()

    print("Is Emirpimeses")    
    for i in range( 10, 101):
        if instance.is_emirpimeses(i):
            print(f'{i}')
    print()

    print("Is Chen Prime")
    for i in range(1, 251):
        if instance.is_chen_prime(i):
            print(f'{i}', end=' ')
    print()


    print("Neighbor Prime")
    print(instance.get_neighbor_prime(199, False, False))
    print(instance.get_previous_prime(199))
    print(instance.get_next_prime(199))
    print(instance.get_previous_prime_inclusive(199))
    print(instance.get_next_prime_inclusive(199))

    print("get_distinct_prime_factors")
    instance.set_the_number(60)
    print(instance.get_distinct_prime_factors(60))








if __name__ == '__main__':
    main()
