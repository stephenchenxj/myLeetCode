#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:35:00 2020

@author: chen


146. LRU Cache
Medium

4978

220

Add to List

Share
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 

Accepted
468,056
Submissions
1,522,924

"""
class DoubleLinkedNode():
    def __init__(self, k, v):
        self.v = v
        self.k = k
        self.next = None
        self.pre = None
        
    
    

class LRUCache():
    
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    def pop_earlest(self):
        node = self.tail.pre
        self.remove(self.tail.pre)
        return node
        
    def add(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node
        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.head = DoubleLinkedNode(None, None)
        self.tail = DoubleLinkedNode(None, None)
        self.ht = dict()
        
        self.head.next =self.tail
        self.tail.pre = self.head
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.ht.get(key) != None:
            node = self.ht.get(key) 
            self.remove(node)
            self.add(node)
            
            return self.ht[key].v
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.ht.get(key) 
        if node!= None:
            self.remove(node)
            node.v = value
            node.k = key
            self.add(node)
            del self.ht[key]
        else:
            node = DoubleLinkedNode(key, value)
            
            if self.size < self.cap:
                self.add(node)
                self.size += 1
            else:
                node2del = self.pop_earlest()
                self.add(node)
                del self.ht[node2del.k]
                
        self.ht[key] = node
                
                
        

            
cache =  LRUCache( 2 )

cache.put(1, 1);
cache.put(2, 2);
print(cache.get(1) )     
cache.put(3, 3);   
print(cache.get(2))
cache.put(4, 4);   
cache.put(1, 1);  
print(cache.get(1))       
print(cache.get(3))     
print(cache.get(4))    

