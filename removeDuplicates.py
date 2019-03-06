#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:33:32 2019

@author: dev
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        appearedN = nums[0]
        res = 1
        for n in nums:
            if n != appearedN:
                nums[res] = n
                res += 1
                appearedN = n
        print(nums)        
        return res
            
                
    
def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
    
if __name__ == '__main__':
    main()