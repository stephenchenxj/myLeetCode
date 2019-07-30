#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:04:33 2019

@author: dev
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, c1, c2):
        
        if c1 == None:
            return c2
        if c2 == None:
            return c1

        forward = 0
        val = c1.val + c2.val
        if val > 9:
            val = val%10
            forward = 1
        else:
            forward = 0
        head = ListNode(val)
        
        a = c1.next
        b = c2.next
        currentNode = head
        
        while a or b or forward: 
            val = 0
            
            if a:
                val += a.val
            if b:
                val += b.val
            val += forward
            if val > 9:
                val = val%10
                forward = 1
            else:
                forward = 0
            
            newNode = ListNode(val)
            currentNode.next = newNode
            currentNode = newNode
            
            
            if a:
                a = a.next
            if b:
                b = b.next
            
            
        return head
    
    
c1 = ListNode(2)
c1_1 = ListNode(4)
c1_2 = ListNode(3)
c1.next = c1_1
c1_1.next = c1_2

c2 = ListNode(5)
c2_1 = ListNode(6)
c2_2 = ListNode(4)
c2.next = c2_1
c2_1.next = c2_2

print(Solution().addTwoNumbers(c1, c2))