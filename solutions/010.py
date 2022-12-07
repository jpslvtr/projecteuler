#!/usr/bin/env python3

"""
Project Euler Problem 10
Remember Ben Ten?
"""

import math
import itertools
import time

start_time = time.time()

def isPrime(n):
    factor = 2
    while (factor * factor <= n):
        if n % factor == 0:
            return False
        factor +=1
    return True

def solve():
    res = 0
    for i in range(2,2000000):
        if isPrime(i):
            res += i
    return res

if __name__ == '__main__':
    print(solve())
    print("--- %.2f seconds ---" % (time.time() - start_time))
