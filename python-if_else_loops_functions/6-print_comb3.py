#!/usr/bin/python3
l = [0,1,2,3,4,5,6,7,8,9]
for i in range l:
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')