#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
   def sortArrayByParity(self, nums):
        """ Another better solution:
        left_index, right_index = 0, len(nums) - 1
        while(left_index < right_index):
            if(nums[left_index] % 2 != 0):
                if(nums[right_index] % 2 == 0):
                    nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                    left_index += 1
                    right_index -= 1
                else:
                    right_index -=1
            else:
                left_index += 1

        return nums"""
        new_nums = []
        for element in nums:
            if element % 2 == 0:
                new_nums.insert(0, element)
            else:
                new_nums.append(element)
        return new_nums

def main():
    nums = [3,1,2,4]
    sol = Solution()
    print(sol.sortArrayByParity(nums))

if __name__ == '__main__':
    main()
