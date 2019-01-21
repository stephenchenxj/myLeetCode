#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:09:08 2019

@author: dev
"""

class Solution(object):
    def __init__(self):
        self.hashmap1 = {}
        self.hashmap2 = {}
    
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index = 0
        for restaurant in list1:
            self.hashmap1[restaurant] = index
            index += 1
        
        '''        
        index = 0
        for restaurant in list2:
            if restaurant in self.hashmap1:
                print (restaurant)            
                self.hashmap2[index + self.hashmap1[restaurant] ] = restaurant
            index += 1
            
        for i in range(999*2):
            if i in self.hashmap2:
                return self.hashmap2[i]
        print(self.hashmap1)
        print(self.hashmap2)
        '''       
        index = 0
        for restaurant in list2:
            if restaurant in self.hashmap1:
                print (restaurant)            
                if (index + self.hashmap1[restaurant]) not in self.hashmap2:
                    self.hashmap2[index + self.hashmap1[restaurant]] = [restaurant]
                else:
                    self.hashmap2[index + self.hashmap1[restaurant]].append(restaurant)  
                print(self.hashmap2)
            index += 1            
            
        print(self.hashmap1)
        print(self.hashmap2)
        
        for i in range(999*2):
            if i in self.hashmap2:
                return self.hashmap2[i]
        
        
        
def main():
    ret = Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Burger King","Tapioca Express","Shogun"])
    print (ret)
    
if __name__ == '__main__':
    main()