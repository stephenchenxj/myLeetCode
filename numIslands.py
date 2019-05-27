#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:48:42 2019

@author: dev
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
    
