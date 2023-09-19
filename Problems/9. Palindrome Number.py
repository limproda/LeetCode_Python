#!/usr/bin/env python
# -*- coding: utf-8 -*-
def comparer(value1 ,value2):
    return value1 == value2
def main():
    value = 121
    x = [int(a) for a in str(value)]
    x.reverse()
    cadena = int(''.join(map(str, x)))
    print(comparer(value, cadena))
if __name__ == '__main__':
    main()