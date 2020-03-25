#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:15:34 2020

@author: stephenchen


144. Binary Tree Preorder Traversal
Medium

1219

52

Add to List

Share
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        rslt = []
        if not root:
            return rslt
        rslt.append(root.val)
        rslt.extend(self.preorderTraversal(root.left))
        rslt.extend(self.preorderTraversal(root.right))
        
        return rslt
    
    def preorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        rslt = []
        stack = [root]
        
        
        while stack != []:
            node = stack.pop()
            if node:
                rslt.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return rslt
        
        
        
        
        
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

test = Solution()
print(test.preorderTraversal(n1))
print(test.preorderTraversalIterative(n1))
