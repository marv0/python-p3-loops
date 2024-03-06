#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while  num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for int in int_list:
        square = int * int
        squared_list.append(square)
    return squared_list

def fizzbuzz():
    for i in range(1,101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"{i}")



