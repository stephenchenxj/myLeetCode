# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:00:42 2019

@author: stephen.chen
107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""
import myBinaryTreeClass



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        rst = []
        if not root:
            return rst
        vals = []
        nodes = [root]
        nextLevelNodes = []
        while nodes or nextLevelNodes:
            node = nodes.pop(0)
            vals.append(node.val)
            if node.left:
                nextLevelNodes.append(node.left)
            if node.right:
                nextLevelNodes.append(node.right)
            if nodes == []:
                rst.append(vals)
                vals = []
                nodes = nextLevelNodes[:]
                nextLevelNodes = []
                
        rst.reverse()        
        return rst
            
        

tree = myBinaryTreeClass.MyBinaryTreeClass()
root = tree.listToBinaryTree([3,9,20,None,None,15,7])
values = tree.getValuesBreadthFirst(root)
print(values)
values = tree.getValuesBreadthFirstWithNone(root)
print(values)

test = Solution()
print (test.levelOrderBottom(root))
