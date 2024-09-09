#!/usr/bin/python3
from calculator_1 import add,sub,mul,div

a = 10
b = 5
x = add(a, b)
y = sub(a,b)
k = mul(a,b)
j = div(a,b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, x))
    print("{} - {} = {}".format(a, b, y))
    print("{} * {} = {}".format(a, b, k))
    print("{} / {} = {}".format(a, b, j))
