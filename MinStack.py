#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:04:33 2019

@author: dev
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.index = -1
        self.minData = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.index += 1
        self.data.append( x )
        
        if self.index == 0:
            self.minData.append( x )
        else: 
            if self.minData[self.index - 1] > x:
                self.minData.append( x )
            else:
                self.minData.append( self.minData[self.index - 1] )
                
                
            
        
        
        
        

    def pop(self):
        """
        :rtype: None
        """
        if self.index >= 0: # not empty
            del self.data[self.index]
            del self.minData[self.index]
            self.index -= 1
        

    def top(self):
        """
        :rtype: int
        """
        if self.index >= 0:
            return self.data[self.index]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minData[self.index ]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()