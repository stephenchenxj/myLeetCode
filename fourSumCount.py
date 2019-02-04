#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:51:36 2019

@author: dev
"""
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        total = 0
        AB_sum = {}
        for i in A:
            for j in B:
                s = i + j
                if s not in AB_sum:
                    AB_sum[s] = 1
                else:
                    AB_sum[s] += 1
                    
        CD_sum = {}
        for i in C:
            for j in D:
                s = i + j
                if s not in CD_sum:
                    CD_sum[s] = 1
                else:
                    CD_sum[s] += 1
        #print(AB_sum)
        #print(CD_sum)
        
        for k in AB_sum:
            #print(k)
            if(-k) in CD_sum:
                total += AB_sum[k]*CD_sum[-k]
                
        return total
                
            
        
        
def main():
    ret = Solution().fourSumCount([1,2,3], [0, -1, -4], [1,-2,3], [3, -1, -2])
    print(ret)
                
if __name__ == '__main__':
    main()
