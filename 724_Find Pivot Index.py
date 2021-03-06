#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:15:32 2019

@author: dev

724. Find Pivot Index
Easy

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.

 

Note:

    The length of nums will be in the range [0, 10000].
    Each element nums[i] will be an integer in the range [-1000, 1000].

 
Accepted
104,156
Submissions
243,991
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return -1
        
        numSums = [nums[0]]
        
        for i in range(1, len(nums)):
            numSums.append(numSums[i-1] + nums[i])
        
        #print(numSums)
        
        
        
        last = numSums[len(numSums)-1]
        if last == numSums[0]:
            return 0
            
        for i in range(1, len(numSums)):
            if (last - numSums[i])== numSums[i-1]:
                return i
        return -1
    
    
        
        
        
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        
        l = 0
        r = sum(nums)
            
        for pI in range(0,len(nums)):

            l += nums[pI]        
            
            if l==r:
                return pI
            r -= nums[pI]
            
            
        return -1
        

    
    
        
def main():
    nums = [-1,-1,-1,0,1,1]
    nums = [1, 7, 3, 6, 5, 6]
    
    ret = Solution().pivotIndex(nums)
    print('Result =')
    print(ret)
    
    
    for index, num in enumerate(nums):
        print(index)
        print(num)
            
    
        
        
if __name__ == '__main__':
    main()
        