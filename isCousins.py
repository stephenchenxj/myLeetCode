# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 01:30:30 2019

@author: stephen.chen
993. Cousins in Binary Tree
Easy

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

 

Note:

    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        if not root:
            return False
        
        nodes = [root]
        nextLevelNodes = []
        target = dict()
        while nodes:
            node = nodes.pop()
            if node.left:
                nextLevelNodes.append(node.left)
                if node.left.val == x or node.left.val == y:
                    target[node.left.val] = node
            if node.right: 
                nextLevelNodes.append(node.right)
                if node.right.val == x or node.right.val == y:
                    target[node.right.val] = node
            if not nodes:
                nodes = nextLevelNodes[:]
                nextLevelNodes = []
                if target.get(x) or target.get(y):
                    break
        if target.get(x) and target.get(y): # find x and y in the same level
            if target[x] != target[y]: # they have different parents
                return True
        return False
    
    
    '''
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]
        '''
                
            
        
        
