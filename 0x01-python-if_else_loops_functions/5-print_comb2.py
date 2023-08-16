#!/usr/bin/python3
n = 0
while n <= 99:
    if n < 99:
        a = n // 10
        b = n % 10
        print("{:d}{:d}".format(a, b), end=', ')
        n += 1
    else:
        print("{:d}".format(n))
        break
