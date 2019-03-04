#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:33:32 2019

@author: dev
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newLen = len(nums)
        i = 0
        while i < newLen:
            if nums[i] == val:
                del nums[i]
                newLen -= 1
                i -= 1
            i += 1
                
        #return nums
        return newLen
                
    
def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))
    
if __name__ == '__main__':
    main()