#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    prints = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            prints += 1
        except IndexError:
            break
    print()
    return (prints)
