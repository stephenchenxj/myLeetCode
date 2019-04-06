#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:27:08 2019

@author: dev
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        if sum(nums) < s:
            return 0        
        minLen = len(nums)        
        for i in range(len(nums)):
            length = 1
            summary = nums[i]            
            if summary >= s:
                if minLen > length:
                    #minLen = 1
                    return 1                        
            for j in range(i+1, len(nums)):
                summary += nums[j]
                length += 1
                if summary >= s:
                    if minLen > length:
                        minLen = length                
        return minLen       
        '''
        if nums == [] or nums == None:
            return 0
        if len(nums) == 1 :
            if nums[0] < s:
                return 0
            else: 
                return 1
            
        lP = 0
        rP = 0
        minLen = 0
        summ = nums[lP]
        while rP < len(nums):
            if summ >= s:
                length = rP-lP +1
                if length < minLen or minLen == 0:
                    minLen = length
                summ -= nums[lP]                
                lP += 1
                if lP > rP:
                    break
            if summ < s:
                rP += 1
                if rP >=len(nums):
                    break
                summ += nums[rP]   
        
        return minLen
        
        
def main():
    s = 3
    nums =  [1,1]
    
    
    print(Solution().minSubArrayLen(s, nums))
    
if __name__ == '__main__':
    main()