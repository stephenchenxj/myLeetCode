#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:52:32 2019

@author: dev
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre_even = None
        pre_odd = None
        oddHead = None
        
        node = head
        index = 0
        while node.next:
            if index %2 == 0: #even
                if pre_even == None: # first ever even
                    pre_even = node
                else: #got even node before
                    pre_even.next = node
                    pre_even = node
            else: # odd
                if pre_odd == None: # first ever even
                    pre_odd = node
                    oddHead = node
                else: #got even node before
                    pre_odd.next = node
                    pre_odd = node
            
            index +=1
            node = node.next
        pre_even.next = oddHead
        return head
        
        
        
def main():
    nodeA = ListNode(1)    
    nodeB = ListNode(2)
    nodeC = ListNode(3)
    nodeD = ListNode(4)
    nodeE = ListNode(5)
    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE
    
    mySolution = Solution()
    result = mySolution.oddEvenList(nodeA)
    
    while result:
        print(result.val)
        result = result.next
    
    
if __name__ == '__main__':
    main()
    