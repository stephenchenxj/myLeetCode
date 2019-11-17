# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 04:12:53 2019

@author: stephen.chen
559. Maximum Depth of N-ary Tree
Easy

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Representation of 3-ary tree.

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth = 0
        if not root:
            return depth        
        currentLevelNodes = [root]
        nextLevelNodes = []
        while currentLevelNodes:
            node = currentLevelNodes.pop()
            if node.children:
                nextLevelNodes.extend(node.children)
            if not currentLevelNodes:
                depth += 1
                currentLevelNodes = nextLevelNodes[:]
                nextLevelNodes = []
        return depth
        

