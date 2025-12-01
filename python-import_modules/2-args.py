#!/usr/bin/python3


def main():
    import sys
    if len(sys.argv) == 2:
        print("1 argument:")
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
