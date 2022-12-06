#!/usr/bin/env python3

# Project Euler Problem 4
# Gimme gimme more

import math
import time
start_time = time.time()

def solve():
    n = 999*999
    palindromes = []
    res = []
    for n in range(n,-1,-1):
        strn = str(n)
        if strn == strn[::-1]:
            palindromes.append(n)
    for i in reversed(range(100,999)):
        for j in reversed(range(100, 999)):
            if i*j in palindromes:
                res.append(i*j)
    return max(res)
           
if __name__ == '__main__':
    print(solve())
    print("--- %.2f seconds ---" % (time.time() - start_time))
