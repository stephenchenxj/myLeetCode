# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 04:42:52 2019

@author: stephen.chen

Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        index = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j]== 0:
                    index.append([i,j])
        
        for pos in index:
            for i in range(row):
                for j in range(col):
                    matrix[pos[0]][j] = 0
                    matrix[i][ pos[1]] = 0
                    
        
m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
        
test = Solution()
(test.setZeroes(m))
print(m)


