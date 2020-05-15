#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:19:17 2020

@author: chen

259. 3Sum Smaller
Medium

527

48

Add to List

Share
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?

Accepted
63,147
Submissions
134,766
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n*n) time
        count = 0
        nums.sort()
        for i in xrange(len(nums)):
            j, k = i+1, len(nums)-1
            if 3*nums[i] >= target:
                return count
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                    # (i,j,j+1) all work, totally (k-j) triplets
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count


