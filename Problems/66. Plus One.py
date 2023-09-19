#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        map(str, array): Transform every element of the array into a string so we can use join.
        ''.join(...): Combine all the elements into one string
        """
        integer = int(''.join(map(str, digits))) +1
        return [int(digito) for digito in str(integer)]
        
def main():
    sol = Solution()

    digits = [4,3,2,1]
    print(sol.plusOne(digits))

if __name__ == '__main__':
    main()