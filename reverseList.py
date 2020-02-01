#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:49:24 2019

@author: dev

206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
Accepted
807,708
Submissions
1,364,506

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        newHead = head
        movingNode = head
        oldHead = head
        
        while movingNode.next:
            newHead = movingNode.next
            movingNode.next = movingNode.next.next
            newHead.next = oldHead            
            oldHead = newHead
        return newHead