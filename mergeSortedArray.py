# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 04:38:15 2019

@author: stephen.chen

Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]



"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m >= 0 and n > 0:
            if nums1[m-1]> nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                if m > 0:
                    m -= 1
            else:
                nums1[m+n-1]=nums2[n-1]
                if n > 0:
                    n -= 1
                
        
nums1=[2,0]
nums2=[1]        
mySolution = Solution()
mySolution.merge(nums1, 1, nums2, 1)
print (nums1)
        