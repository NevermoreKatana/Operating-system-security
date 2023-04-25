import base64

import psutil
import sympy
import time
import hashlib

def prime_number():
    prime_number = sympy.randprime(2**127, 2**128-1)
    result = prime_number * 4 + 3
    return result


massive = []
def salt():
    p = prime_number()
    q = prime_number()
    M = p * q
    seed = psutil.cpu_stats()[0]
    for i in range(0, 128):
        seed = pow(seed, 2) % M
        bit = bin(seed % 2)

        massive.append(bit[2:])
    frs = ''
    for index in range(len(massive)):
        frs += massive[index]
    bit = bytearray(frs.encode())
    return bit
salt()
