# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 03:58:38 2019

@author: stephen.chen
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

"""

import myBinaryTreeClass

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root == None:
            return depth
        currentLevelNodes = [root]
        nextLevelNodes = []
        depth = 1
        while currentLevelNodes or nextLevelNodes:
            node = currentLevelNodes.pop(0)
            if node.left == None and node.right == None:
                return depth
            if node.left:
                nextLevelNodes.append(node.left)
            if node.right:
                nextLevelNodes.append(node.right)
            if currentLevelNodes == []:
                depth += 1
                currentLevelNodes = nextLevelNodes[:]
                nextLevelNodes = []
        return depth
            
                
                
        
        
        
tree = myBinaryTreeClass.MyBinaryTreeClass()
root = tree.listToBinaryTree([3,9,20,None,None,15,7])

test = Solution()
print(test.minDepth(root))