#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:55:33 2020

@author: chen


42. Trapping Rain Water
Hard

6134

107

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Accepted
460,966
Submissions
972,575

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        size = len(height)
        if size <= 1:
            return 0
        l = 0
        r = size-1
        
        l_max = height[l]
        r_max = height[r]
        water = 0
        while l < r:
            if l_max <= r_max:
                l += 1
                water += max(min(l_max, r_max) - height[l],0)
                l_max = max(l_max, height[l])
            else:
                r -= 1
                water += max(min(l_max, r_max) - height[r],0)
                r_max = max(r_max, height[r])
                
        return water
    
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))