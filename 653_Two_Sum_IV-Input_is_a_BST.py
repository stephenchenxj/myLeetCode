#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:35:43 2020

@author: stephenchen

653. Two Sum IV - Input is a BST
Easy

1219

129

Add to List

Share
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
 

Accepted
124,345
Submissions
228,283


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        # vals = []
        # def preorder(root, vals):
        #     if root:
        #         vals.append(root.val)
        #     if root.left:
        #         preorder(root.left, vals)
        #     if root.right:
        #         preorder(root.right, vals)
            
        # pair = dict()     
        
        # preorder(root, vals)
        
        # for val in vals:
        #     if pair.get(k-val):
        #         return True
        #     else:
        #         pair[val] = True
                
        # print(vals)
        # return False
        
        pair = dict()
        
        def inorder(root):
            rslt = False
            if root.left:
                rslt = inorder(root.left)
                if rslt:
                    return rslt
            if root:
                if pair.get(k-root.val):
                    return True
                else:
                    pair[root.val] = True
            if root.right:
                rslt = inorder(root.right)
                
            return rslt 
         
        return inorder(root)
    
    
            
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)


n1.left = n2
n1.right = n3      

print(Solution().findTarget(n1,4))      
            
    