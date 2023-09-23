#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def frequencySort(self, nums):
        frequency = {}
        self.frequencyCounter(nums, frequency)
        sortedList = sorted(nums, key=lambda x: (frequency[x], -x))
        return sortedList
    
    def frequencyCounter(self, nums, frequency):
        for number in nums:
            if number in frequency:
                counter = frequency[number]
                frequency[number] = counter + 1
            else:
                frequency[number] = 1
        



def main():
    nums = [0,1,2,3]
    sol = Solution()
    print(sol.frequencySort(nums))
if __name__ == '__main__':
    main()