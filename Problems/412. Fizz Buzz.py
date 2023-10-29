#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def fizzBuzz(self, n):
        res = []
        for number in range(1, n+1):
            if number%3 == 0 and number%5 == 0:
                res.append("FizzBuzz")
            elif number%3 == 0:
                res.append("Fizz")
            elif number%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(number))
        return res

def main():
    n = 15
    sol = Solution()
    print(sol.fizzBuzz(n))

if __name__ == '__main__':
    main()