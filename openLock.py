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
        move = {}
        for i in range(10):
            move[str(i)] = [str(((i-1)+10)%10), str((i+1)%10)]
    
        q = ['0000']
        while q: # when q is not empty
            steps += 1
            newQ = []
            for key in q:
                for i in range(8):
                    newKey = key[:int(i/2)] + move[key[int(i/2)]][i%2] + key[int(i/2)+1:]
                    if newKey == target:
                        return steps
                    elif newKey not in deadNchecked:
                        newQ.append(newKey)
            for key in q:
                deadNchecked.add(key)
            q = newQ
        
        return -1
        
        
        
        
        
def main():
    deadends = ["0500"]
    target = '3250'
    print(Solution().openLock(deadends,target))
    
#    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#    target = '8888'
#    print(Solution().openLock(deadends,target))
    
if __name__ == '__main__':
    main()