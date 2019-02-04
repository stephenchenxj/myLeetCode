#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:13:25 2019

@author: dev
"""

from random import randrange

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.randomSet:
            self.randomSet.append(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        random_index = randrange(len(self.randomSet))
        return(self.randomSet[random_index])
        
def main():
    obj = RandomizedSet()
    print(param_1 = obj.insert(1))
    param_2 = obj.remove(2)
    param_3 = obj.getRandom()
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()