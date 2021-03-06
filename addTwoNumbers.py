#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:43:08 2019

@author: dev

2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Accepted
1,193,725
Submissions
3,655,839
"""

 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def addTwoNumbers(self, c1, c2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if c1 == None:
            return c2
        if c2 == None:
            return c1
        
        
        forward = 0       
        
        currentNode = None
        head = None
        while c1 or c2 or forward > 0:
            v = 0
            if c1:
                v += c1.val
                c1 = c1.next
            if c2:
                v += c2.val
                c2 = c2.next
            v += forward
            if v > 9:
                v = v - 10
                forward = 1
            else:
                forward = 0
                
            if currentNode == None:
                head = currentNode = ListNode(v)
            else:
                currentNode.next = ListNode(v)
                currentNode = currentNode.next
            
        return head
            
            

def main():
    node1 = ListNode(1)  
    node2 = ListNode(2)
    node3 = ListNode(4)  
    node4 = ListNode(1)
    node5 = ListNode(9)  
    node6 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    
    node4.next = node5
    node5.next = node6
    
    merged = Solution().addTwoNumbers(node1, node4)
    
    while merged:
        print (merged.val)
        merged = merged.next
      
if __name__ == '__main__':
    main()
        