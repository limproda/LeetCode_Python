#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def isSubsequence(self, s, t):
        # First approach. The problem is that we are creating new lists everytime
        while len(s) and len(t):
            if s[0] == t[0]:
                s = s[1:]
                t = t[1:]
            else:
                t = t[1:]
        return not len(s)
        """
         Second approach. We use the same strings but is not necessary to update them:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)
        """
def main():
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s,t))
if __name__ == '__main__':
    main()