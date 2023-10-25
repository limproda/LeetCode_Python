#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def relocateMarbles(self, nums, moveFrom, moveTo):
        positions = set(nums) 

        for i in range(len(moveFrom)):
            if moveFrom[i] in positions:
                positions.remove(moveFrom[i])
                positions.add(moveTo[i])

        return sorted(positions)
    
def main():
    nums = [1,1,3,3]
    moveFrom = [1,3]
    moveTo = [2,2]
    sol = Solution()
    print(sol.relocateMarbles(nums, moveFrom, moveTo))

if __name__ == '__main__':
    main()