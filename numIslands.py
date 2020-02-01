#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:48:42 2019

@author: dev

200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

Accepted
531,507
Submissions
1,194,056
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None:
            return 0
        
        num = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print (grid[i][j])
                if grid[i][j] == '1':
                    num += 1
                    self.DFS_clear_adjacent_land(grid, i, j)
        return num
    
    def DFS_clear_adjacent_land(self, grid, i, j):
        if( i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1'):
            return None
        grid[i][j] = '0'
        self.DFS_clear_adjacent_land(grid, i-1, j)
        self.DFS_clear_adjacent_land(grid, i+1, j)
        self.DFS_clear_adjacent_land(grid, i, j-1)
        self.DFS_clear_adjacent_land(grid, i, j+1)
        
                
        
        
        
        
        
def main():
    grid = [ ['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0'] ]
    print( Solution().numIslands(grid))
    
if __name__ == '__main__':
    main()
    
