#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for number in nums:
            if number in seen:
                return number
            seen.add(number)

def main():
    sol = Solution()
    nums = [1,3,4,2,2]
    print(sol.findDuplicate(nums))
if __name__ == '__main__':
    main()