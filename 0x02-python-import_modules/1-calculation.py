#!/usr/bin/python3
if __name__ == "__main__":
    """Importation of the three functions."""

    from calculator_1 import div, mul, add, sub
    a = 10
    b = 5

    print("{} = {}".format(add({a} + {b}), add(a, b)))
    print("{} = {}".format(sub({a} - {b}), sub(a, b)))
    print("{} = {}".format(mul({a} * {b}), mul(a, b)))
    print("{} = {}".format(div({a} / {b}), div(a, b)))
