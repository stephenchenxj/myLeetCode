#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:40:52 2019

@author: dev

94. Binary Tree Inorder Traversal
Medium

2557

111

Add to List

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

Accepted
644,149
Submissions
1,054,223

"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rslt = []
        if not root:
            return rslt
        rslt.extend(self.inorderTraversal(root.left))
        rslt.append(root.val)
        rslt.extend(self.inorderTraversal(root.right))
        return rslt
    
    def inorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rslt = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            rslt.append(root.val)
            root = root.right
        return rslt
        

        
    
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

test = Solution()
print(test.inorderTraversal(n1))
print(test.inorderTraversalIterative(n1))
    