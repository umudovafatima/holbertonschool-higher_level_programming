#!/usr/bin/python3   
for letters in range(ord('a'), ord('z')+1):
    if chr(letters) == 'q' or chr(letters) == 'e':
        pass
    else:
        print("{}".format(chr(letters)), end = "")
