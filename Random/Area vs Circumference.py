import random
from math import sqrt

def generate_circumference():
    radius=random.randint(1, 25)
    circumference=2*(3.14*radius)
    return circumference

def generate_area():
    area=random.randint(500,1000)
    perimeter=2*(sqrt(area))
    return perimeter

for i in range(10):
    circle=int(generate_circumference())
    square=int(generate_area())
    if circle>=square:
        print(f"The circle {circle} is larger than the square {square} resulting in a {True} statement")
    else:
        print(f"The circle {circle} is smaller than the square {square} resulting in a {False} statement")