#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:28:49 2020

@author: stephenchen
Zombie Matrix
user profile image
System made a post.
Given a 2D grid, each cell is either a zombie or a human. Zombies can turn adjacent (up/down/left/right) human beings into zombies every day. Find out how many days does it take to infect all humans?

Input:
matrix, a 2D integer array where a[i][j] = 1 represents a zombie on the cell and a[i][j] = 0 represents a human on the cell.

Output:
Return an integer represent how many days does it take to infect all humans.
Return -1 if no zombie exists.

Example :
Input:
[[0, 1, 1, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 0, 0, 0]]

Output:
2

Explanation:
At the end of the day 1, the status of the grid:
[[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[0, 1, 0, 1, 1],
[1, 1, 1, 0, 1]]

At the end of the day 2, the status of the grid:
[[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1]]

"""


def humanDays(matrix):
    
    queue = []
    m = len(matrix)
    n = len(matrix[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                queue.append([i,j])
                cnt += 1
    if cnt == 0:
        return -1 # no zombie exists
    elif cnt == m*n:
        return 0 # all zombies
    
    def infect(z_loc):
        no_new_z = 0
        [i,j] = z_loc
        if i+1 < m:
            if matrix[i+1][j] == 0:
                matrix[i+1][j] = 1
                no_new_z += 1
                queue.append([i+1,j])
        if i-1 >= 0:
            if matrix[i-1][j] == 0:
                matrix[i-1][j] = 1
                no_new_z += 1   
                queue.append([i-1,j])
        if j+1 < n:
            if matrix[i][j+1] == 0:
                matrix[i][j+1] = 1
                no_new_z += 1
                queue.append([i,j+1])
        if j-1 >= 0:
            if matrix[i][j-1] == 0:
                matrix[i][j-1] = 1
                no_new_z += 1   
                queue.append([i,j-1])
        return no_new_z
    
    day = 0
    cnt_new = 0
    while queue:
        z_loc = queue.pop(0)
        cnt -= 1
        cnt_new += infect(z_loc)
        
        if cnt == 0 and cnt_new > 0:
            day += 1
            cnt = cnt_new
            cnt_new = 0
            
    return day

M = [[1,0]]
print(humanDays(M))