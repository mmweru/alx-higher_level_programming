#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    s = 0
    for value in range(x):
        try:
            print("{:d}".format(my_list[value]), end="")
            s += 1

        except (ValueError, TypeError):
            continue

    print()
    return (s)
