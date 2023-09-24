#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def numDifferentIntegers(self, word):
        numbers = set()
        digits = ""
        for letter in word:
            if letter.isalpha():
                if digits:
                    numbers.add(int(digits))
                    digits = ""
                continue
            else:
                digits = digits + letter
        if digits:
            numbers.add(int(digits))
        return len(numbers)
def main():
    word = "a123bc34d8ef34"
    sol = Solution()
    print(sol.numDifferentIntegers(word))

if __name__ == '__main__':
    main()