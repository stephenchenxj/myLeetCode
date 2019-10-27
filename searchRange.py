# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 04:07:35 2019

@author: stephen.chen

Search for a Range

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        length = len(nums)
        
        if length == 0:
            return result
        if target < nums[0] or target > nums[length-1]:
            return result
        
        def leftMost(nums, target, l, m, r):
            if r-l == 1:
                if nums[l]<target and nums[r]==target:
                    return r
                elif nums[l]<target and nums[r]>target:
                    return -1
                elif nums[r] < target:
                    return -1
            if l == m-1 and nums[m] == target and nums[l] < target:
                return m
            if m == 0 and nums[m] == target:
                return 0
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m            
            return leftMost(nums, target, l, int((l+r)/2), r)
        

        def rightMost(nums, target, l, m, r):
            if r-l == 1:
                if nums[l]==target and nums[r]>target:
                    return l                
            if r <= m+1 and nums[m] == target and nums[r] > target:
                return m
            if r >= len(nums)-1 and nums[r] == target:
                return r    
            if nums[m] > target:
                r = m      
            if nums[m] == target:
                l = m
            if nums[r] == target:
                r = int((length-1 + r)/2)+1
            return rightMost(nums, target, l, int((l+r)/2), r)

        
            
        left = leftMost(nums, target, 0, int(length/2), length-1)
        print (left)
        if left == -1:
            return [-1,-1]
        right = rightMost(nums, target, left, int((length-1 + left)/2), length-1)
        return [left, right]
        

        
        
        
nums = [0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10]
target =1
test = Solution()
print(test.searchRange(nums, target))