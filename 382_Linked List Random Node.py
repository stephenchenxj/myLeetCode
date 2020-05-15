#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:36:35 2020

@author: chen


382. Linked List Random Node
Medium

515

151

Add to List

Share
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
Accepted
66,223
Submissions
128,967

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import randint

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.cur = head
        node = head
        self.depth = 0
        while node:
            self.depth += 1
            node = node.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rand = randint(1, self.depth)
        for i in range(rand):
            if self.cur.next:
                self.cur = self.cur.next
            else:
                self.cur = self.head
        
        return self.cur.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
