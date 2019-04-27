#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:41:00 2019

@author: dev
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
                    node2del = cur
                    cur = cur.next
                    del node2del
                else: 
                    head = cur.next
                    node2del = cur
                    cur = cur.next
                    del node2del
            else: # keep cur                
                pre = cur
                cur = cur.next
            
        return head
    
    
def main():
    nodeA = ListNode(1)    
    nodeB = ListNode(1)
    nodeA.next = nodeB
    
    mySolution = Solution()
    result = mySolution.removeElements(nodeA, 1)
    
    while result:
        print(result.val)
        result = result.next
    
    
if __name__ == '__main__':
    main()
    