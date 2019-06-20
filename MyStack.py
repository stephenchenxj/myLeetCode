#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:41:45 2019

@author: dev
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.index = -1
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        
        self.stack.append(x)
        self.index += 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        rst = self.stack[self.index]
        del self.stack[self.index]
        self.index -= 1
        return rst
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        
        if not self.empty():
            return self.stack[self.index]
        else:
            return 
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        
        if self.index < 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)