import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import primes
import NumberTheory




def main():    
    print(f"{primes.is_prime(7)=}")
    print(f"{primes.is_prime(6)=}")
    print(f"{primes.get_prime_factors(200)=}")
    print(f"{primes.get_distinct_prime_factors(200)=}")
    print(f"{primes.is_semi_prime(65)=}")
    print(f"{primes.is_semi_prime(200)=}")
    print(f"{primes.get_prime_sieve(20)=}")
    print(f"{primes.get_digit_count(20000)=}")
    print(f"{primes.is_brilliant(33823)=}")
    print(f"{primes.is_droll(48384)=}")
    print(f"{primes.is_droll(71)=}")
    print(f"{primes.get_prime_lucky_numbers(7)=}")
    print(type(primes.get_prime_lucky_numbers(7)[0]))
    print(repr(primes.get_prime_lucky_numbers(7)))
    print(f"{NumberTheory.get_lucky_number_list(7)=}")
    print(f"{primes.is_chen_prime(251)=}")

    print(f"{primes.is_inter_prime(9)=}")
    print(f"{primes.get_lonely_numbers(20000)=}")
    print(f"{primes.get_primes_up_to(23)=}")    
    print(f"{primes.get_distance_to_closest_prime(23)=}")

    print(f"{primes.get_first_n_primes(23)=}")    
    print(f"{primes.get_fortunate_number(3)=}")

    
    print(f"{primes.is_n_smooth(60, 5)=}")  #S/b true    
    print(f"{primes.is_n_smooth(98, 5)=}")  #S/b false

    print(f"{primes.is_pierpont_prime(109)=}")  #S/b true
    print(f"{primes.is_pierpont_prime(31)=}")  #S/b false


    
    
    print(f"Jeff is a wizard!! ")
        
    



if __name__ == '__main__':
    main()

    