#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:06:55 2020

@author: stephenchen
"""


class Solution(object):
    
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        

        
        history = dict()
        
        def recursion(d,f,target, history):
            ways = 0
            if target > d*f or target < d:
                return ways
        
            if d == 1:
                ways = 1
            else:
                for i in range(1, f+1):
                    if (d-1, target -i) not in history.keys():
                        temp = recursion(d-1, f, target-i, history)
                        history[(d-1, target - i)] = temp
                    else:
                        temp = history[(d-1, target - i)]
                    ways += temp 
            
            return ways%(10**9 +7)
        
        return recursion(d,f,target, history)
            
print(Solution().numRollsToTarget(30,30,500))