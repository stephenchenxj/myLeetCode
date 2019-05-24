#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 08:29:49 2019

@author: dev
"""


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.head = self.tail = 0
        self.size = k
        self.len = 0
        self.array = [None]*k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.len < self.size:
            self.tail += 1
            if self.tail >= self.size:
                self.tail -= self.size
            self.array[self.tail] = value
            self.len += 1
            if self.len == 1:
                self.head = self.tail
            return True
        else:
            return False
            

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty() == False: # not empty
            self.head += 1
            if self.head >= self.size:
                self.head -= self.size
            self.len -= 1
            return True
        
        else: # empty, can't deQueue
            return False
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.len > 0:
            #print(self.head)
            #print(self.array[self.head])
            return self.array[self.head]
        else:
            return -1
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.len > 0:
            return self.array[self.tail]
        else:
            return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.len == 0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.len == self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(2)
param_1 = obj.enQueue(1)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()