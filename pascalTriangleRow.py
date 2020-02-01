#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:56:56 2019

@author: dev

119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

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