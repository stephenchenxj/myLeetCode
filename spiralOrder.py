#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 14:42:40 2019

@author: dev
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m = len(matrix)
        if not m:
            return result   
        
        if isinstance(matrix[0], int):
            return matrix
        
        n = len(matrix[0])  
        
        subMatrix = []
        if n > 2:
            if m >3:            
                for i in range(m-2):
                    subMatrix.append(matrix[i+1][1:n-1])
            elif m == 3:
                subMatrix=(matrix[1][1:n-1])
                
        if m == 1:
            return matrix[0]
        if n == 1:
            for i in range(m):
                result.append(matrix[i][0])
            return result
        
        
        for i in range(n):
            result.append(matrix[0][i])
        for i in range(m-2):
            result.append(matrix[i+1][n-1])
        for i in range(n):
            result.append(matrix[m-1][n-i-1])
        for i in range(m-2):
            result.append(matrix[m-i-2][0])
        
        
        result.extend(self.spiralOrder(subMatrix))
                
                
        return result
                
            
        
        
        
def main():
    matrix = [[1],[2],[3]]
    
    
    ret = Solution().spiralOrder(matrix)
    print(ret)
    
if __name__ == '__main__':
    main()
        