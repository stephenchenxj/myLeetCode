# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 02:24:04 2019

@author: stephen.chen

429. N-ary Tree Level Order Traversal
Medium

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

 

Constraints:

    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]


"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        currentLevel = [root]
        nextLevel = []
        ans = []
        vals = []
        while currentLevel:
            node = currentLevel.pop(0)
            if node:
                vals.append(node.val)
                if node.children:
                    nextLevel.extend(node.children)
            
            if not currentLevel:
                currentLevel = nextLevel[:]
                nextLevel = []                
                ans.append(vals)
                vals = []
                
        return ans
    
n1 =  Node(1)  
n2 =  Node(2)
n3 =  Node(3)
n4 =  Node(4)
n5 =  Node(5)
n6 =  Node(6)
n7 =  Node(7)
n1.children = [n3,n2,n4]
n3.children = [n5,n6]
test = Solution()
print(test.levelOrder(n1))
 
