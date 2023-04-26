#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        if b == 0 or a == 0:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(a / b))
