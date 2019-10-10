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
        odd = 1
        even = 0
        for i in range(n-1):
            odd, even = self.waysToClimb(odd, even)
        
        return odd+even
    
    def waysToClimb(self, odd,even):
        newOdd = even + odd
        newEven = odd
        return newOdd, newEven
    
    
        

def main():
    mySolution = Solution()
    print (mySolution.climbStairs(5))
    
if __name__ == '__main__':
    main()

        