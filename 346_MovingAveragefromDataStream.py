#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:10:53 2020

@author: stephenchen

346. Moving Average from Data Stream
Easy

480

50

Add to List

Share
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
 

Accepted
107,939
Submissions
155,834

"""


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        
        self.size = size
        self.cnt = 0
        self.sum = 0
        self.history = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.cnt += 1
        
        if self.cnt <= self.size:
            self.sum += val
            self.history.append(val)
            return float(self.sum)/self.cnt
        else:
            self.sum += val
            self.sum -= self.history.pop(0)
            self.history.append(val)
            return float(self.sum)/self.size