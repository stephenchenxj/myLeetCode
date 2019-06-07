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
        biggersIndex = [] # only push the local temperature peaks into the stack. 
        #the highest temperature's index should be at the bottomn. pop peaks if they are surpassed by newer temperature peaks
        days[num-1] = 0
            
        for i in range(1, num):
            #print(T[num-i-1])
            a = T[num-i-1]
            if T[num-i-1] < T[num-i]:
                days[num-i-1] = 1
                biggersIndex.append(num-i) #push day after today index into stack: the temperature of current day is lower than the next day
            else:
                while biggersIndex:
                    higherTempIndex = biggersIndex[-1] #get the top value in the stack, without removing it.
                    if T[num-i-1] < T[higherTempIndex]:
                        days[num-i-1] =  higherTempIndex - (num-i-1)
                        break
                    biggersIndex.pop() #remove the index (the future day) on the top, as the temperature of the current day is higher than (or equal to) the future day. 
                    # No need to keep that future day in the rest of the comparason. 
            
            
            
            
        return days
                
 
print(Solution().dailyTemperatures([47,34,47,34,47,49,50,48]))