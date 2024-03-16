#!/usr/bin/python3
for num in range(0, 99):
    if (num % 10 == 0):
        num = num + 1 // 10
    print("{:02},".format(num), end=' ')
