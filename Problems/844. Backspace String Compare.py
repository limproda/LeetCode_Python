#!/usr/bin/env python
# -*- coding: utf-8 -*-
#NECESSARY TO REVISE#

class Solution:
    def backspaceCompare(self, s,t):
        news = ""
        newt = ""
        if "#" in s:
            for letter in s:
                if letter == "#":
                    news = news[:-1]
                else:
                    news += letter
        if "#" in t:
            for letter in t:
                if letter == "#":
                    newt = newt[:-1]
                else:
                    newt += letter
        return news == newt

def main():
    s = "ab#c"
    t = "ad#c"
    sol = Solution()
    print(sol.backspaceCompare(s,t))

if __name__ == '__main__':
    main()