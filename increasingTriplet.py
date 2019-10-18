# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 05:36:59 2019

@author: stephen.chen

Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

Example 2:

Input: [5,4,3,2,1]
Output: false



"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ''' too slow
        if len(nums)<3:
            return False
        
        length = len(nums)
        
        
        for i in range(1,length-1):
            left = 0
            right = 0
            for j in range(0,i):
                if nums[j]<nums[i]:
                    left = 1
                    break
            for j in range(i+1, length):
                if nums[j]>nums[i]:
                    right = 1
                    break
            if left and right:
                return True
        return False
        '''
        
        length = len(nums)
        if length < 3:
            return False
        
        
        min1 = nums[0]
        min2 = None
        
        for i in range(1,length):
            if nums[i]> min1:
                if min2 == None or min2 > nums[i]:
                    min2 = nums[i]
                if min2 < nums[i]:
                    return True
            elif nums[i] < min1:
                min1 = nums[i]
        return False
            
            
        
    
test = Solution()
input = [5,4,2,3,1,6]
print(test.increasingTriplet(input))
            
        