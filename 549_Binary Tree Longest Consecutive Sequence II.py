#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:01:01 2020

@author: chen

549. Binary Tree Longest Consecutive Sequence II
Medium

535

41

Add to List

Share
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longest_path(root):
            if not root:
                return 0, 0
            inc, dec = 1, 1
            l_inc, l_dec = longest_path(root.left)
            r_inc, r_dec = longest_path(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    inc = max(inc, 1 + l_inc)
                if root.left.val == root.val - 1:
                    dec = max(dec, 1 + l_dec)
            if root.right:
                if root.right.val == root.val + 1:
                    inc = max(inc, 1 + r_inc)
                if root.right.val == root.val - 1:
                    dec = max(dec, 1 + r_dec)
            res[0] = max(res[0], inc + dec - 1)
            return (inc, dec)
        
        res = [0]
        longest_path(root)
        return res[0]
        
