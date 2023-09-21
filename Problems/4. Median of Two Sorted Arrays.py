#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        return self.calculateMedian(merged)
    
    def calculateMedian(self, merged):
        if len(merged) % 2 == 0:
            mid1 = merged[len(merged) // 2]
            mid2 = merged[len(merged) // 2 -1]
            return (mid1 + mid2) / 2.0
        else:
            return float(merged[len(merged) // 2])
        
        
    
def main():
    sol = Solution()
    nums1 = [1,3]
    nums2 = [2,4]
    print(sol.findMedianSortedArrays(nums1,nums2))
if __name__ == '__main__':
    main()