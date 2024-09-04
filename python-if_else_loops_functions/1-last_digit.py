#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
salam = abs(number) % 10

if salam > 5:
    print(f'Last digit of {number} is {salam} and is greater than 5')
elif salam == 0:
    print(f'Last digit of {number} is {salam} and is 0')
else:
    print(f'Last digit of {number} is {salam} and is less than 6 and not 0')
