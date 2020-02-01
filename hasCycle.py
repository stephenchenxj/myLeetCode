#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:49:28 2019

@author: dev

141. Linked List Cycle
Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
Accepted
526,996
Submissions
1,337,843

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def setNext(self, node):
        self.next = node
        
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None or head.next == None:
            return False
        
        fastNode = head 
        slowNode = head
        
        while fastNode != None:        
            fastNode = fastNode.next
            if fastNode == None:
                return False
            fastNode = fastNode.next
            slowNode = slowNode.next
            
            if fastNode == slowNode:
                return True
        
        return False

def main():
    n1 =  ListNode(3)
    n2 =  ListNode(2)
    n3 =  ListNode(0)
    n4 =  ListNode(-4)
    
    '''
    n1.setNext(n2)
    n2.setNext(n3)
    n3.setNext(n4)
    n4.setNext(n2)
    '''
    
    '''
    n1.setNext(n2)
    n2.setNext(n1)
    '''
    
    test = Solution()
    print(test.hasCycle(n1))
    
        
        
if __name__ == '__main__':
    main()