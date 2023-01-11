import random
from math import sqrt

def stutter(word):
    print(f"{word[0:2]}... {word[0:2]}... {word}?")

def generate_circumference():
    radius=random.randint(1, 25)
    circumference=2*(3.14*radius)
    return circumference

def generate_area():
    area=random.randint(500,1000)
    perimeter=2*(sqrt(area))
    return perimeter

def binary(number):
    while True:
        try:
            number=int(number)
            break
        except ValueError:
            print("Invalid input -- try entering an integer")
    if 0<=number<1024:
        binary_number="00000000"
        if (number-128)>=0:
            number-=128
            binary_number[0]="1"
        if (number-64)>=0:
            number-=64
            binary_number[1]="1"
        if (number-32)>=0:
            number-=32
            binary_number[2]="1"
        if (number-16)>=0:
            number-=16
            binary_number[3]="1"
        if (number-8)>=0:
            number-=8
            binary_number[4]="1"
        if (number-4)>=0:
            number-=4
            binary_number[5]="1"
        if (number-2)>=0:
            number-=2
            binary_number[6]="1"
        if (number-1)>=0:
            number-=1
            binary_number[7]="1"
        print(binary_number)
        return binary_number

    else:
        print("Invalid input -- please enter a number between 0 and 1024")


stutter("encyclopedia")

converted_integer=input("Please enter a number between 0 and 1024: ")
new_bin=binary(converted_integer)
print(new_bin)

for i in range(10):
    circle=int(generate_circumference())
    square=int(generate_area())
    if circle>=square:
        print(f"The circle {circle} is larger than the square {square} resulting in a {True} statement")
    else:
        print(f"The circle {circle} is smaller than the square {square} resulting in a {False} statement")