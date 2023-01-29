#!/usr/bin/env python3

"""
Project Euler 1
"""

def solve():
    sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

if __name__ == '__main__':
    print(solve())
