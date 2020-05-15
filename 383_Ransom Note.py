#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:08:12 2020

@author: chen

383. Ransom Note
Easy

476

167

Add to List

Share
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
Accepted
143,921
Submissions
277,978

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        htr = dict()
        htm = dict()
        for c in ransomNote:
            htr[c] = htr.get(c, 0) + 1
        for c in magazine:
            htm[c] = htm.get(c, 0) + 1
            
        for k in htr.keys():
            if k not in htm:
                return False
            if htr[k] > htm[k]:
                return False
        return True


