# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 03:46:02 2019

@author: stephen.chen
Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing 
from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant 
extra space complexity?

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
        
        n = len(nums) 
        
        total = sum(nums)
        total_no_missing = (n+1)*n/2
        
        return total_no_missing - total
        
        '''
        
        for i in range(n ):
            if i not in nums:
                return i
        return n
        '''
            
test = Solution()
print(test.missingNumber([0,1,2,3,4,5,7,8]))     