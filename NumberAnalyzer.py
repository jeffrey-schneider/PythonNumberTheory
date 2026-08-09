import primes


class NumberAnalyzer:

    def __init__(self, value: int):
        self.value = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int):
        self._value = new_value

    @property
    def is_prime(self) -> bool:
        return primes.is_prime(self.value)
    
    
    @property
    def get_prime_factors(self) -> list[int]:
        return primes.get_prime_factors(self.value)
    
    @property
    def generate_primes(self) -> list[int]:
        return primes.generate_primes(self.value)
    
    @property
    def is_semi_prime(self) -> bool:
        return primes.is_semi_prime(self.value)
    
    @property
    def get_prime_sieve(self) -> list[bool]:
        return primes.get_prime_sieve(self.value) 
    
    @property
    def get_digit_count(self)-> int:
        return primes.get_digit_count(self.value)
    
    @property
    def is_brilliant(self)->bool:
        return primes.is_brilliant(self.value)
    
    @property
    def is_emirpimes(self) -> bool:
        return primes.is_emirpimes(self.value)
    
    @property
    def is_chen_prime(self) -> bool:   
        return primes.is_chen_prime(self.value)
    
    @property
    def is_emirp(self) -> bool:
        return primes.is_emirp(self.value)
    

    @property
    def is_good_prime(self) -> bool:
        return primes.is_good_prime(self.value)
    
    @property
    def get_next_prime(self) -> int:
        return primes.get_next_prime(self.value)
    
    @property
    def get_previous_prime(self)->int:
        return primes.get_previous_prime(self.value)
    
    @property
    def get_next_prime_inclusive(self) -> int:
        return primes.get_next_prime_inclusive(self.value)
    
    @property
    def get_previous_prime_inclusive(self) -> int:
        return primes.get_previous_prime_inclusive(self.value)
    
    @property
    def is_a_pointer_prime(self) -> bool:
        return primes.is_a_pointer_prime(self.value)
    
    @property
    def is_m_pointer_prime(self) -> bool:
        return primes.is_m_pointer_prime(self.value)
    
    @property
    def is_inter_prime(self) -> bool:
        return primes.is_inter_prime(self.value)

    @property
    def get_distinct_prime_factors(self) -> list[int]:
        return primes.get_distinct_prime_factors(self.value)
    
    @property
    def is_droll(self) -> bool:
        return primes.is_droll(self.value)
    
    @property
    def get_prime_lucky_numbers(self) -> list[int]:
        return primes.get_prime_lucky_numbers(self.value)
    
    #Not a property
    def is_co_prime(self, b) -> bool:
        return primes.is_co_prime(self.value, b)
    
    @property
    def get_lonely_numbers(self)-> list[int]:
        return primes.get_lonely_numbers(self.value)
    
    @property
    def get_distance_to_closest_prime(self) -> int:
        return primes.get_distance_to_closest_prime(self.value)
    
    @property
    def get_fortunate_number(self) -> int:
        return primes.get_fortunate_number(self.value)
    
    
    #Not a property
    def is_n_smooth(self, n: int) -> bool:
        return primes.is_n_smooth(self.value, n)
    

    @property
    def is_pierpont_prime(self) -> bool:
        return primes.is_pierpont_prime(self.value)

    @property
    def is_sphenic(self) -> bool:
        return primes.is_sphenic(self.value)
    
    @property
    def get_primes_up_to(self) -> list[int]:
        return primes.get_primes_up_to(self.value)
    
    @property
    def get_first_n_primes(self)-> list[int]:
        return primes.get_first_n_primes(self.value)






    

