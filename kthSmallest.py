# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:21:49 2019

@author: stephen.chen
Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def transverse(self, root, vals):
        
        if root:
            if root.left:
                self.transverse(root.left, vals )     
                
            #if root.val: # wrong. if root.val = 0, it will not be append. got missing val
            #    vals.append(root.val)            
            vals.append(root.val)
            if root.right:
                self.transverse(root.right, vals )
        
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        listV = []
        count = 0
        
        self.transverse(root, listV)
        return listV[k-1]


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node5.left = node3
node5.right = node6
node3.left = node2
node3.right = node4
node2.left = node1

test = Solution()
vals = []
test.transverse(node5, vals)
print(vals)
print(test.kthSmallest(node5, 3))