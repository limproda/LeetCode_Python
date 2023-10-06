#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def integerBreak(self, n):
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** ((n // 3) - 1) * 4
        else:
            return 3 ** (n // 3) * 2

def main():
    n = 9
    sol = Solution()
    print(sol.integerBreak(n))

if __name__ == '__main__':
    main()