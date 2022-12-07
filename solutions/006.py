#!/usr/bin/env python3

"""
Project Euler Problem 6
Stones and sticks
"""

def solve():
    sum1 = 0
    sum2 = 0
    for x in range(101):
        sum1 += x*x
        sum2 += x
    return sum2*sum2 - sum1

if __name__ == '__main__':
    print(solve())
