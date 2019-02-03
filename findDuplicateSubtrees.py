#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:40:36 2019

@author: dev
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        self.res = []
        self.dic = {}
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return '#'
        tree = str(root.val) + self.dfs(root.left) + self.dfs(root.right) 
        if tree in self.dic and self.dic[tree] == 1:
            self.res.append(root)
        self.dic[tree] = self.dic.get(tree, 0) + 1
        print(tree)
        return tree
        
        
def main():
    #tree = [1,2,3,4,None,2,4,None,None,4]
    #ret = Solution().findDuplicateSubtrees(tree)
    
    root = TreeNode(1)
    l1 = TreeNode(2)
    r1 = TreeNode(3)
    l2l = TreeNode(4)
    r2l = TreeNode(2)
    r2r = TreeNode(4)
    r2l3 = TreeNode(4)
    
    r2l.left = r2l3
    l1.left = l2l
    r1.left = r2l
    r1.right = r2r
    root.left = l1
    root.right = r1
    
    ret = Solution().findDuplicateSubtrees(root)
    print(ret)
    
if __name__ == '__main__':
    main()

        