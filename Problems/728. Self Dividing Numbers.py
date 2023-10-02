#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for number in range(left, right + 1):
            values = str(number)
            self_divider = True
            for digit in values:
                if digit == '0' or number % int(digit) != 0:
                    self_divider = False
                    break
            if self_divider:
                    result.append(number)
        return result

def main():
    left, right = 1, 22
    sol = Solution()
    print(sol.selfDividingNumbers(left, right))

if __name__ == '__main__':
    main()