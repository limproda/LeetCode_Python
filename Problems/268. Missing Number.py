#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
def main():
    sol = Solution()
    nums = [3,0,1]
    print(sol.missingNumber(nums))
if __name__ == '__main__':
    main()