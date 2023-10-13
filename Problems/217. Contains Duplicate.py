#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def containsDuplicate(self, nums):
        return (len(nums) != len(set(nums)))
    
def main():
    nums = [0,1,2,3,1]
    sol = Solution()
    print(sol.containsDuplicate(nums))

if __name__ == '__main__':
    main()