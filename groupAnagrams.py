#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:52:17 2019

@author: dev
"""

class Solution(object):
    def __init__(self):
        self.hashmap = {}
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        for eachStr in strs:
            key = self.myhash(eachStr)
            
            if key not in self.hashmap:
                self.hashmap[key] = eachStr
            else:
                self.hashmap[key].append(eachStr)
        print(self.hashmap)
        
    def myhash(self, st):
        hm = {}
        for c in st:
            if c not in hm:
                hm[c]= 1
            else:
                hm[c] += 1
        result = []
        for i in hm:
            result.append(i)
            result.append(str(hm[i]))
        print(result)
        result = ''.join(result)
        return result
    
def main():
    #ret = Solution().groupAnagrams(['eat','tea', 'tan', 'ate', 'nat','bat'])
    #print(ret)
    
    ret = Solution().myhash('aaab')
    print(ret)
    
    ret = Solution().myhash('baaa')
    print(ret)
    
if __name__ == '__main__':
    main()
