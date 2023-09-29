#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def isMonotonic(self, nums):
        increasing = decreasing = True

        for i in range(1, lens(n)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False
            
            if not increasing and not decreasing:
                return False
        return True
       
def main():
    nums = [1,3,2]
    sol = Solution()
    print(sol.isMonotonic(nums))

if __name__ == '__main__':
    main()