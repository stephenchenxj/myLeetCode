# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:14:28 2019

@author: stephen.chen

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"





"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre = ''
        
        num = 0
        if n <= 0:
            return pre
        
        for i in range(n):
            say = ''
            repeat = ''
            if pre == '':
                say = '1'
            else:
                for c in pre:
                    if c == repeat: # repeated digit
                        num += 1
                    else: # a new digit                        
                        if repeat != '':
                            say += str(num)+repeat
                        repeat = c
                        num = 1
                say += str(num)+repeat   
            pre = say
            
        return say
                    
        
        
def main():
    test = Solution()
    result = (test.countAndSay(5))
    print (result)
    
if __name__ == '__main__':
    main()