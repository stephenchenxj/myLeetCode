#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:42:15 2019

@author: dev

66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Accepted
503,211
Submissions
1,201,218
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        
        if n == 0:
            return [1]
        
        #print(n)
        
        #print(digits[0:(n-1)])
        
        if digits[n-1] == 9:
            #print(digits[n-1]) 
            temp = self.plusOne(digits[0:(n-1)])
            temp.append(0)
            return temp
        else:
            digits[n-1] += 1
            #print(digits[n-1]) 
            return digits
            
        
        
        
        
        
def main():
    ret = Solution().plusOne([9,9,8,9])
    print(ret)
    
if __name__ == '__main__':
    main()