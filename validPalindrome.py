# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 04:41:13 2019

@author: stephen.chen
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for c in s:            
            if c.isalnum():
                while not s[-1].isalnum():
                    s =s[:-1]                    
                if c.upper() != s[-1].upper():
                    return False
                else:
                    s =s[:-1]
        return True
                        
                
                
        
        
def main():
    mySolution = Solution()
    print(mySolution.isPalindrome("0P"))
    
if __name__ == '__main__':
    main()