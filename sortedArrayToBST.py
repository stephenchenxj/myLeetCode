# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 02:50:35 2019

@author: stephen.chen

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5




"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length ==0:
            return None
        i = int(length/2)
        head = TreeNode(nums[i])
        
        head.left = self.sortedArrayToBST(nums[:i])
        head.right = self.sortedArrayToBST(nums[i+1:])
        return head
    

nums = [1,2,3,4,5,6,7,8]     
length = len(nums)
i = int(length/2)
print (nums[i] )
print(nums[:i-1])
print(nums[:i])
print(nums[i+1:])
        