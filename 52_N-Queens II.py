#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:40:19 2020

@author: chen

52. N-Queens II
Hard

428

139

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = dict()
        diff = dict()
        summ = dict()
        if (n <= 0):
            return 0
        return self.dfs(0, n, col, diff, summ, 0)
    def dfs(self, level, n, col, diff, summ, ans):
        if level == n:
            ans += 1
            return ans
        for i in range(n):
            if not col.get(i) and not diff.get(level-i) and not summ.get(level+i) :
                col[i] = True
                diff[level-i] =True
                summ[level+i] = True
                ans = self.dfs(level +1, n, col, diff, summ, ans)
                del col[i]
                del diff[level -i]
                del summ[level +i]
        return ans
        
print(Solution().totalNQueens(4))