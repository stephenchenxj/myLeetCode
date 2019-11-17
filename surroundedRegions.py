# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 22:55:42 2019

@author: stephen.chen
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the 
board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to 
an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent 
cells connected horizontally or vertically.
Accepted
171,365
Submissions
698,011
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row <= 1:
            return board
        col = len(board[0])
        if col <= 1:
            return board
        
        #first step: find all the '0' on the border, store them
        border0s = []
        for i in range(row):
            #first col
            if board[i][0] == '0':
                border0s.append((i,0))            
            #last col
            if board[i][col-1] == '0':
                border0s.append((i,col-1))    
                
        for j in range(col):
            #first row
            if board[0][j] == '0':
                border0s.append((0,j))            
            #last row
            if board[row-1][j] == '0':
                border0s.append((row-1,j))  
        
        def markConnected0(loc, preserve):
            r = loc[0]
            c = loc[1]
            locs = []
            if r + 1 < row:
                if board[r+1][c] == '0':   
                    locs.append((r+1,c))
            if c + 1 < col:
                if board[r][c+1] == '0':
                    locs.append((r,c+1))
            if r - 1 >= 0:
                if board[r-1][c] == '0':  
                    locs.append((r-1,c))
            if c - 1 >= 0:
                if board[r][c-1] == '0':
                    locs.append((r,c-1))
                    
            return locs
            

        preserve = dict()
        while border0s:
            loc = border0s.pop()
            preserve[loc] = True
            newLocs = markConnected0(loc, preserve)
            for newLoc in newLocs:
                if not preserve.get(newLoc):
                    border0s.append(newLoc)
                    preserve[newLoc] = True
        for i in range(row):
            for j in range(col):
                if not preserve.get((i,j)):
                    board[i][j] = 'X'
                
        return board
    
board = [['X', 'X', 'X', 'X'],
         ['X', '0', '0', 'X'],
         ['X', 'X', '0', 'X'],
         ['X', '0', 'X', 'X']]        
test = Solution()
print(test.solve(board))
