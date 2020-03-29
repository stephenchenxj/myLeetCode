#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:41:03 2020

@author: stephenchen
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rslt = [[0 for i in range(n)] for j in range(n)] 
        
        visited = dict()
        
        def isBoundry(i,j):
            if i >= n or i < 0 or j >= n or j < 0:
                return True
            if visited.get((i,j)) == True:
                return True
            return False
        
        state = 1 # 4 state: 1: right, 2: down, 3: left, 4: up
        r = 0
        c = 0
        for i in range(1,n*n+1):
            
            visited[(r,c)] = True
            rslt[r][c] = i
            
            if state == 1:
                c += 1
            elif state == 2:
                r += 1
            elif state == 3:
                c -= 1
            elif state == 4:
                r -= 1
                
            if isBoundry(r,c): # reached boundry, change state
                if state == 1:
                    state = 2
                    c -= 1
                    r += 1
                elif state == 2:
                    state = 3
                    r -= 1
                    c -= 1
                elif state == 3:
                    state = 4
                    c += 1
                    r -= 1
                elif state == 4:
                    state = 1
                    r += 1
                    c += 1
                    

                    
        return rslt
    
    
print(Solution().generateMatrix(3))