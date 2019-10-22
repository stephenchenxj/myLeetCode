# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:44:11 2019

@author: stephen.chen

Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n <= 1:
            return [nums]
        
        rst = [[nums[0]]]
        
        for i in range(1,n):
            temp = []
            for j in range(len(rst)): # retrieve each row in rst
                temp.extend( self.insert(rst[j], nums[i]))
            rst = temp
        return rst
        
        
        
    def insert(self, array, n):
        length = len(array)
        after_insert = []
        for i in range(length+1):
            temp = array[0:i]
            temp.append(n)
            temp.extend(array[i:length])
            after_insert.append(temp)
        return after_insert
    
test = Solution()
print(test.insert([1], 4))
print(test.permute([1,2,3]))
        

       
        