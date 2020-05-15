#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:05:14 2020

@author: chen

694. Number of Distinct Islands
Medium

676

43

Add to List

Share
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.

Accepted
49,461
Submissions
90,344

"""

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #print(grid)
        maps = dict()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    steps = ""
                    moves = []
                    self.dfs(grid, r,c, 'o', moves)
                    steps = "".join(moves)
                    moves = []
                    maps[steps] = maps.get(steps, 0) + 1
        #print(maps)   
        
        return len(maps.keys())
        
    def dfs(self, grid, r, c, move, moves):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] == 1: #it is land
            grid[r][c] = "#"
            moves.append( move)
            self.dfs(grid, r+1, c, 'd', moves)
            moves.append( "u")
            self.dfs(grid, r-1, c, 'u', moves)
            moves.append( "d")
            self.dfs(grid, r, c+1, 'r', moves)
            moves.append( "l")
            self.dfs(grid, r, c-1, 'l', moves)
            moves.append( "r")
        else: # it is water
            return

grid = [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]
print(Solution().numDistinctIslands(grid))