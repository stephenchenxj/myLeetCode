#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:36:20 2020

@author: stephenchen

1128. Number of Equivalent Domino Pairs
Easy

139

82

Add to List

Share
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

"""

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d = dict()
        cnt = 0
        for domino in dominoes:
            temp = sorted(domino)
            s = tuple(temp)
            if s not in d.keys():
                d[s] = 1
            else:
                d[s] += 1
                if cnt < d[s]:
                    cnt = d[s]
        
        rslt = 0
        for key in d.keys():  
            if d[key]>1:
                s = d[key]*(d[key]-1)
                rslt += (s/2)
        
        return int(rslt)
    
    
dominoes =    [[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]

print(Solution().numEquivDominoPairs(dominoes))