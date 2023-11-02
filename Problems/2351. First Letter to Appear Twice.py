#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def repeatedCharacter(self, s):
        res = []
        for letter in s:
            if (letter in res) == True:
                return letter
            else:
                res.append(letter)

def main():
    s = "abccbaacz"
    sol = Solution()
    print(sol.repeatedCharacter(s))

if __name__ == '__main__':
    main()