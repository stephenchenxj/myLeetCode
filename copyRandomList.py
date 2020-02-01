#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:33:49 2019

@author: dev

138. Copy List with Random Pointer
Medium

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

 

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.

 

Constraints:

    -10000 <= Node.val <= 10000
    Node.random is null or pointing to a node in the linked list.
    Number of Nodes will not exceed 1000.

Accepted
337,694
Submissions
1,054,559
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        map = {None : None}
        temp = head
        while temp:
            map[temp] = Node(temp.val,temp.next,temp.random)
            temp = temp.next
        print(map)
        temp = head
        while temp:
            map[temp].next = map[temp.next]
            map[temp].random = map[temp.random]
            temp = temp.next
        return map[head]
            



def main():
    node1 = Node(1)  
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.next = None
    node2.random = node2
    

    
    
    copiedList = Solution().copyRandomList(node1)
    
    while copiedList:
        print (copiedList.val)
        copiedList = copiedList.next
if __name__ == '__main__':
    main()