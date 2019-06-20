#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:29:54 2019

@author: dev
"""

class Solution(object):
    result = 0
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = 0
        
        summ = sum(nums)
        #print(summ)
        
        # (summ + S) must be even 
        if (summ + S) % 2 != 0:
            return res
        
        if len(nums) == 1:
            if nums[0] == abs(S):
                return 1
            else:
                return 0 
            
        if nums[0] == 0:
            preDic = {0:2}
        else:
            preDic = {nums[0]:1,-nums[0]:1}
        
        
        
        for n in nums[1:]:
            keys = preDic.keys()
#            print(keys)
            curDic = dict()
            for key in keys:
                curDic[key + n] = preDic[key] + curDic.get ((key + n) ,0)
                curDic[key - n] = preDic[key] + curDic.get ((key - n) ,0)
                
#                if (key + n) in curDic.keys():
#                    curDic[key + n] += preDic[key] 
#                else:
#                    curDic[key + n] = preDic[key] 
#                if (key - n) in curDic.keys():
#                    curDic[key - n] += preDic[key] 
#                else:
#                    curDic[key - n] = preDic[key] 
            
#            print(n)
            #print(preDic)
            preDic=(curDic.copy())
            #print(preDic)
        
        
        return curDic.get (S ,0)
    
    
    
    def helper(self, nums, S, pos, eval):
        print(eval)
        if pos == len(nums):
            if S == eval:
                self.result += 1
            return
        self.helper(nums, S, pos+1, eval + nums[pos])
        self.helper(nums, S, pos+1, eval - nums[pos])
    def findTargetSumWaysDFS(self, nums, S):
        self.result = 0
        if nums == None or len(nums)== 0: 
            return self.result
        self.helper(nums, S, 0, 0);
        return self.result
    
    
    
def main():


    mySolution = Solution()
    print(mySolution.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 10))
    #print(mySolution.findTargetSumWaysDFS([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 10))
    print(mySolution.findTargetSumWaysDFS([1,2,3],2))
    
if __name__ == '__main__':
    main()