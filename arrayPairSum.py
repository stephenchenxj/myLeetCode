#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:51:55 2019

@author: dev
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        print(nums)
        
        result = 0
        i = 0
        while i < (len(nums)):
            result += nums[i]            
            i += 2
            
        return result
        
        
        
def main():
    nums = [1,4,3,2]
    
    print(Solution().arrayPairSum(nums))
    

if __name__ == '__main__':
    main()