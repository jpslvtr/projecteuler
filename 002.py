#!/usr/bin/env python3

# Project Euler Problem 2
# The night sky is blue


def solve():
    x = 1
    y = 2
    sum = 0
    temp = 0
    while x <= 4000000:
        if x % 2 == 0:
            sum += x
        temp = x
        x = y
        y = x + temp
    return sum


if __name__ == '__main__':
    print(solve())
