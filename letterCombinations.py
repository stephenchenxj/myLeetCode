# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 05:06:14 2019

@author: stephen.chen

Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.


"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'],
              '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        rst = []
        for d in digits:
            if rst == []:
                rst = dict[d]
            else:
                temp = []
                for c in dict[d]:
                    for s in rst:
                        temp.append (s+c)
                rst = temp
            
        return rst
                    
            
            
test = Solution()
print (test.letterCombinations('23'))
            
            
      