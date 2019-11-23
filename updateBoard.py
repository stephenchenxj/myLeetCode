# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:53:20 2019

@author: stephen.chen

529. Minesweeper
Medium

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

    If a mine ('M') is revealed, then the game is over - change it to 'X'.
    If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    Return the board when no more squares will be revealed.

 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

 

Note:

    The range of the input matrix's height and width is [1,50].
    The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
    The input board won't be a stage when game is over (some mines have been revealed).
    For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.


"""
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r = click[0]
        c = click[1]
        checked = dict()
        def adjMines(r,c):
            cnt = 0
            a = max(0,r-1)
            b = min(len(board),r+2)
            d = max(0,c-1)
            e = min(len(board[0]),c+2)
            for i in range(a,b):
                for j in range(d,e):
                    if board[i][j] == 'M':
                        cnt += 1
            if cnt == 0:
                board[r][c] = 'B'
            else:
                board[r][c] = str(cnt)
            return cnt
        
        def checkNeighbor(r,c):
            if not checked.get((r,c)):
                checked[(r,c)] = True
                a = max(0,r-1)
                b = min(len(board),r+2)
                d = max(0,c-1)
                e = min(len(board[0]),c+2)
                for i in range(a,b):
                    for j in range(d,e):
                        if adjMines(i,j) == 0:
                            checkNeighbor(i,j)
            
            
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        elif board[r][c] == 'E':
            cnt = adjMines(r,c)
            if cnt == 0:
                checkNeighbor(r,c)
                
            return board
        else:
            return board
            
        
        
board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

click = [3,0]
test = Solution()
print(test.updateBoard(board, click))
click = [1,2]
print(test.updateBoard(board, click))

a = str(1)
print(a)
print(type(a))