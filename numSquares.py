#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:45:50 2019

@author: chen
"""

import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxNum = int(math.sqrt(n))
        
        #print(maxNum)
        node =[]
        for i in range(maxNum):
            node.append ( (maxNum - i)**2 )
        #print(node)
        
def main():
    print(Solution().numSquares(17))
    
if __name__ == '__main__':
    main()