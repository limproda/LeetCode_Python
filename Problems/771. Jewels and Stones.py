#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def numJewelsInStones(self, jewels, stones):
        res = 0
        for jewel in jewels:
            if jewel in stones:
                res += stones.count(jewel)
        return res
    
def main():
    jewels = "aA"
    stones = "aAAbbbb"
    sol = Solution()
    print(sol.numJewelsInStones(jewels, stones))

if __name__ == '__main__':
    main()