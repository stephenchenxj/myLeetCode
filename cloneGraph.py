#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:56:36 2019

@author: dev
"""

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return node
        
        nodeMapping = dict()
        nodeStack = [node]
        
        # deep copy of node value
        while nodeStack:
            nodeToClone = nodeStack.pop()
            
            if nodeToClone not in nodeMapping.keys(): # this node is not in Hashmap yet. It has not been visited.
                nodeMapping[nodeToClone] = Node(nodeToClone.val,[])
                #print(nodeToClone.val)
                for neighbor in nodeToClone.neighbors:
                    if neighbor not in nodeMapping.keys(): # this neighbor node is not in Hashmap yet. It has not been visited.
                        nodeStack.append(neighbor)
        
        # deep copy of node neighbors
        nodeStack = [node]
        visitedNodes = {node}
        while nodeStack:
            nodeToLink = nodeStack.pop()
            for neighbor in nodeToLink.neighbors:
                nodeMapping[nodeToLink].neighbors.append(nodeMapping[neighbor]) 
                if neighbor not in visitedNodes:                    
                    visitedNodes.add(neighbor)
                    nodeStack.append(neighbor)
                    
        return nodeMapping[node]
                    
                    
                    
            
                
                
                    
    #basic task first: you got to know how to trasverse the graph
    def trasverseGraph(self, node):
        if not node:
            print( node)
        
        # it does not work. It is an infinite loop if you don't check if the node is visited before
#        nodeStack = {node} 
#        while nodeStack:
#            currentNode = nodeStack.pop()
#            print(currentNode.val)
#            nodeStack.update(currentNode.neighbors)
            
        nodeStack = [node]
        visitedNodes = {node}
        while nodeStack:
            currentNode = nodeStack.pop()
            print(currentNode.val)
            for node in currentNode.neighbors:
                if node not in visitedNodes:
                    nodeStack.append(node)
                    visitedNodes.add(node)    
        
        
        
        

def main():
    node1 = Node(1,[])
    node2 = Node(2,[])
    node3 = Node(3,[])
    node4 = Node(4,[])
    node5 = Node(5,[])
    node6 = Node(6,[])
    node7 = Node(7,[])
    node8 = Node(8,[])
    
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
#    node1.neighbors.append(node5)
#    node1.neighbors.append(node6)
    
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    
    node4.neighbors.append(node3)
    node4.neighbors.append(node1)
#    
#    node5.neighbors.append(node1)
#    node6.neighbors.append(node1)
#    
#    node6.neighbors.append(node2)
#    node2.neighbors.append(node6)
#    
#    node6.neighbors.append(node7)
#    node7.neighbors.append(node6)
#    
#    node7.neighbors.append(node8)
#    node8.neighbors.append(node7)
    
#    solution = Solution()
#    solution.trasverseGraph(node1)
    
    clonedGraph = (Solution().cloneGraph(node1))
    Solution().trasverseGraph(clonedGraph)
    print('original:')
    Solution().trasverseGraph(node1)


if __name__ == '__main__':
    main()
