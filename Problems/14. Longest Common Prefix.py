#!/usr/bin/env python
# -*- coding: utf-8 -*-
def tryIt(strs, letter, numeroPalabra):
    try:
        if numeroPalabra >= len(strs):
            return True
        elif strs[0][letter] == strs[numeroPalabra][letter]:
            return tryIt(strs, letter, numeroPalabra+1)
        else:
            return False
    except:
        return False

def main():
    strs = ["flower","flow","flight"]
    coincidences = ""
    for letter in range(len(strs[0])):
        if tryIt(strs, letter, 1):
            coincidences += strs[0][letter]
    if not len(coincidences):
        print("There is no common prefix among the input strings.")
    else:
        print(coincidences)
            
if __name__ == '__main__':
    main()