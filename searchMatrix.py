# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:22:23 2019

@author: stephen.chen

Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.


"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if (matrix[0])==[]:
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        def mayExist(matrix, target, tl_r, tl_c, br_r, br_c):    
            if br_r-tl_r <=1 or br_c-tl_c <=1:
                for i in range(tl_r, br_r+1):
                    for j in range(tl_c, br_c+1):
                        if matrix[i][j] == target:
                            return 0
                return -1
            
            if matrix[tl_r][tl_c] < target and matrix[br_r][br_c] > target:
                return 1
            elif matrix[tl_r][tl_c] == target or matrix[br_r][br_c] == target:
                return 0
            else:
                return -1
        pool = [[0,0, row-1, col-1]]    
        while pool:
            area = pool.pop()
            temp = mayExist(matrix, target, area[0], area[1], area[2], area[3]) 
            if temp == 0:
                return True
            elif temp == -1: # no target in this area
                continue
            else: # target may exist in this area. Devide the area into 4 sub areas, add them into pool
                sub_tl=[area[0], area[1],int((area[0]+area[2])/2)-1,int((area[1]+area[3])/2)-1]
                sub_bl=[area[0], int((area[1]+area[3])/2), int((area[0]+area[2])/2)-1, area[3]]
                sub_tr=[int((area[0]+area[2])/2), area[1],area[2],int((area[1]+area[3])/2)-1]
                sub_br=[int((area[0]+area[2])/2),int((area[1]+area[3])/2), area[2], area[3]]
                
                pool.append(sub_tl)
                pool.append(sub_bl)
                pool.append(sub_tr)
                pool.append(sub_br)
                
        return False
                    
M = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

N = [[-1,3]]
t = 3
test = Solution()
print(test.searchMatrix(N, t))                
        
        
        
        