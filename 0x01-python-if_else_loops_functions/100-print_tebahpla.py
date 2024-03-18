#!/usr/bin/python3
for alp in range(122, 96, -1):
    print("{:c}".format(alp - 32 if alp % 2 != 0 else alp), end='')
