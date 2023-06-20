import psutil
import sympy
import time
f = open('PBSG.txt', 'w')

MIN = 2 ** 127
MAX = 2 ** 128 - 1
COUNT = 1500000

def create_prime_number():
    prime_number = sympy.randprime(MIN, MAX)
    result = prime_number * 4 + 3
    return result


def main():
    startTime = time.time()
    p = create_prime_number()
    q = create_prime_number()
    M = p * q
    print('----------------------------------------------------Числа блюма--------------------------------------------')
    print('p = ', p)
    print('q = ', q)
    print('-----------------------------------------------------------------------------------------------------------')
    seed = psutil.cpu_stats()[0]

    for i in range(COUNT):
        seed = pow(seed, 2) % M
        bit = str(seed % 2)
        f.write(bit)
    f.close()
    print(f"Completed in {time.time() - startTime} seconds.")

if __name__ == '__main__':
    main()