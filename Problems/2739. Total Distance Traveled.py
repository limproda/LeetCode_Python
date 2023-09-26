#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def distanceTraveled(self, mainTank,additionalTank):
        counter = 0
        km = 0
        while mainTank > 0:
            mainTank -= 1
            km += 10
            counter += 1
            if counter == 5 and additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
                counter = 0
        return km
def main():
    sol = Solution()
    print(sol.distanceTraveled(9,1))
if __name__ == '__main__':
    main()