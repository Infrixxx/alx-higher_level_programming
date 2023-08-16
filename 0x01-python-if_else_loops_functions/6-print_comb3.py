#!/usr/bin/python3
for a in range(9):
    for b in range(a + 1, 9):
            print("{:d}{:d}".format(a, b), end=', ')
print('89')
