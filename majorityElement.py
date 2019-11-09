# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 01:05:51 2019

@author: stephen.chen

Majority Element

Given an array of size n, find the majority element. The majority element is 
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        threshold = len(nums)//2
        myDict = dict()
        for n in nums:
            if myDict.get(n) != None:
                myDict[n] += 1
            else:
                myDict[n] = 1
            
            if myDict[n]> threshold:
                return n
    
test = Solution()
print(test.majorityElement([1,2,3,4,4,3,2,1,4,4,4,4,4,4,4,4]))
            
