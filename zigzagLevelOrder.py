# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 04:09:21 2019

@author: stephen.chen

 Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return None
        result = []
        left2right = True
        nodes = [root]
        while nodes != []:
            nextLevelNodes = []
            values = []
            
            for node in nodes:   
                values.append(node.val)
                if not left2right:                    
                    if node.right:
                        nextLevelNodes.insert(0,node.right)
                    if node.left:
                        nextLevelNodes.insert(0,node.left)
                else:
                    if node.left:
                        nextLevelNodes.insert(0,node.left)
                    if node.right:
                        nextLevelNodes.insert(0,node.right)
            result.append(values)  
#            if not left2right:
#                nodes.reverse()
            nodes = nextLevelNodes
            
            left2right = not left2right
            
        return result

test = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

print (test.zigzagLevelOrder(node1))
            
node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5


print (test.zigzagLevelOrder(node1))





