# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 03:52:09 2019

@author: stephen.chen
1162. As Far from Land as Possible
Medium

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

 

Note:

    1 <= grid.length == grid[0].length <= 100
    grid[i][j] is 0 or 1

Accepted
9,256
Submissions
22,675

"""
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # find all land first
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
        if len(q) == 0 or len(q) == (i+1)*(j+1):
            return -1
                    
        def fill(loc, q):
            i = loc[0]
            j = loc[1]            
            if (i + 1) < len(grid):
                if grid[i+1][j] == 0:
                    grid[i+1][j] = grid[i][j] + 1
                    q.append((i+1,j))
                else:
                    grid[i+1][j] = min(grid[i+1][j] + 1, grid[i+1][j])
            if (i - 1) >= 0:
                if grid[i-1][j] == 0:
                    grid[i-1][j] = grid[i][j] + 1
                    q.append((i-1,j))
                else:
                    grid[i-1][j] = min(grid[i-1][j] + 1, grid[i-1][j])
            if (j + 1) < len(grid[0]):
                if grid[i][j+1] == 0:
                    grid[i][j+1] = grid[i][j] + 1
                    q.append((i,j+1))
                else:
                    grid[i][j+1] = min(grid[i][j+1] + 1, grid[i][j+1])
            if (j - 1) >= 0:
                if grid[i][j-1] == 0:
                    grid[i][j-1] = grid[i][j] + 1
                    q.append((i,j-1))
                else:
                    grid[i][j-1] = min(grid[i][j-1] + 1, grid[i][j-1])
        
        while q:            
            land = q.pop(0)      
            fill(land, q)
        return max(max(x) for x in grid) -1
    
test = Solution()
m = [[1,0,0],[0,0,0],[0,0,0]]
print(test.maxDistance(m))

