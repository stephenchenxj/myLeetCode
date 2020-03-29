# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 02:41:59 2019

@author: stephen.chen
994. Rotting Oranges
Easy

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

 

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.

Accepted
26,530
Submissions
57,255
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        
        ans = 0
        newRotten = []
        rotting = []
        fresh = dict()
        for i in range(row):
            for j in range(col):
                if grid[i][j]== 2:
                    newRotten.append((i,j))
                elif grid[i][j]==1:
                    fresh[(i,j)] = True
        if not newRotten and fresh:
            return -1
        elif not fresh:
            return 0
        #print(fresh)        
        while newRotten:
            loc = newRotten.pop()
            if fresh.get((loc[0]+1,loc[1])):
                rotting.append((loc[0]+1,loc[1]))
                fresh.pop((loc[0]+1,loc[1]))
            if fresh.get((loc[0]-1,loc[1])):
                rotting.append((loc[0]-1,loc[1]))
                fresh.pop((loc[0]-1,loc[1]))
            if fresh.get((loc[0],loc[1]+1)):
                rotting.append((loc[0],loc[1]+1))
                fresh.pop((loc[0],loc[1]+1))
            if fresh.get((loc[0],loc[1]-1)):
                rotting.append((loc[0],loc[1]-1))
                fresh.pop((loc[0],loc[1]-1))
            
            if not newRotten:
                newRotten = rotting[:]
                rotting = []
                ans+=1
        if fresh:
            return -1

        return ans-1
    
test = Solution()
grid = [[2,1,1],[0,1,1],[1,1,1]]
print(test.orangesRotting(grid))
print(test.orangesRotting([[0]]))
print(test.orangesRotting([[0,2]]))
print(test.orangesRotting([[2],[1],[1],[1],[2],[1],[1]]))
            
            
        

