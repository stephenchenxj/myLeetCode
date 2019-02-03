#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:25:19 2019

@author: dev
"""

class Solution(object):
    def lengthOfLongestSubstring_slow(self, s):
        """
        :type s: str
        :rtype: int
        """        
        result = 0        
        if len(s) == 1:
            return 1   
        for i in range(len(s)):
            print(s[i])
            hashset=[]
            length = 0
            for j in range(i,len(s)):
                if s[j] not in hashset:
                    length += 1
                    hashset.append(s[j])
                    print(hashset)
                else:
                    break
                if length > result:
                    result = length                    
        return result
    

    

     
                    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        result = 0  
        usedchar = {}
        start = 0
        index = 0
        for c in s:
            if c  in usedchar and start <= usedchar[c]:
                start = usedchar[c]+1
                print(c)
                print(usedchar[c])
                print(start)
            else:                
                result = max(result, index - start + 1)
                
            usedchar[c] = index
            index += 1
        print(usedchar)
        
        return result


        
        
        
def main():
    ret = Solution().lengthOfLongestSubstring("abcabcbb")
    print(ret)
    
if __name__ == '__main__':
    main()
            
            