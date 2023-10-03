#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def numIdenticalPairs(self, nums):
        goods = 0
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    goods += 1
        return goods

def main():
    nums = [1,2,3,1,1,3]
    sol = Solution()
    print(sol.numIdenticalPairs(nums))

if __name__ == '__main__':
    main()