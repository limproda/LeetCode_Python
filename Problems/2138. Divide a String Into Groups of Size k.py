#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def divideString(self, s, k, fill):
        while len(s) % k != 0:
            s += fill
        return  [s[i:i+k] for i in range(0, len(s), k)]
    
def main():
    s = "abcdefgh"
    k = 3
    fill = "x"
    sol = Solution()
    print(sol.divideString(s, k, fill))

if __name__ == '__main__':
    main()