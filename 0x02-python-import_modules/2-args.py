#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if (len(argv) == 1):
        print("0 arguments.")
    else:
        print("{} {}".format(len(argv) - 1,
                             'arguments:' if (len(argv)) > 2
                             else 'argument:'))
        for i in range(1, len(argv)):
            print("{}: {} ".format(i, argv[i]))
