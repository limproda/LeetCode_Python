#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(str(words[-1]))
    
def main():
    sol = Solution()
    s = "   fly me   to   the moon  "

    print(sol.lengthOfLastWord(s))
    
if __name__ == '__main__':
    main()