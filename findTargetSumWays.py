#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:29:54 2019

@author: dev
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = 0
        
        summ = sum(nums)
        print(summ)
        
        # (summ + S) must be even 
        if (summ + S) % 2 != 0:
            return res
        else:
            pSum = (summ + S)/2
            
        print('pSum = %d ' %pSum)
            
        if pSum > summ or pSum < 0:
            return res
        
        for n in nums:
            if n == pSum:
                res += 1
                nums.remove(n)
        
        print(nums)
        return res
    
def main():
    mySolution = Solution()
    print(mySolution.findTargetSumWays([1,1,1],-1))
    
    
if __name__ == '__main__':
    main()