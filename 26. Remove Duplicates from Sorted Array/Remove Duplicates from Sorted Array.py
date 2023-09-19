#!/usr/bin/env python
# -*- coding: utf-8 -*-
def removeDuplicates(nums):
        newList = []
        for number in nums:
            if number not in newList:
                 newList.append(number)
        return newList
def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
if __name__ == '__main__':
    main()