#!/usr/bin/env python3

"""
Project Euler 8
"""

import math
import time

start_time = time.time()

def read_file(filename):
    with open(filename) as f:
        res = f.read().strip('\n')
    return res

def product(window):
    res = 1
    for c in window:
        res *= int(c)
    return res

def solve():
    n = 0
    inputFile = read_file("../inputs/008.txt")
    for i in range(len(inputFile)-12):
        window = inputFile[i: i+13]
        window = product(window)
        if window > n:
            n = window
    return n
 
if __name__ == '__main__':
    print(solve())
    print("--- %.2f seconds ---" % (time.time() - start_time))
