#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:40:28 2019

@author: dev

118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Accepted
326,646
Submissions
656,441
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result = [[1]]
        if numRows == 1:
            return result
        
        for i in range(1,numRows):
            #print(i)
            temp = []
            temp.append(1)
            for j in range(1,i):
                temp.append( result[i-1][j] + result[i-1][j-1])
            temp.append(1)
            result.append(temp)
        
        return result
        
        
        
        
        
def main():
    ret = Solution().generate(5)
    print(ret)
    
if __name__ == '__main__':
    main()