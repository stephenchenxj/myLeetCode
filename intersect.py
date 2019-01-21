#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:48:25 2019

@author: dev
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
