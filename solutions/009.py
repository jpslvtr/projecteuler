#!/usr/bin/env python3

"""
Project Euler Problem 9
Coding is sublime
"""

import math
import itertools
import time

start_time = time.time()

def solve():
    res = []
    for a in range(1,1000):
        for b in range(a+1, 1000):
            c = math.sqrt(a*a + b*b)
            if c.is_integer() and c*c == a*a + b*b and a+b+c==1000:
                res.extend([a, b, c])
    return res

if __name__ == '__main__':
    print(solve())
    print("--- %.2f seconds ---" % (time.time() - start_time))
