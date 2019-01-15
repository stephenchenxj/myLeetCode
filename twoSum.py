#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:14:21 2019

@author: dev
"""


class Solution(object):
    def __init__(self):
        self.hashmap = {}
        
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        for n in nums:
            #print (n)
            
            if (target - n ) in self.hashmap:
                return [ self.hashmap[target - n ], index]
            
            self.hashmap[n] = index
            index += 1
            
            
            
        #print (self.hashmap)


def main():

    import sys
    
    
    ret = Solution().twoSum([3,2,4], 6)
    out = (ret)
    print (out)
    
    
if __name__ == '__main__':
    main()