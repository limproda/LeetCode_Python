#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
   def addSpaces(self, s, spaces):
        """My solution causes TLE (Time Limit Exceeded). Better this solution:
        res = ""
        lastIdx = 0
        for i in spaces:
            res += s[lastIdx:i]
            res += " "
            lastIdx = i
        res += s[lastIdx:]
        return(res)"""
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