#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    nargs = len(argv)
    if nargs < 2:
        print("{} arguments.".format(nargs - 1))
    else:
        if nargs == 2:
            print("{} argument:".format(nargs - 1))
        else:
            print("{} arguments:".format(nargs - 1))
            for n in range(1, nargs):
                print("{}: {}".format(n, argv[n]))
