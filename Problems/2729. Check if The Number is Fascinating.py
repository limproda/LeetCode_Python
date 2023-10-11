#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def isFascinating(self, n):
        res = str(n) + str(n*2) + str(n*3)
        if "0" in res:
            return False
        for index,letter in enumerate(res):
            if letter in res[index+1:]:
                return False
            else:
                continue
        return True
    
def main():
    n = 192
    sol = Solution()
    print(sol.isFascinating(n))

if __name__ == '__main__':
    main()