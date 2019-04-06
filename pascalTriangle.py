#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:40:28 2019

@author: dev
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result = [[1]]
        if numRows == 1:
            return result
        
        for i in range(1,numRows):
            #print(i)
            temp = []
            temp.append(1)
            for j in range(1,i):
                temp.append( result[i-1][j] + result[i-1][j-1])
            temp.append(1)
            result.append(temp)
        
        return result
        
        
        
        
        
def main():
    ret = Solution().generate(5)
    print(ret)
    
if __name__ == '__main__':
    main()