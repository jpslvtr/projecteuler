#!/usr/bin/env python3

# Project Euler Problem 3
# Tomorrow is not guaranteed

import math

def solve():
    n = 600851475143
    i = 2
    factors = []
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return max(factors)

if __name__ == '__main__':
    print(solve())
