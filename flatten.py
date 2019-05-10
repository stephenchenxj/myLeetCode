#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:08:03 2019

@author: dev
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
        currentNode = head
        node2connect = []
        
        # exist condition: no more next node or no more node to connect
        while currentNode.next or node2connect !=[]: 
            #print(currentNode.val)
            if currentNode.child: # got child
                if currentNode.next: # and it got next
                    node2connect.append( currentNode.next )
                    #print(currentNode.next.val)
                child = currentNode.child
                currentNode.next = child
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
                        node.pre = currentNode
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
      
if __name__ == '__main__':
    main()