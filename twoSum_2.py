#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:43:01 2019

@author: dev
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                elif numbers[i] + numbers[j] > target:
                    break
        '''

        fw = 0
        bw = len(numbers) -1    
        
        while fw < bw:
            if numbers[fw] + numbers[bw] == target:
                return [fw+1, bw+1]
            elif numbers[fw] + numbers[bw] < target:
                fw += 1
            else:
                bw -= 1
        
        
def main():
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target))
    
if __name__ == '__main__':
    main()