#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:45:50 2019

@author: chen
"""

import math

class Solution(object):
    tempResult = {}
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxNum = int(math.sqrt(n))
        
        #print(maxNum)
        nodes =[]
        for i in range(maxNum):
            nodes.append ( (maxNum - i)**2 )
        #print(nodes)
        
        num = 0
        minCount = n
        
        
        i = 0
        for node in nodes:
            i += 1
            if (n-node) not in self.tempResult.keys():
                self.tempResult[n-node] =  self.numSquares(n - node)
            num = 1 + self.tempResult[n-node]
            if minCount > num:
                minCount = num
                
            if i > 20:
                break
        
        return minCount
        
def main():
    print(Solution().numSquares(7168))
    
if __name__ == '__main__':
    main()