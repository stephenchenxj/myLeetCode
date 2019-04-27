#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:41:00 2019

@author: dev
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        cur = head
        
        while cur:
            if cur.val == val: # need to delete cur
                if pre: # got pre node
                    pre.next = cur.next
                else: 
                    head = cur.next
            pre = cur
            cur = cur.next
            
        return head