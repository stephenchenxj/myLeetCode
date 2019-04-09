#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:52:21 2019

@author: dev
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = 0
        
        if head == None:
            return -1
        currentNode = head
        
        nodeSet = set()
        while currentNode:
            if currentNode not in nodeSet:
                nodeSet.add(currentNode)
                print(nodeSet)
                index += 1
            else:
                print(index)
                return index
            currentNode = currentNode.next
            
        return -1