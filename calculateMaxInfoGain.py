#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:37:36 2019

@author: dev
"""
import math

class Solution(object):
    
    def calculateEntropy(self, input):
        """
        :type input: List[int]
        :rtype: float
        """
        p = dict()
        
        n = len(input)
        for i in input:
            if i not in p.keys():
                p[i] = float(input.count(i))/n
                
        #print (p)
        
        entropy = 0
        for i in p.keys():
            #print(p[i])
            entropy += -1*p[i]*math.log(p[i],2)
            
        return entropy
    
    def split(self, lengths, species, l):
        '''
        rtype: species_a and species_b
        '''
        species_a = []
        species_b = []
        
        for i in range(len(lengths)):
            if lengths[i] <= l:
                species_a.append(species[i])
            else:
                species_b.append(species[i])
        return species_a, species_b
        
    
    def calculateMaxInfoGain(self, petal_length, species):
        """
        :type petal_length: List[float]
        :type species: List[str]
        :rtype: float
        """
        
        H = self.calculateEntropy(species)
        
        print (H)
        
#        cluster = dict()
#        for i in range(len(species)):
#            if species[i] in cluster.keys():
#                cluster[species[i]].append(petal_length[i])
#            else:
#                cluster[species[i]] = [ petal_length[i] ]
#                
#        center = dict()
#        for key in cluster.keys():
#            center[key] = sum(cluster[key])/len(cluster[key])
        
        H_max = 0
        l = 0 

        for length in petal_length:
            a, b = self.split(petal_length, species, length)
            H_a = self.calculateEntropy(a)
            H_b = self.calculateEntropy(b)
            
            temp = H - H_a*len(a)/len(species) - H_b*len(b)/len(species)
            
            if H_max < temp:
                H_max = temp
                l = length
            
      
        
        
        return H_max, l
        
        
def main():
    species = ["versicolor","versicolor","setosa","virginica","virginica","versicolor","versicolor","setosa","versicolor","versicolor"]
    length = [1,2,3,4,5,6,7,8,9,10]
    solution = Solution()
    print (solution.calculateMaxInfoGain(length, species))
    
if __name__ == '__main__':
    main()