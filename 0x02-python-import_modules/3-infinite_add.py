#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    add = 0
    for args in sys.argv[1:]:
        add += int(args)

    print(add)
