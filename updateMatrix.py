#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:27:15 2019

@author: dev
"""

class Solution(object):
    def findMinNb(self, matrix, i, j):
        minV = 10000
        if i+1 < len(matrix):
            if matrix[i+1][j] < minV:
                minV = matrix[i+1][j] 
        if i-1 >= 0:
            if matrix[i-1][j] < minV:
                minV = matrix[i-1][j] 
        if j+1 < len(matrix[0]):
            if matrix[i][j+1] < minV:
                minV = matrix[i][j+1] 
        if j-1 >= 0:
            if matrix[i][j-1] < minV:
                minV = matrix[i][j-1]
        return minV
            
    
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        haveUpdate = True
        
        while haveUpdate:
            haveUpdate = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 0:
                         newV = self.findMinNb(matrix, i, j) + 1
                         if matrix[i][j] != newV:
                             matrix[i][j] = newV
                             haveUpdate = True
        
        return matrix
                    
M = [[0],[1]]
print(Solution().updateMatrix(M))