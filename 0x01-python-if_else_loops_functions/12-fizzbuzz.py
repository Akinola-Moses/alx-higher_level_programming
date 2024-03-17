#!/usr/bin/python3
def fizzbuzz():
    num = 0
    for num in range(100):
        if ((num % 3) == 0):
            print("Fizz", end=' ')
        elif ((num % 5) == 0):
            print("Buzz", end=' ')
        elif ((( num % 3) == 0) and (num % 5) == 0):
            print("FizzBuzz", end=' ')
        else:
            print("{}".format(num), end=' ')
