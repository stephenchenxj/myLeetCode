# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:48:34 2019

@author: stephen.chen

Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?


"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        l = [1]*len(nums)
        
        for i,n in enumerate(nums):
            for j in range(i):
                if n > nums[j]:
                    l[i] = max(l[i], l[j]+1)
                    
        return max(l)
    
test = Solution()
print(test.lengthOfLIS([10,9,2,5,3,7,101,18]))
            
