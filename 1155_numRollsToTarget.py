#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:42:07 2020

@author: stephenchen


1155. Number of Dice Rolls With Target Sum
Medium

412

28

Add to List

Share
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
Accepted
24,787
Submissions
50,170


"""


class Solution(object):
    hm = dict()
    f = 0
    
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        ways = 0
        if self.f != f: # it means an object with a new face number is created. The class viarable hm is not valid anymore
            self.f = f
            self.hm = dict()
        
        if f*d < target or target < d:
            return ways
        if d == 1:
            if target <= f:
                ways = 1
        for i in range(1,f+1):
            if (d-1, target-i) not in self.hm:  
                temp = self.numRollsToTarget(d-1, f, target - i)
                self.hm[(d-1, target-i)] = temp
            ways += self.hm[(d-1, target-i)]                
        return ways
    
d = 2
f = 5
target = 10
print(Solution().numRollsToTarget(d, f, target))