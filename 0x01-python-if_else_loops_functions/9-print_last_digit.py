#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
    if number < 0:
        num = number * -1
        last = num % 10

    print("{:d}".format(last), end="")
    return last
