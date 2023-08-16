#!/usr/bin/python3
n = 0;
while n <= 99:
    if n < 99:
        a = n // 10
        b = n%10
        print(f"{a:d}{b:d}",end=', ')
        n += 1
    else:
        print(f"{n:d}")
        break
