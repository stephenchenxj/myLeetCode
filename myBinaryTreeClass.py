# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:00:42 2019

@author: stephen.chen
107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyBinaryTreeClass(object):
    def getValuesBreadthFirst(self, root):
        if not root:
            return
        nodes = [root]
        vals = []
        while nodes:
            currentNode = nodes.pop(0)
            vals.append(currentNode.val)
            if currentNode.left:
                nodes.append(currentNode.left)
            if currentNode.right:
                nodes.append(currentNode.right)
        return vals
    
    def getValuesBreadthFirstWithNone(self, root):
        if not root:
            return
        nodes = [root]
        vals = []
        proceed = 1
        while proceed:
            currentNode = nodes.pop(0)
            
            if currentNode == None:
                vals.append(None)
                nodes.append(None)
                nodes.append(None)
            else:
                proceed -= 1
                vals.append(currentNode.val)
                if currentNode.left:
                    proceed += 1
                if currentNode.right:
                    proceed += 1
                nodes.append(currentNode.left)
                nodes.append(currentNode.right)
        return vals
            
            
        
    
    
    def listToBinaryTree(self, values):
        """
        :type: List[List[int]]
        :rtype root: TreeNode
        """
        if len(values) == 0:
            return None
        head = TreeNode(values[0])
        currentLevelNodes = []
        currentLevelNodes.append(head)
        i = 1 # point to values[1] now
        
        nextLevelNodes = []
        while i < len(values):
            currentNode = currentLevelNodes.pop(0)
            if currentNode == None:
                i += 2
            else:    
                if values[i] != None:
                    currentNode.left = TreeNode(values[i])
                else:
                    currentNode.left = None
                i += 1
                if i >= len(values):
                    break
                if values[i] != None:
                    currentNode.right = TreeNode(values[i])
                else:
                    currentNode.right = None
                i += 1
            
                nextLevelNodes.append(currentNode.left)
                nextLevelNodes.append(currentNode.right)
            
            if currentLevelNodes == []:
                currentLevelNodes = nextLevelNodes[:]
                #print(currentLevelNodes)
                nextLevelNodes = []
                
        return head
            
tree = MyBinaryTreeClass()
root = tree.listToBinaryTree([0,1,None, 3, 4,None, None,None, None, 9, None, None, None, None, None])    
print(root)    

vals = tree.getValuesBreadthFirst(root)
print(vals)

vals = tree.getValuesBreadthFirstWithNone(root)
print(vals)


#lst = [1,2,3,4]
#item = lst.pop(0)
#print(item)
#print(lst)


        
