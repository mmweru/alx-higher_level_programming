#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    s = 0
    try:
        for i in my_list[0: x]:
            print(i, end="")
            s += 1

    except Exception:
        pass

    print()
    return s
