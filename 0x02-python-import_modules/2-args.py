#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv[1:]
    args_count = len(args)

    if args_count == 0:
        print("0 arguments.")

    elif args_count == 1:
        print("{} argument:".format(args_count))
        for idx in range(args_count):
            print("{}: {}".format(idx + 1, args[idx]))
    else:
        print("{} arguments:".format(args_count))
        for idx in range(args_count):
            print("{}: {}".format(idx + 1, args[idx]))
