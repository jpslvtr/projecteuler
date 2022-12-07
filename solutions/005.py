#!/usr/bin/env python3

"""
Project Euler Problem 5
I am alive
"""

import math

def solve():
    gcd = 1
    for x in range(1,21):
        gcd_curr = math.gcd(x,gcd)
        gcd *= x // gcd_curr
    return gcd

if __name__ == '__main__':
    print(solve())
