#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:16:15 2019

@author: dev
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        m = (max(nums))
        
        index = -1
        i = 0
        for n in nums:
            if n != m:
                if 2*n > m:
                    return -1
            else:
                index = i
            i += 1
        
        
        return index
        
        
        
def main():
    ret = Solution().dominantIndex([3,6,1,0])
    print(ret)
    
if __name__ == '__main__':
    main()