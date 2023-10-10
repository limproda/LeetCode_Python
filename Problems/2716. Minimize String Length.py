#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return(len(set(s)))

def main():
    s = "aaabc"
    sol = Solution()
    print(sol.minimizedStringLength(s))

if __name__ == '__main__':
    main()