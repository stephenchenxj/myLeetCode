#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:46:43 2019

@author: dev
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
            else:
                if length > maxLen:
                    maxLen = length
                length = 0
                
            if length > maxLen:
                    maxLen = length    
        return maxLen
        
        
        
def main():
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))
    
if __name__ == '__main__':
    main()