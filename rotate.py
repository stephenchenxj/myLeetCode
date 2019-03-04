#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:29:50 2019

@author: dev
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result = []
        for i in range(len(nums)):
            j = i - k
            if j < 0:
                j += len(nums)
            result.append(nums[j])
            
        for i in range(len(nums)):
            nums[i] = result[i]
        
        
        
def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    
    print(Solution().rotate(nums, k))
    print(nums)
    
if __name__ == '__main__':
    main()