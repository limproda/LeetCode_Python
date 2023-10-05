#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def countPairs(self, nums, k):
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res

def main():
    nums= [3,1,2,2,2,1,3]
    k = 2
    sol = Solution()
    print(sol.countPairs(nums, k))

if __name__ == '__main__':
    main()