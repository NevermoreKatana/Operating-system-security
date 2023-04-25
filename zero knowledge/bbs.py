import psutil
import sympy
import time


class bit_e():
    def prime_number():
        prime_number = sympy.randprime(2**1023, 2**1024-1)
        result = prime_number * 4 + 3
        return result

    def generate_e():
        p = bit_e.prime_number()
        q = bit_e.prime_number()
        M = p * q
        seed = psutil.cpu_stats()[0]
        for i in range(0, 1):
            seed = pow(seed, 2) % M
            bit = bin(seed % 2)
        return bit[2:]


