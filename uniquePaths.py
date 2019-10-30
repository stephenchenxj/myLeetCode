# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 05:30:23 2019

@author: stephen.chen
Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28


                                    []
                    d                               r
            d               r               d               r
        d       r       d       r       d       r       d       r
        
        d: col + 1
        r: row + 1

"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        self.count = 0
        #initial position
        r = 0
        c = 0
        
        '''
        def dfs(m,n,r,c,path):
            temp = path[:] 
            if r < m-1:
                temp.append('d')
                dfs(m, n, r+1, c, temp)
                temp.pop()
            if c < n-1:     
                temp.append('r')
                dfs(m, n, r, c+1, temp)
                temp.pop()
            if r==m-1 and c==n-1:                
                self.count += 1        
        path = []
        dfs(m,n,r,c,path)
        '''
        
        '''
        # still too slow :(
        def dfs(m,n,r,c):
            if r < m-1:
                dfs(m, n, r+1, c)
            if c < n-1:     
                dfs(m, n, r, c+1)
            if r==m-1 and c==n-1:                
                self.count += 1  
        dfs(m,n,r,c)
        return self.count
        '''
        
        
        array = [[0 for j in range(n)] for i in range(m)]
        array[0][0] = 1
        
        # can not use this: matrix = m*[n*[0]]
        # because you end up with m copies of the same list, so when you modify one of them they all change
#         matrix = 5*[5*[0]]
#         matrix
#         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#         matrix[4][4] = 2
#         matrix
#         [[0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2]]
        
        for r in range(0,m):
            for c in range(0,n):
                if r == 0 and c == 0:
                    continue
                else:
                    array[r][c] = array[r][c-1] + array[r-1][c]
        return array[m-1][n-1]
    
    
    
        
test = Solution()

print(test.uniquePaths(23,12))

        
        
        