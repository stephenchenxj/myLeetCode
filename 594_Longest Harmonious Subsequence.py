#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:35:08 2020

@author: chen

594. Longest Harmonious Subsequence
Easy

579

77

Add to List

Share
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 

Note: The length of the input array will not exceed 20,000.

Accepted
50,507
Submissions
110,259

"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        ht = dict()
        for n in nums:
            ht[n] = ht.get(n,0) + 1
        keys = sorted(ht)
        for i in range(len(keys)-1):
            if keys[i+1]-keys[i] == 1:
                if maximum < ht[keys[i+1]] + ht[keys[i]]:
                    maximum = ht[keys[i+1]] + ht[keys[i]]
            
        return maximum
        


