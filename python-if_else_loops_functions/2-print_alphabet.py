#!/usr/bin/python3   
for letters in range(ord('a'), ord('z')+1):
    if letters >= ord('a') and letters <= ord('z'):
        print(f'{chr(letters)}', end="")
