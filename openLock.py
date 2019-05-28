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
                for i in range(4):
                    newKey1 = key[:i] + move[key[i]][0] + key[i+1:]
                    newKey2 = key[:i] + move[key[i]][1] + key[i+1:]
                    #print (newKey1)
                    #print(newKey2)
                    if newKey1 in deadNchecked:
                        continue
                    elif newKey1 == target:
                        return steps
                    else:
                        newQ.append(newKey1)
                        #deadNchecked.add(newKey1)
                        
                    if newKey2 in deadNchecked:
                        continue
                    elif newKey2 == target:
                        return steps
                    else:
                        newQ.append(newKey2)
                        #deadNchecked.add(newKey2)
#                print( 'steps = %d , newQ is ' %steps)
#                print (newQ)
                        
                #deadNchecked.add(key)
                
            
            q = newQ
        
        return -1
        
        
        
        
        
def main():
    deadends = ["0100"]
    target = '2200'
    print(Solution().openLock(deadends,target))
    
#    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#    target = '8888'
#    print(Solution().openLock(deadends,target))
    
if __name__ == '__main__':
    main()