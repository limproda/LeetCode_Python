#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
   def addSpaces(self, s, spaces):
        new_s = ""
        for index, letter in enumerate(s):
            if index in spaces:
                new_s += " "
            new_s += letter
        return new_s
   
def main():
    s = "LeetcodeHelpsMeLearn"
    spaces = [8,13,15]
    sol = Solution()
    print(sol.addSpaces(s, spaces))

if __name__ == '__main__':
    main()