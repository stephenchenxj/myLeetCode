# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:35:35 2019

@author: stephen.chen


3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l_index = i+1
            r_index = len(nums)-1
            while l_index < r_index:
                if nums[i] + nums[l_index] + nums[r_index] == 0:
                    triplet = [nums[i], nums[l_index], nums[r_index]]
                    result.append(triplet)
                    while l_index < r_index and nums[l_index] == nums[l_index+1]:
                        l_index += 1
                    while l_index < r_index and nums[r_index] == nums[r_index -1]:
                        r_index -= 1
                    l_index += 1
                    r_index -= 1
                elif nums[i] + nums[l_index] + nums[r_index] < 0:
                    l_index += 1
                else:
                    r_index -= 1
                
        return result
        
nums = [-1, 0, 1, 2, -1, -4]
test = Solution()
print(test.threeSum(nums))
        