#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:40:52 2019

@author: dev
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        if not root :
            return None
        
        left = self.inorderTraversal(root.left)
        if left:
            rst.extend(left)
        rst.extend([root.val])
        
        right = self.inorderTraversal(root.right)
        if right:
            rst.extend(right)
        
        return rst
        