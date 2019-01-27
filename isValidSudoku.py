#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 21:51:57 2019

@author: dev
"""

class Solution(object):
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        if len(board) != 9:
            return False
        
        for line in board:
            if len(line) != 9:
                return False
        
        for i in range(9):
            subList = board[i]
            if not self.hasRepeatedNumber (subList):
                return False
        
        for i in range(9):
            subList = []
            for j in range(9):
                subList.append( board[j][i])
            if not self.hasRepeatedNumber (subList):
                return False
            
        
        for i in range(3):            
            for j in range(3):
                subList = []
                for m in range(3):            
                    for n in range(3):                
                        subList.append( board[j*3+n][i*3+m])
                if not self.hasRepeatedNumber (subList):
                    return False         
        
        return True
    
    def hasRepeatedNumber(self, subList):
        if len(subList) != 9:
            print('Length is not 9')
            return False
        hashmap = {}
        for n in subList:
            if n != '.':
                if n in hashmap:
                    return False
                else:
                    hashmap[n]=1
        return True    
        
def main():
    
    sodoku  = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    
    
    
    ret = Solution().isValidSudoku(sodoku)
    print(ret)
    
    
if __name__ == '__main__':
    main()
