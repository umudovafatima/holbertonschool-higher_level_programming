#!/usr/bin/python3
import calculator_1
a = 10
b = 5
x= calculator_1.add(a, b)
y = calculator_1.sub(a,b)
k =calculator_1.mul(a,b)
j = calculator_1.div(a,b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, x))
    print("{} - {} = {}".format(a, b, y))
    print("{} * {} = {}".format(a, b, k))
    print("{} / {} = {}".format(a, b, j))
