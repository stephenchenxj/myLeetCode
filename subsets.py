# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 05:52:52 2019

@author: stephen.chen


Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.rst = []
        def dfs(nums, temp, index):
            self.rst.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i+1)
                temp.pop()
            
        dfs( nums, [], 0)
        return self.rst
    

    
        
            
test = Solution()
print(test.subsets([1,2,3]))




            

