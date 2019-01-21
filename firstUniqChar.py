#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:45:37 2019

@author: dev
"""

class Solution(object):
    def __init__(self):
        self.hashmap = {}
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        for c in s:
            if c not in self.hashmap:
                self.hashmap[c]=index
            else:
                self.hashmap[c] = -1
            index += 1
        
        for c in s:
            if self.hashmap[c] > -1:
                return self.hashmap[c]            
        return -1
                
        
def main():
    ret = Solution().firstUniqChar('ffiirrstt')
    print (ret)
    
if __name__ == '__main__':
    main()
    