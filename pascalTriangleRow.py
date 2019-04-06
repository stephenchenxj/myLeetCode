#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:56:56 2019

@author: dev
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        
        lastRow = [None]*(rowIndex)
        currentRow = [None]*(rowIndex+1)
        
        #lastRow[0] = 1
        for i in range(1,rowIndex+1):
            currentRow[0] = 1
            currentRow[i] = 1
            for j in range(1,i):                
                currentRow[j] = lastRow[j]+lastRow[j-1]
            #lastRow = currentRow # it is wrong! can not! Python passes list by Reference
            lastRow = currentRow[:]
        return currentRow
        
        
        
        
def main():
    ret = Solution().getRow(5)
    print(ret)
    
if __name__ == '__main__':
    main()