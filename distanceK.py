# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:32:51 2019

@author: stephen.chen

863. All Nodes Distance K in Binary Tree
Medium

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

 

Note:

    The given tree is non-empty.
    Each node in the tree has unique values 0 <= node.val <= 500.
    The target node is a node in the tree.
    0 <= K <= 1000.

Accepted
42,106
Submissions
82,511
"""


import myBinaryTreeClass

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        #target is a TreeNode, not the target value. So no need to search for the node with that value
        
        parents = dict()        
        def findParent(node, parent):
            if node:
                parents[node.val] = parent
                findParent(node.left, node)
                findParent(node.right, node)
                
        findParent(root, None)
        
        ans = []
        visited = dict()
        def findK(root, K):
            if not root:
                return
            if visited.get(root):
                return            
            if K == 0:
                ans.append(root.val)                
            else:
                visited[root] = True
                findK(root.left, K-1)
                findK(root.right, K-1)
                b = (root.val)
                if parents.get(root.val): #if it doesn't have a parent in the dict, it means 
                    #this node is below the target. No need to search upwards
                    findK(parents[root.val],K-1)
        findK(target, K)
        return ans
            
        
    

