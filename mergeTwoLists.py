#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:53:58 2019

@author: dev
"""

 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        head = None
        currentN1 = l1
        currentN2 = l2
        current = None
        
        
        while currentN2 and currentN1:
            if currentN2.val < currentN1.val:
                if head == None:
                    head = current = currentN2
                else:
                    current.next = currentN2
                    current = currentN2
                    
                currentN2 = currentN2.next    
                v = current.val
                v1 = currentN1.val
                v2 = currentN2.val

                    
            else: #currentN2.val >= currentN1.val
                if head == None:
                    head = current = currentN1
                else:
                    current.next = currentN1
                    current = currentN1
                
                currentN1 = currentN1.next 
                
        if currentN1 == None:
            current.next = currentN2  
        else:
            current.next = currentN1
                

            
        
        return head


def main():
    node1 = ListNode(1)  
    node2 = ListNode(2)
    node3 = ListNode(4)  
    node4 = ListNode(1)
    node5 = ListNode(3)  
    node6 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    
    node4.next = node5
    node5.next = node6
    
    merged = Solution().mergeTwoLists(node1, node4)
    
    while merged:
        print (merged.val)
        merged = merged.next
      
if __name__ == '__main__':
    main()