#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:46:43 2019

@author: dev

485. Max Consecutive Ones
Easy

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

Accepted
168,598
Submissions
300,857

"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
            else:
                if length > maxLen:
                    maxLen = length
                length = 0
                
            if length > maxLen:
                    maxLen = length    
        return maxLen
        
        
        
def main():
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))
    
if __name__ == '__main__':
    main()