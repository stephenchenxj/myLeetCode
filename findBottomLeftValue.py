# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 04:28:13 2019

@author: stephen.chen
513. Find Bottom Left Tree Value
Medium

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL. 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = None
        currentLevel = [root]
        nextLevel = []
        
        while currentLevel:
            node = currentLevel.pop(0)
            if ans == None:
                ans = node.val
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if not currentLevel:
                if not nextLevel:
                    return ans
                currentLevel = nextLevel[:]
                nextLevel = []
                ans = None
                
        
        

