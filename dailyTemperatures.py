#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:06:45 2019

@author: dev
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        num = len(T)
        days = [0]*num
        biggersIndex = []
        days[num-1] = 0
            
        for i in range(1, num):
            print(T[num-i-1])
            if T[num-i-1] < T[num-i]:
                days[num-i-1] = 1
                biggersIndex.append(num-i)
            else:
                while biggersIndex:
                    higherTempIndex = biggersIndex.pop()
                    if T[num-i-1] < T[higherTempIndex]:
                        days[num-i-1] =  higherTempIndex - (num-i)
                        break
            
            
            
            
        return days
                
 
print(Solution().dailyTemperatures([47,34,47,34,47,49,50,48]))