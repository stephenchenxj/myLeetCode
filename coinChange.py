# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 03:18:32 2019

@author: stephen.chen

Coin Change

You are given coins of different denominations and a total amount of money 
amount. Write a function to compute the fewest number of coins that you need 
to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

"""

class Solution(object):
    
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ''' it is too slow
        self.mem = {0:0}        
        def search(coins, amount):        
            if amount in self.mem.keys():
                return self.mem[amount]            
            count = []
            for c in coins:
                if c == amount:
                    return 1
                if amount - c > 0:
                    temp = search(coins, amount-c)
                    if temp != -1:
                        temp += 1
                        count.append(temp)
            if len(count)> 0:
                self.mem[amount] = min(count)
                return self.mem[amount] 
            else: 
                return -1            
        return search(coins, amount)
        '''
        minCnt = [amount+1]*(amount+1)
        minCnt[0] = 0
        for c in coins:
            for i in range(amount+1):
                if i-c >= 0:
                    minCnt[i] = min(minCnt[i-c]+1, minCnt[i])
        
        if minCnt[amount]== amount + 1:
            return -1
        return minCnt[amount]
        
        
test =  Solution()

coins = [186,419,83,408]
amount = 1000
print(test.coinChange(coins, amount)) 


            
        

