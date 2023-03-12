#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
last = number % 10
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
=======
if number > 0:
    last = number % 10
    message = "Last digit of {} is {}".format(number, last)
    if last > 5:
        print("{} and is greater than 5".format(message))
    elif last == 0:
        print("{} and is 0".format(message))
    elif (last < 6) and (last != 0):
        print("{} and is less than 6 and not 0".format(message))
if number < 0:
    num = number * -1
    last = (num % 10) * -1
    message = "Last digit of {} is {}".format(number, last)
    if last == 0:
        print("{} and is 0".format(message))
    elif (last < 6) and (last != 0):
        print("{} and is less than 6 and not 0".format(message))
if number == 0:
    message = "Last digit of {} is {}".format(number, number)
    print("{} and is 0".format(message))
>>>>>>> 7372dd703cbc9fcae0b941232ef1f91cfdb682cd
