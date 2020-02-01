#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:33:32 2019

@author: dev

283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        zero = 0
        index = 0
        for n in nums:
            if n != zero:
                nums[index] = n
                index += 1                
                
                
        for i in range(index, len(nums)):
            nums[i] = 0
            
                
    
def main():
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))
    print(nums)
    
if __name__ == '__main__':
    main()