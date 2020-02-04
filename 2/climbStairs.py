# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:02:32 2019

@author: stephen.chen

Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        f(3) = 3:            
        1,1,1
        2,  1
        
        1,2
        
        f(4) = 5:
        1,1,1, 1
        2,1,   1
        1,2,   1
        
        1,1,2
        2,2
        
        总结规律： f(n) = f(n-1)+f(n-2), f(1) = 1, f(2)=2
        can't use recursive method directly, too many repeated function call.
        so, build a hash map from bottomn up.
        
        '''
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        stairs = dict()
        stairs[1] = 1
        stairs[2] = 2
        for i in range(3,n):
            stairs[i] = stairs[i-1] + stairs[i-2]
            
        return stairs[n-1] + stairs[n-2]
    
    
        

def main():
    mySolution = Solution()
    print (mySolution.climbStairs(35))
    
if __name__ == '__main__':
    main()

        