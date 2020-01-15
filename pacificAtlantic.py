# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 05:01:54 2020

@author: stephen.chen

417. Pacific Atlantic Water Flow
Medium

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.

 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        
        
        
        pacificAccessable = dict()
        pacificAccessable[(0,0)] = True
        atlanticAccessable = dict()
        atlanticAccessable[(row-1, col-1)] = True
        toProcess = [(0,0)]
        
        processed = dict()
        
        def searchPacificAccessable(land, matrix, accessable, toProcess):                
            if land[0] > 0:
                if not accessable.get((land[0]-1, land[1])):
                    if matrix[land[0]-1][land[1]] >= matrix[land[0]][land[1]] or land[0]-1 == 0 or land[1] == 0:
                        accessable[(land[0]-1, land[1])] = True
                        toProcess.append((land[0]-1, land[1]))
            if land[1] > 0:
                if not accessable.get((land[0], land[1]-1)):
                    if matrix[land[0]][land[1]-1] >= matrix[land[0]][land[1]] or land[1]-1 == 0 or land[0] == 0:
                        accessable[(land[0], land[1]-1)] = True
                        toProcess.append((land[0], land[1]-1))
            if land[0] + 1 <= len(matrix)-1:
                if not accessable.get((land[0]+1, land[1])):
                    if matrix[land[0]+1][land[1]] >= matrix[land[0]][land[1]] or land[1] == 0 or land[0]+1 == 0:
                        accessable[(land[0]+1, land[1])] = True
                        toProcess.append((land[0]+1, land[1]))
            if land[1] + 1 <= len(matrix[0])-1:
                if not accessable.get((land[0], land[1]+1)):
                    if matrix[land[0]][land[1]+1] >= matrix[land[0]][land[1]] or land[0] == 0 or land[1]+1 == 0:
                        accessable[(land[0], land[1]+1)] = True
                        toProcess.append((land[0], land[1]+1))        
        def searchAtlanticAccessable(land, matrix, accessable, toProcess):                
            if land[0] > 0:
                if not accessable.get((land[0]-1, land[1])):
                    if matrix[land[0]-1][land[1]] >= matrix[land[0]][land[1]] or land[0]-1 == len(matrix)-1 or land[1] == len(matrix[0])-1:
                        accessable[(land[0]-1, land[1])] = True
                        toProcess.append((land[0]-1, land[1]))
            if land[1] > 0:
                if not accessable.get((land[0], land[1]-1)):
                    if matrix[land[0]][land[1]-1] >= matrix[land[0]][land[1]] or land[1]-1 == len(matrix[0])-1 or land[0] == len(matrix)-1:
                        accessable[(land[0], land[1]-1)] = True
                        toProcess.append((land[0], land[1]-1))
            if land[0] + 1 <= len(matrix)-1:
                if not accessable.get((land[0]+1, land[1])):
                    if matrix[land[0]+1][land[1]] >= matrix[land[0]][land[1]] or land[1] == len(matrix[0])-1 or land[0]+1 == len(matrix)-1:
                        accessable[(land[0]+1, land[1])] = True
                        toProcess.append((land[0]+1, land[1]))
            if land[1] + 1 <= len(matrix[0])-1:
                if not accessable.get((land[0], land[1]+1)):
                    if matrix[land[0]][land[1]+1] >= matrix[land[0]][land[1]] or land[0] == len(matrix)-1 or land[1]+1 == len(matrix[0])-1:
                        accessable[(land[0], land[1]+1)] = True
                        toProcess.append((land[0], land[1]+1))           
            
        
        while toProcess:
            land = toProcess.pop(0)
            searchPacificAccessable(land, matrix, pacificAccessable, toProcess)
        
        toProcess = [(row-1, col-1)]
        while toProcess:
            land = toProcess.pop(0)
            searchAtlanticAccessable(land, matrix, atlanticAccessable, toProcess)
            
        result = []    
        for i in range(row):
            for j in range(col):
                if pacificAccessable.get((i,j)) and atlanticAccessable.get((i,j)):
                    result.append([i,j])
                    
        return result
    
        
test = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(test.pacificAtlantic(matrix))
