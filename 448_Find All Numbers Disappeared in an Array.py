#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:36:06 2020

@author: chen

448. Find All Numbers Disappeared in an Array
Easy

2448

223

Add to List

Share
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        ht = dict()
        for n in nums:
            ht[n] = True
        for i in range(1,len(nums)+1):
            if not ht.get(i):
                ans.append(i)
        return ans
    
    def findDisappearedNumbersO_1_space(self, nums):
        ans = []
        for n in nums:
            nums[abs(n)-1] = -1*abs(nums[abs(n)-1])
        
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
                
        return ans
                
    
    
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))

print(Solution().findDisappearedNumbersO_1_space(nums))