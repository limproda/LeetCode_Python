#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Another approach:
        class Solution:
            def hammingWeight(self, n: int) -> int:
                ans = 0
                while n:
                bit = n & 1 # bit mask, and a different one: n = n & (n-1)
                ans += bit
                n >>= 1
                return ans
"""
class Solution:
    def hammingWeight(self, n):
        counter = 0
        bits = bin(n)
        for bit in bits:
            if bit == "1":
                counter += 1
            return counter

def main():
    sol = Solution()
    n = 0b00000000000000000000000000001011
    print(sol.hammingWeight(n))

if __name__ == '__main__':
    main()
        