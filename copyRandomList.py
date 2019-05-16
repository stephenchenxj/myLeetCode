#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:33:49 2019

@author: dev
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