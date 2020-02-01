#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:08:03 2019

@author: dev

430. Flatten a Multilevel Doubly Linked List
Medium

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []

 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

 

Constraints:

    Number of Nodes will not exceed 1000.
    1 <= Node.val <= 10^5

Accepted
52,912
Submissions
109,880
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head == None:
            return head
        
        currentNode = head
        node2connect = []
        
        # exist condition: no more next node or no more node to connect
        while currentNode.next or node2connect !=[] or currentNode.child: 
            #print(currentNode.val)
            if currentNode.child: # got child
                if currentNode.next: # and it got next
                    currentNode.next.prev = None # clear the prev. it will get new prev anyway
                    node2connect.append( currentNode.next )
                    #print(currentNode.next.val)
                child = currentNode.child
                currentNode.next = child
                currentNode.child = None
                child.prev = currentNode
                currentNode = child
                
            else: # no child
                if currentNode.next:
                    currentNode = currentNode.next
                    #print(currentNode.val)
                elif node2connect !=[]: # currentNode.next == None, and node2connect got items
                    node = node2connect.pop()                    
                    if node: # not empty node
                        #print(node.val)
                        currentNode.next = node
                        node.prev = currentNode
                        currentNode = node
                    else:
                        currentNode.next = node
                        currentNode = node
                        #print(currentNode.val)
            
            #v = currentNode.val
        #print('end flatten')
        return head
                    
                    
                
                
        
        
        
def main():
    node1 = Node(1)  
    node2 = Node(2)
    node3 = Node(3)  
    node4 = Node(4)
    node5 = Node(5)  
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)  
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)  
    node12 = Node(12)
    
    '''
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    
    node2.child = node4
    node4.next = node5
    node5.prev = node4
    
    node5.child = node6
    
    
    flatten = Solution().flatten(node1)
    
    while flatten:
        print (flatten.val)
        flatten = flatten.next
    '''    
    
    
    
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2    
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5
    
    node3.child = node7
    node7.next = node8
    node8.prev = node7
    node8.next = node9
    node9.prev = node8
    node9.next = node10
    node10.prev = node9
    
    node8.child = node11
    node11.next = node12
    node12.prev = node11
    
    
    flatten = Solution().flatten(node1)
    
    while flatten:
        print (flatten.val)
        flatten = flatten.next
        
    '''    
    node1.child = node2
    node2.child = node3
    node3.child = node4
    node4.child = node5
    node5.child = node6
    node6.child = node7
    node7.child = node8
    node8.child = node9
    node9.child = node10
    node10.child = node11
    node11.child = node12
    
    
    flatten = Solution().flatten(node1)
    
    while flatten:
        print (flatten.val)
        flatten = flatten.next
    '''  
if __name__ == '__main__':
    main()