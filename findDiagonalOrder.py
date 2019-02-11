# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix)
        
        if r == 0:
            return []
        
        c = len(matrix[0])
        print(r)
        print(c)
        
        print(matrix[r-1][c-1])
        
        result = []
        
        for i in range(r-1+c):
            print('i = %d' %i)
            if i%2 == 0:
                #go up right
                for j in range(i+1):
                    if (i-j) < r and j < c:
                        result.append(matrix[i-j][j])
            else:
                #go down left
                for j in range(i+1):
                    if(i-j) <c and j<r:
                        result.append(matrix[j][i-j])
        return result
        
        
def main():
    
    print(len([]))

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ret = Solution().findDiagonalOrder(matrix)
    print(ret)
    
if __name__ == '__main__':
    main()