#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:52:32 2019

@author: dev

328. Odd Even Linked List
Medium

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...

Accepted
192,993
Submissions
372,576

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
        if not head:
            return head
        pre_even = None
        pre_odd = None
        oddHead = None
        
        node = head
        index = 0
        while node:
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
        if pre_odd:
            pre_odd.next = None
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
    nodeE.next = None
    
    mySolution = Solution()
    result = mySolution.oddEvenList(nodeA)
    
    while result:
        print(result.val)
        result = result.next
    
    
if __name__ == '__main__':
    main()
    