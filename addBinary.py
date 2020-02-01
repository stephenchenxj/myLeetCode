#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:04:17 2019

@author: dev
67. Add Binary
Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Accepted
381,343
Submissions
908,135
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        '''
        v_a = 0
        for i in range(len(a)):
            if a[len(a)-i-1] == '1':
                v_a +=  2** i
        v_b = 0
        for i in range(len(b)):            
            if b[len(b)-i-1] == '1':              
                v_b +=  2** i
        
        v = v_a + v_b
        '''
        
        length = max(len(a),len(b)) +1
        result = [None]*length
        forward = 0
        for i in range(length):
            v_a = 0
            v_b = 0
            if i < len(a):
                #print(a[len(a)-i-1])
                if a[len(a)-i-1] == '1':
                    v_a = 1
                
            if i < len(b):
                #print(b[len(b)-i-1])
                if b[len(b)-i-1] == '1':
                    v_b = 1
            '''
            print('length = %d' %length)
            print('i = %d' %i)
            print('length = %d' %length)
            print('length-i-1 = %d' %(length-i-1))
            '''
            
            if v_a + v_b + forward== 0:
                result[length-i-1] = '0'
                forward = 0
            elif v_a + v_b + forward== 1:
                result[length-i-1] = '1'
                forward = 0
            elif v_a + v_b + forward== 2:
                result[length-i-1] = '0'
                forward = 1
            elif v_a + v_b + forward== 3:
                result[length-i-1] = '1'
                forward = 1       
        if result[0] == '0':
            del result[0]
        mystr = ''.join(result)
        return mystr
        
        
        
        
def main():
    a = '10101'
    b = '10'
    ret = Solution().addBinary(a,b)
    print(ret)
    
if __name__ == '__main__':
    main()