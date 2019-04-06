#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:06:26 2019

@author: dev
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