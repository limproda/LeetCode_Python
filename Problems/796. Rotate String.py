#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def rotateString(self, s, goal):
        """
            MORE ELEGANT SOLUTION:
            return len(s) == len(goal) and s in goal + goal
        """
        if len(s) != len(goal):
            return False
        for lenght in range(len(s)):
            if s == goal:
                return True
            else:
                s= s[-1] + s
                s = s[:-1]
        return False


def main():
    s = "abcde"
    goal = "cdeab"
    sol = Solution()
    print(sol.rotateString(s,goal))

if __name__ == '__main__':
    main()