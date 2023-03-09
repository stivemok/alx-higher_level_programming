#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = 0
    for i in range(len(argv) -1):
        num += int(argv[i + 1])
    print("{}".format(num))
