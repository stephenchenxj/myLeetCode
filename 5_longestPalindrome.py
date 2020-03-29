# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 05:35:41 2019

@author: stephen.chen

5. Longest Palindromic Substring
Medium

5805

485

Add to List

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
Accepted
836,155
Submissions
2,896,265


"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in range(len(s)):
            l = i
            r = i
            while l >=0 and r < len(s) and self.isPalindrome(s,l,r):
                if r-l+1 > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
                
            l = i
            r = i+1
            while l >=0 and r < len(s) and self.isPalindrome(s,l,r):
                if r-l+1 > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
                
        return result    
            
    
    def isPalindrome(self, s, l, r):
        if s[l]==s[r]:
            return True
        else:
            return False
        
            
test = Solution()
s = 'babad'

print(test.longestPalindrome(s))

t = s[0:2]
print(t)
        
        
    