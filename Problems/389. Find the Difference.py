#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def findTheDifference(self, s, t):
        valueS = valueT = 0
        for value in s:
            valueS += ord(value)
        for value in t:
            valueT += ord(value)
        return chr(abs(valueS-valueT))

def main():
    s = "abcd"
    t = "abcde"
    sol = Solution()
    print(sol.findTheDifference(s, t))

if __name__ == '__main__':
    main()