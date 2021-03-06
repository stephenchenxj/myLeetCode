#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:56:26 2019

@author: dev

205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
Accepted
258,065
Submissions
663,196
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
        
        
        
#        if not s or not t:
 #           return True
        
        
        dic = {}
        dic2 = {}
        count = 0
        count2 = 0
        
        
        for a,b in zip(s,t):
            
            print(a)
            print(b)
            
            if not a in dic:
                dic[a] = count
                count += 1
            if not b in dic2:
                dic2[b] = count2
                count2 +=1

        for a,b in zip(s,t):
            if not dic[a] == dic2[b]:
                return False
        return True


        
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
    
    s = 'abcdefgh'
    t = 'xyzstu'
    u = '123456'
    
    for a,b in zip(s,t):
            
            print(a)
            print(b)


    for a,b,c in zip(s,t,u):
            
            print(a)
            print(b)
            print(c)

    import sys
    
    ret = Solution().isIsomorphic('egg', 'add')
    out = (ret)
    print (out)
    
    
    ret = Solution().isIsomorphic('ab', 'aa')
    out = (ret)
    print (out)
    
    
if __name__ == '__main__':
    main()