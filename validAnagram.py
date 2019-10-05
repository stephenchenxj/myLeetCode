# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 02:14:29 2019

@author: stephen.chen
"""

'''
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for c in s:
            if c in t:
                t = t.replace(c,'',1)
            else:
                return False
        if t =='':
            return True
        return False
        
def main():
    mySolution = Solution()
    print(mySolution.isAnagram('anagram',  "nagaram" ))
    
if __name__== '__main__':
    main()