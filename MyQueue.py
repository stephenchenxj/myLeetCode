#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:21:22 2019

@author: dev
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.index = -1
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.index += 1
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        rst = self.queue[0]
        del self.queue[0]
        self.index -= 1
        return rst
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.queue[0]
        else:
            return 
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.index < 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())

print(obj.empty())