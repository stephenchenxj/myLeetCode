#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:15:15 2020

@author: chen

83. Remove Duplicates from Sorted List
Easy

1257

100

Add to List

Share
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
        preNode = head
        node = head.next
        while node:
            if node.val == preNode.val: # delete this node
                preNode.next = node.next
            else:
                preNode = node
            node = node.next
            
        return head