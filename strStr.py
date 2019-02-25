#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:07:56 2019

@author: dev
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        
        for i in range(len(haystack)):
            match = 1
            for j in range(len(needle)):
                if i+len(needle) > len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    match = 0
                    break
            if match == 1:
                return i
            
        return -1  
                    
        
        
def main():
    haystack = 'aaaabaa'
    needle = 'baa'
    print(Solution().strStr(haystack, needle))
    
    
if __name__ == '__main__':
    main()