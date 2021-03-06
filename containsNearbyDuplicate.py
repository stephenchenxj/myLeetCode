#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 21:40:06 2019

@author: dev

219. Contains Duplicate II
Easy

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Accepted
237,709
Submissions
648,627

"""

class Solution(object):
    def __init__(self):
        self.hashmap = {}
        
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        index = 0
        gotRepeat = False
        for n in nums:
            if n not in self.hashmap:
                self.hashmap[n] = [index]
            else:
                self.hashmap[n].append(index)
                gotRepeat = True
            index += 1    
        #print(self.hashmap)
        
        '''
        maxDis = 0
        for key in self.hashmap:
            if len(self.hashmap[key] )> 1:
                localMax = self.hashmap[key][len(self.hashmap[key] )-1] - self.hashmap[key][0]
                if maxDis < localMax:
                    maxDis = localMax
        if maxDis > k:
            return False
        else:
            return True
        '''
        
        if gotRepeat == False: 
            return False
        
        minDis = len(nums)
        
        for key in self.hashmap:
            if len(self.hashmap[key] )> 1:
                localMin = len(nums)
                for i in range(len(self.hashmap[key])-1):
                    if localMin > self.hashmap[key][i+1] - self.hashmap[key][i]:
                        localMin = self.hashmap[key][i+1] - self.hashmap[key][i]
                print(localMin)
                if minDis > localMin:
                    minDis = localMin
                
                    
        if minDis > k:
            return False
        else:
            return True
        
    
def main():
    ret = Solution().containsNearbyDuplicate([1,2], 2)
    print(ret)
    
if __name__ == '__main__':
    main()
        