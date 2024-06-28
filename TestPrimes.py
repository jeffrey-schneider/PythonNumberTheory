from Primes import Primes


def main():
    instance = Primes(8)
    print(instance.get_the_number())
    instance.set_the_number(3600)
    print(instance.get_the_number())

    print("Get Prime Factors")
    print(Primes.get_prime_factors(instance))

    print('Semi Primes ')
    i = 2
    line_counter = 0
    while i < 100:
        if Primes.is_semi_prime(None, i):
            print(f'{i}', end=' ')
            line_counter += 1
            if line_counter % 10 == 0:
                print()
        i += 1
    print()

    print('Is Brilliant')
    for i in range(4, 400):
        if instance.is_brilliant(None, i):
            print(f'{i}', end=" ")
    print()

    print("Is Emirpimeses")
    for i in range(10, 101):
        if Primes.is_emirpimeses(None, i):
            print(f'{i}')
    print()

    print("Is Chen Prime")
    for i in range(1, 251):
        if Primes.is_chen_prime(None, i):
            print(f'{i}', end=' ')
    print()

    print("Neighbor Prime")
    print(Primes.get_neighbor_prime(199, False, False))
    print(Primes.get_previous_prime(None, 199))
    print(Primes.get_next_prime(None,199))
    print(Primes.get_previous_prime_inclusive(None, 199))
    print(Primes.get_next_prime_inclusive(None, 199))

    print("get_distinct_prime_factors")
    instance.set_the_number(60)
    print(Primes.get_distinct_prime_factors(instance))
    print(f'{Primes.get_distinct_prime_factors(None,360) = }')

    print("---Droll")
    print("48384", Primes.is_droll(None, 43834))
    print("72", Primes.is_droll(None, 72))


if __name__ == '__main__':
    main()
