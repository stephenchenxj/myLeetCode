#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:42:19 2020

@author: chen

62. Unique Paths
Medium

2711

189

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

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
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
Accepted
423,668
Submissions
814,308
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ht = dict()
        return self.dfs(m,n,1,1, ht)
        
        
    def dfs(self, m, n, c, r, ht):
        if (c,r) in ht:
            return ht[(c,r)]
        if c == m or r ==n:
            return 1
        ans = self.dfs(m, n, c+1, r, ht) + self.dfs(m, n, c, r+1, ht)
        ht[(c,r)] = ans
        return ans
    
    
    
class Solution_better(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
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
    
    
    


