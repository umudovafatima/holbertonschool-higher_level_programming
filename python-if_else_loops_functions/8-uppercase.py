#!/usr/bin/python3
def uppercase(str):
    salam = ''
    for fatima in str:
        if 'a' <= fatima <= 'z':
            salam = salam + "{}".format(chr(ord(fatima) - 32))
        else:
            salam = salam + "{}".format(fatima)
    print("{}".format(salam))
