#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def getRow(self, rowIndex):

        res = [1]
        if rowIndex == 0:
            return res
        res.append(1)
        if rowIndex == 1:
            return res
        for _ in range(2, rowIndex + 1):
            new_row = [1]  
            for i in range(1, len(res)):
                new_row.append(res[i - 1] + res[i]) 
            new_row.append(1)
            res = new_row 
        return res

                
def main():
    rowIndex = 4
    sol = Solution()
    print(sol.getRow(rowIndex))

if __name__ == '__main__':
    main()