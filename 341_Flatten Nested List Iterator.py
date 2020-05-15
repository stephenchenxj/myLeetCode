#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:08:37 2020

@author: chen

341. Flatten Nested List Iterator
Medium

1496

606

Add to List

Share
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
Accepted
158,300
Submissions
305,572

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """

#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """

#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger] ##!! Pay attention here: It is List of NestedInteger, not NestedInterger (or, NestedInteger of NestedInteger)
        """
        nestedList.reverse()
        self.stack = nestedList
        self.nextInt = None
        
    def next(self):
        """
        :rtype: int
        """
        return self.nextInt
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            item = self.stack.pop()
            if item.isInteger():
                self.nextInt = item.getInteger()
                return True
            else:
                items = item.getList()
                items.reverse()
                for i in items:
                    self.stack.append(i)
                return self.hasNext()
        else:
            return None
    
            
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())        
        

