import psutil
import sympy
import time
f = open('C:/Users/Grenk/OneDrive/Рабочий стол/test.txt', 'w')


def prime_number():
    prime_number = sympy.randprime(2**127, 2**128-1)
    result = prime_number * 4 + 3
    return result


startTime = time.time()
p = prime_number()
q = prime_number()
M = p * q
print('----------------------------------------------------Числа блюма--------------------------------------------')
print('p = ', p)
print('q = ', q)
print('-----------------------------------------------------------------------------------------------------------')
seed = psutil.cpu_stats()[0]


for i in range(0, 1500000):
    seed = pow(seed, 2) % M
    bit = str(seed % 2)
    f.write(bit)
f.close()
print(f"Completed in {time.time() - startTime} seconds.")

