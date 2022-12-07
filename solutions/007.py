#!/usr/bin/env python3

"""
Project Euler Problem 7
I am Eleven
"""

import math
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
    num, count = 1, 1
    while count < 10001:
        num +=2 # optimization
        if isPrime(num):
            count +=1
    return num
           
if __name__ == '__main__':
    print(solve())
    print("--- %.2f seconds ---" % (time.time() - start_time))
