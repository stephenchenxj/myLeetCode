#!//usr//bin//env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:43:05 2020

@author: chen

34. Find First and Last Position of Element in Sorted Array
Medium

2935

133

Add to List

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Accepted
457,322
Submissions
1,290,620


"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(nums) - 1
        
        loc = -1
        while l <= r:
            c = int((l+r)//2)
            if nums[c] > target:
                r = c -1
            elif nums[c] < target:
                l = c + 1
            else:
                loc = c
                break
        print(loc)        
        if loc == -1: #could not find target in nums
            return [-1, -1]
        
        left = -1
        l= 0
        r = loc
        if nums[l] == target:
            left = 0
        else:
            while l < r :
                c = int((l+r)//2)
                if nums[c] < target and nums[c+1] == target:
                    left = c + 1
                    break
                elif nums[c] < target and nums[c+1] < target:
                    l = c + 1
                elif nums[c] == target:
                    r = c
        right = -1        
        l= loc
        r = len(nums) - 1
        if nums[r] == target:
            return [left, r]
        
        while l < r :
            c = int((l+r)//2)
            if nums[c] == target and nums[c+1] > target:
                right = c 
                break
            elif nums[c] == target and nums[c+1] == target:
                l = c + 1
            elif nums[c] > target and nums[c+1] > target:
                r = c
        return[left, right]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ans = [-1,-1]
        
        l = 0
        r = len(nums)-1
        loc = -1
        while l <= r:
            if nums[(l+r)//2] < target:
                l = (l+r)//2 +1
            elif nums[(l+r)//2] > target:
                r = (l+r)//2 -1
            else: # found target
                loc = (l+r)//2
                break
                
        if loc == -1: # no target
            return ans
        
        l = 0
        loc_l = loc
        while l < loc:
            if nums[(l+loc)//2] < target and nums[(l+loc)//2 + 1]  >= target:
                loc_l = (l+loc)//2 + 1
                break
            elif nums[(l+loc)//2] == target:
                loc = (l+loc)//2
                loc_l = loc
            elif nums[(l+loc)//2] < target and nums[(l+loc)//2 + 1]  < target:
                l = (l+loc)//2 + 1
        
        loc_r = loc
        while r > loc:
            if nums[(r+loc)//2] == target and nums[(r+loc)//2 + 1]  > target:
                loc_r = (r+loc)//2 
                break
            elif nums[(r+loc)//2] > target:
                r = (r+loc)//2 - 1
            elif nums[(r+loc)//2] == target and nums[(r+loc)//2 + 1]  == target:
                loc = (r+loc)//2 + 1
                loc_r = loc
                     
        ans= [loc_l, loc_r]
        return ans
    
    
nums = [1,1,2]
target = 1

print(Solution().searchRange(nums, target))