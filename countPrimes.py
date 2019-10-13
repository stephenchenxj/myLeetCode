# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:53:15 2019

@author: stephen.chen

 Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.




"""
from math import sqrt

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n < 3:
            return 0
        prime = [1]*n
        prime[0] = 0
        prime[1] = 0
        for i in range(2,int(sqrt(n))+1):
            if prime[i] == 1:
                j = 2*i
                while(j<n):                    
                    prime[j]=0
                    j += i
                    
        
        return sum(prime)
    
mySolution = Solution()
print (mySolution.countPrimes(12))
                