#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:16:13 2019

@author: dev
"""

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        
        result = []
        hist = {}
        frequences = []
        for n in nums:
            if n in hist:
                hist[n] += 1
            else:
                hist[n] = 1
        #print(hist)
        
        frequences =(sorted(hist.values()))
        #print(frequences)
        
        for n, f in hist.items():
            if f >= frequences[len(frequences)-k]:
                result.append(n)
        
            
        return result
        
    

                
        
        
        
        
        
def main():
    ret = Solution().topKFrequent([-1,-1], 1)
    print(ret)
    

                
if __name__ == '__main__':
    main()
        