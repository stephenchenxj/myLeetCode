#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:50:30 2020

@author: chen


82. Remove Duplicates from Sorted List II
Medium

1375

100

Add to List

Share
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
Accepted
232,181
Submissions
650,228

"""


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def display(self, head):
        while head:
            print(head.val)
            head=head.next
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        #create a dummy head, 
        dummyH = ListNode(0)
        cur = head
        #dummy head point to the current node. the current node may update in the following while loop
        dummyH.next = cur 
        #create pre to record the valid previous node, initiate it to the dummy head
        pre = dummyH 
        
        while cur and cur.next: # if current and next node both exist
            #from the current node, find the first node with different val
            while cur.next and cur.val == cur.next.val: 
                cur=cur.next
            #after the above while loop, cur and next node have different val
            #for instance, given [2,2,2,3,3], before the while loop, if cur node is 2, after the while loop
            # cur node is the third 2 now, and next node is the first 3.
            
            #since last time update pre.next, cur is not updated, 
            #it means cur.next has different value with cur. so update the pre by pre=cur
            if pre.next == cur: 
                pre = cur
            else: #since last time update pre.next, cur is updated. update pre.next, delete cur from the list
                pre.next =cur.next
            
            #finish one round, point to the next node
            cur = cur.next
        
        return dummyH.next
    
    
    
n1 = ListNode(1)       
n2 = ListNode(2)   
n3 = ListNode(2)   
n4 = ListNode(3)   
n5 = ListNode(4)    
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

h = Solution().deleteDuplicates(n1)
Solution().display(h)