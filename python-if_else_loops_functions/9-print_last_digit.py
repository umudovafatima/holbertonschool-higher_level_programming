#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    salam = abs(number) % 10
    print(f'{salam}', end='')
    return salam
