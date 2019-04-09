#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:49:28 2019

@author: dev
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