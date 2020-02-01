#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:06:26 2019

@author: dev

14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
Accepted
628,935
Submissions
1,816,836
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        notMatch = 0
        for i in range(len(strs[0])):
            currentCh = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]):
                    notMatch = 1
                    break
                    
                if strs[j][i] != currentCh:
                    notMatch = 1
                    break
            if notMatch == 1:
                return strs[0][0:i]
         
        return strs[0]
                    
            
        


def main():
    strs = ["aa","a"]
    print(Solution().longestCommonPrefix(strs))
    
if __name__ == '__main__':
    main()