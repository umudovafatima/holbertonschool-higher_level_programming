#!/usr/bin/python3
for i in range(0, 100):
    if i >= 0 and i < 10:
        print(str(i).zfill(2), end=',')
    else:
        print(i, end=',')
