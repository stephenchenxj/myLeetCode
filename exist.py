# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:55:54 2019

@author: stephen.chen

Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.



"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        
        def search(r, c, i):
            m = len(self.board)  # row
            n = len(self.board[0])      # col
            
            if r >= m or r < 0:
                return False
            if c >= n or c < 0:
                return False            
            if self.board[r][c] != word[i]: # it's not a match
                return False
            
            # Find a match 
            backup = self.board[r][c]
            self.board[r][c]=0 # set it to a non-char, so will not search it again in the future
            
            if i == len(word) - 1: # reach the end of the word
                return True
            # have not reach the end of the word
            result = search(r-1, c, i+1) or search(r+1, c, i+1) or search(r, c-1, i+1) or search(r, c+1, i+1)
            self.board[r][c] = backup
            return result
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                result = search(i, j, 0)
                if result == True:
                    return True
        return False
                     

board =[
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]]

word = "AAB"
       
test = Solution()
print(test.exist(board, word))            
            
        