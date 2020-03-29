#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:18:15 2020

@author: stephenchen

541. Reverse String II
Easy

359

1061

Add to List

Share
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
Accepted
79,607
Submissions
167,514
Seen this question in a real interview before?

Yes

No

"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        rslt = []
        rounds = len(s)//(2*k)
        rmain = len(s)%(2*k)
        
        
        for i in range(rounds):
            for j in range(2*k):
                if j < k: # reverse
                    rslt.append(s[i*2*k+k-j-1])
                else:
                    rslt.append(s[i*2*k+j])
                    
        if rmain > k:
            for j in range(k):
                rslt.append(s[rounds*2*k+k-j-1])
            for j in range(k, rmain):
                rslt.append(s[rounds*2*k+j])
        elif rmain <= k and rmain > 0:
            for j in range(rmain):
                rslt.append(s[rounds*2*k+rmain-j-1])
            
            
        
        
        return ''.join(rslt)
    
s = 'a'
k = 4
print(Solution().reverseStr(s, k))