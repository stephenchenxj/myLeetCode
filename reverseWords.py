#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:27:40 2019

@author: dev
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp = s.split(' ')
        
        while '' in temp:
            temp.remove('')
        
        result = []
        while temp:
            result.append(temp.pop())
            #result.append(' ')
#            result += (temp.pop())
#            result += (' ')
#            result
        
        
        #return result
        return ' '.join(result)
        
        
        
def main():
    s = "the sky   is blue!"
    print(Solution().reverseWords(s))
    
if __name__ == '__main__':
    main()