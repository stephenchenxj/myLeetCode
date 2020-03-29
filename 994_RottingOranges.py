#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:24:26 2020

@author: stephenchen
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        queue = []
        minutes = 0
        
        
        
        def findRotten():
            cnt = 0
            m = len(grid)
            n = len(grid[0])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        cnt += 1
                        queue.append((i,j))
            return cnt
        
        def findFresh():
            cnt = 0
            m = len(grid)
            n = len(grid[0])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        cnt += 1
            return cnt
        
        def infect(i,j):
            cnt = 0 
            m = len(grid)
            n = len(grid[0])
            if i+1 < m:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1, j))
                    cnt += 1
            if i-1 >= 0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i-1, j))
                    cnt += 1
            if j+1 < n:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i, j+1))
                    cnt += 1
            if j-1 >= 0:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i, j-1))
                    cnt += 1
            return cnt
        
        
        if findFresh() == 0:
            return minutes
        
        cnt = findRotten()
        if cnt == 0:
            return -1
        newCnt = 0
        while queue:
            loc = queue.pop(0)
            cnt -= 1
            newCnt += infect(loc[0], loc[1])
            
            if cnt == 0:
                if newCnt > 0:
                    cnt = newCnt
                    newCnt = 0
                    minutes += 1
        
        if findFresh() > 0:
            return -1
        
        return minutes
    
    
grid = [[0,2]]

print(Solution().orangesRotting(grid))
            