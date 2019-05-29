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
#        move = {'0':['9', '1'], '1':['0', '2'], '2':['1', '3'], '3':['2', '4'],
#                '4':['3', '5'], '5':['4', '6'], '6':['5', '7'], '7':['6', '8'], 
#                '8':['7', '9'], '9':['8', '0']}
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
                        #deadNchecked.add(newKey1)
                        
#                print( 'steps = %d , newQ is ' %steps)
#                print (newQ)
                        
                #deadNchecked.add(key)
                
                deadNchecked.add(key)
            q = newQ
#            print( 'steps = %d , newQ is ' %steps)
#            print (newQ)
#            print( ' deadNchecked is ')
#            print (deadNchecked)
        
        return -1
        
        
        
        
        
def main():
    deadends = ["0500"]
    target = '3000'
    print(Solution().openLock(deadends,target))
    
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = '8888'
    print(Solution().openLock(deadends,target))
    
if __name__ == '__main__':
    main()