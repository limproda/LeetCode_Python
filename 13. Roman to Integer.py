#!/usr/bin/env python
# -*- coding: utf-8 -*-
romanValues = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def receiveRNumber():
    no_valid = True
    while no_valid:
        no_valid = False
        s = input("Escriba su Número Romano: ")
        try:
            for index in range(len(s)-1):
                if not romanValues.get(s[index]):
                    print("Número romano incorrecto.")
                    no_valid = True
                    break
                if romanValues[s[index]] >= romanValues[s[index+1]]:
                    continue
                if s[index] == "I" and s[index+1] == "V" or s[index] == "I" and s[index+1] == "X":
                    continue
                elif  s[index] == "X" and s[index+1] == "L" or s[index] == "X" and s[index+1] == "C":
                    continue
                elif s[index] == "C" and s[index+1] == "D" or s[index] == "C" and s[index+1] == "M":
                    continue
                else:
                    print("Número romano incorrecto.")
                    no_valid = True
                    break
        except:
            print("Número romano incorrecto.")
            no_valid = True
        if not no_valid:
            break
    return s
def sumadorRomano(total, s):
    for index in range(len(s)):
        if index > 0 and romanValues[s[index]] > romanValues[s[index - 1]]:
            total += (romanValues[s[index]] - 2 * romanValues[s[index - 1]])
        else:
            total += romanValues[s[index]]
    return total

def main():
    total = 0
    s = receiveRNumber()
    print("El valor es: ", sumadorRomano(total, s))

if __name__ == '__main__':
    main()