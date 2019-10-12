# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:18:44 2019

@author: stephen.chen

Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return None
        history_max_sum = nums[0]
        pre_max_sum = nums[0]
        for n in nums[1:]:
            pre_max_sum = max(n, n+pre_max_sum)
            history_max_sum = max(pre_max_sum, history_max_sum)
            
        return history_max_sum
            
        