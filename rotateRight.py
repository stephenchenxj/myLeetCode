#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:32:12 2019

@author: dev
"""

 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        length = self.getLength(head)
        print(length)
        
        for i in range(k%length):
            head = self.rotateRightBy1(head)
        return head
    
    def getLength(self, head):
        length = 1        
        if head == None:
            return 0        
        node = head
        while node.next:
            node = node.next
            length += 1            
        return length
        
    
    def rotateRightBy1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head.next == None:
            return head
        
        #find tail and new tail
        node = head
        newTail = node.next
        while node.next:
            newTail = node
            node = node.next
            
        node.next = head        
        newTail.next = None
        
        return node
        
        
        
def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    #node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    mySolution = Solution().rotateRight(node1, 0)
    while mySolution:
        print(mySolution.val)
        mySolution = mySolution.next
        
if __name__ == '__main__':
    main()