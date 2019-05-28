#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:14:48 2019

@author: chen
"""

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        steps = 0
        deadNchecked = set(deadends)
        print (deadNchecked)
        move = {'0':['9', '1'], '1':['0', '2'], '2':['1', '3'], '3':['2', '4'],
                '4':['3', '5'], '5':['4', '6'], '6':['5', '7'], '7':['6', '8'], 
                '8':['7', '9'], '9':['8', '0']}
        q = ['0000']
        while q: # when q is not empty
            steps += 1
            for key in q:
                if key == target:
                    return steps
                
                for i in range(4):
                    newKey1 = key[:i] + move[key[i]][0] + key[i+1:]
                    newKey2 = key[:i] + move[key[i]][1] + key[i+1:]
                    #print (newKey1)
                    #print(newKey2)
                    if newKey1 in deadNchecked:
                        continue
                    else:
                        q.append(newKey1)
                        deadNchecked.add(newKey1)
                        
                    if newKey2 in deadNchecked:
                        continue
                    else:
                        q.append(newKey2)
                        deadNchecked.add(newKey2)
                deadNchecked.add(key)
                q.remove(key)
        
        return -1
        
        
        
        
        
def main():
    deadends = ['1234', '2000']
    target = '3210'
    print(Solution().openLock(deadends,target))
    
if __name__ == '__main__':
    main()