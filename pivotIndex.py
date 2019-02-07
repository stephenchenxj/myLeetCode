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
        