# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:41:52 2019

@author: stephen.chen

515. Find Largest Value in Each Tree Row
Medium

You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

Accepted
75,698
Submissions
128,632
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []        
        currentLevel = [root]
        nextLevel = []
        ans = []
        maxVal = None
        while currentLevel:
            node = currentLevel.pop(0)
            if maxVal == None or maxVal < node.val:
                maxVal = node.val
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if not currentLevel:
                ans.append(maxVal)
                maxVal = None
                currentLevel = nextLevel[:]
                nextLevel = []
        return ans
    
     