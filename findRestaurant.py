#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:09:08 2019

@author: dev

599. Minimum Index Sum of Two Lists
Easy

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:

    The length of both lists will be in the range of [1, 1000].
    The length of strings in both lists will be in the range of [1, 30].
    The index is starting from 0 to the list length minus 1.
    No duplicates in both lists.

Accepted
75,683
Submissions
152,628

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