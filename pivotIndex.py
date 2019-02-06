#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:15:32 2019

@author: dev
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        
        for pI in range(0,len(nums)):
            l = 0
            r = 0
            for i in range(pI):
                l += nums[i]
            for i in range(pI+1,len(nums)):
                r += nums[i]            
            
            if l==r:
                return pI
            
        return -1
        
def main():
    nums = [-1,-1,-1,0,1,1]
    ret = Solution().pivotIndex(nums)
    print('Result =')
    print(ret)
    
        
        
if __name__ == '__main__':
    main()
        