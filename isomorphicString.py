#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:56:26 2019

@author: dev
"""

class Solution(object):
    def __init__(self):
        self.hashmapA = {}
        self.hashmapB = {}
        
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        index = 0
        for c in s:
            if c not in self.hashmapA:
                self.hashmapA[c] = [index]
            else:
                self.hashmapA[c].append(index)                
            index += 1            
         
        index = 0
        for c in t:
            if c not in self.hashmapB:
                self.hashmapB[c] = [index]
            else:
                self.hashmapB[c].append(index)                
            index += 1   
            

        
        listA = []
        for kA in self.hashmapA:
            listA.append(self.hashmapA[kA]) 
        listB = []
        for kB in self.hashmapB:
            listB.append(self.hashmapB[kB]) 
        
        print (listA)
        print (listB)

#        if listA == listB:
#            return True
#        else:            
#            return False
        
        for index in listA:
            if index not in listB:
                return False
        return True
            
        

def main():
    
    


    import sys
    
    ret = Solution().isIsomorphic('egg', 'add')
    out = (ret)
    print (out)
    
    
    ret = Solution().isIsomorphic('ab', 'aa')
    out = (ret)
    print (out)
    
    
if __name__ == '__main__':
    main()