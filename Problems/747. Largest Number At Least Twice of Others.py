#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def dominantIndex(self, nums):
        major = max(nums)
        index = nums.index(major)
        nums.remove(major)
        for number in nums:
            if major >= number * 2:
                continue
            else:
                return -1
        return index

def main():
    nums = [3,6,1,0]
    sol = Solution()
    print(sol.dominantIndex(nums))

if __name__ == '__main__':
    main()