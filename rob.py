# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:42:51 2019

@author: stephen.chen

House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.



"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        max_2 = nums[0]
        max_1 = max(nums[0], nums[1])
        max_current = 0
        
        for n in nums[2:]:
            max_current = max((n + max_2), max_1) 
            max_2 = max_1
            max_1 = max_current
            
        return max_current
    
def main():
    mySolution = Solution()
    print(mySolution.rob([1,2,3,1]))
    
if __name__ == '__main__':
    main()
        