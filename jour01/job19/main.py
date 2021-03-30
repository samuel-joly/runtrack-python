#!/usr/bin/env python3

def FizzBuzz():
    for i in range(100):
        if i%5==0 and i%3==0:
            print("FizzBuzz")
        elif i%3 == 0 :
            print("Buzz")
        elif i%5 == 0 :
            print("Fizz")

FizzBuzz()
