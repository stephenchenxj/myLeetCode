#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:48:25 2019

@author: dev

350. Intersection of Two Arrays II
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Accepted
282,020
Submissions
562,065
"""

class Solution(object):
    def __init__(self):
        self.hashmap = {}
        self.hashmap2 = {}
    def intersect(self, nums1, nums2):
        
        for n in nums1:
            if n not in self.hashmap:
                self.hashmap[n] = 1
            else:
                self.hashmap[n] += 1
        print(self.hashmap)    
        
        for n in nums2:
            if n not in self.hashmap2:
                self.hashmap2[n] = 1
            else:
                self.hashmap2[n] += 1
        print(self.hashmap2)   
        
        result = []
        if len(nums1) <= len(nums2):
            for n in self.hashmap:
                if n in self.hashmap2:
                    count = min(self.hashmap[n],self.hashmap2[n])
                    for i in range(count):
                        result.append(n)           
        else:
            for n in self.hashmap2:
                if n in self.hashmap:
                    count = min(self.hashmap[n],self.hashmap2[n])
                    for i in range(count):
                        result.append(n)    
        
        return result
    
def main():
    ret = Solution().intersect([4,9,4,5,4,8,9], [9,4,9,8,4])
    print(ret)
    
if __name__ == '__main__':
    main()
