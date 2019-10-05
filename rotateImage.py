# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:17:55 2019

@author: stephen.chen
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # get dimension
        if n == 0:
            return
        
        for i in range(int((n+ 1)/2) ): # get dimension n
            for j in range(i,n-i-1):
                temp = matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=temp
        
        
        
        
        
def main():
    image = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[8,9,10,11]]
    print (image)
    mySolution = Solution()
    mySolution.rotate(image)
    print(image)
    

if __name__ == "__main__":
    main()
