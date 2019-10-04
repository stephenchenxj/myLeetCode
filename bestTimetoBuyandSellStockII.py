# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 05:21:33 2019

@author: stephen.chen
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) <= 1:
            return 0
        
        profit = 0
        low = prices[0]
        
        for i in range(len(prices)):
            if prices[i]>low:
                profit += prices[i] - low
            low = prices[i]
            
        return profit
    
    
def main():
      mySolution = Solution()
      print (mySolution.maxProfit([]))
  
if __name__ == '__main__':
    main()
    
