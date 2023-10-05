#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def majorityElement(self, nums):
        length = len(nums)
        res = set()
        for number in nums:
            if nums.count(number) > length/3:
                res.add(number)
                
        return list(res)

def main():
    nums = [3,2,3]
    sol = Solution()
    print(sol.majorityElement(nums))

if __name__ == '__main__':
    main()