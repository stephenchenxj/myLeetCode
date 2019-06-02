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
        
        #create a list of squares, from 1 to int(sqrt(n))
        squares =[]
        for i in range(1,n):
            square = i**2
            if square > n:
                break
            squares.append ( square )
        #print(nodes)
        
        num = 0
        
        #initialize the toCheck set (use set, not list, because don't want to check repeated values)
        toCheck = {n}
        
        while toCheck:
            
            nextLayer = set() #create a set for the next layer value to toCheck
            num += 1 #num +1 for each layer
            
            for value in toCheck: #traverse all the values in the toCheck set
                if value in squares: # if the value is a square itself, return num
                    return num
                for square in squares: #traverse all the squares in the list
                    if value < square: # value can't consist this square, skip all bigger squares
                        break
                    nextLayer.add(value - square)#current value consists value and square. So the next layer value will be (value - square)
            
            toCheck = nextLayer # update toCheck set
            
        return num
        
        
        

        
def main():
    print(Solution().numSquares(120))
    
if __name__ == '__main__':
    main()