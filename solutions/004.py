#!/usr/bin/env python3

"""
Project Euler Problem 4
Gimme gimme more
"""

import math
import time

start_time = time.time()

def solve():
    res = 0
    for i in range(100, 999):
        for j in range(100, 999):
            x = i*j
            if x > res:
                s = str(x)
                if s == s[::-1]:
                    res = x            
    return res
           
if __name__ == '__main__':
    print(solve())
    print("--- %.2f seconds ---" % (time.time() - start_time))
