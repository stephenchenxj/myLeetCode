#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:48:59 2019

@author: chen
"""

import math


class Solution(object):
    def calculateEntropy(self, input):
        """
        :type input: List[int]
        :rtype: float
        """
        p = dict()
        
        n = len(input)
        for i in input:
            if i not in p.keys():
                p[i] = float(input.count(i))/n
                
        #print (p)
        
        entropy = 0
        for i in p.keys():
            #print(p[i])
            entropy += -1*p[i]*math.log(p[i],2)
            
        return entropy
            
        
        
        
input = [1,1,2,2]
print(Solution().calculateEntropy(input))
