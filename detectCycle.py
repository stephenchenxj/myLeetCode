#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:07:32 2019

@author: chen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:35:46 2019

@author: chen
"""

class Node(object):
    def __init__(self, val = -1):
        """
        Initialize your data structure here.
        """
        self.next = self.pre = None
        self.val = val
        


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0


    def getNode(self, index):
        """
        Get the index-th node in the linked list. If the index is invalid, return None.
        :type index: int
        :rtype: Node
        """
        if index > self.size:
            return None
        
        currentNode = self.head.next
        while index > 0:
            index -= 1
            nextNode = currentNode.next
            currentNode = nextNode
        return currentNode
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size:
            return -1
        
        currentNode = self.getNode(index)
        return currentNode.val
        
        


        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.size + 1:
            indexNode = self.tail
        elif index <= self.size:
            indexNode = self.getNode(index)
        elif index > self.size +1:
            return
        newNode = Node(val)
        newNode.next = indexNode
        nodeBeforeIndex = indexNode.pre
        nodeBeforeIndex.next = newNode
        indexNode.pre = newNode
        newNode.pre = nodeBeforeIndex
        self.size += 1
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(1, val)
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index <= self.size  and index > 0:
            indexNode = self.getNode(index)
        else:
            return
        
        indexNode.next.pre = indexNode.pre
        indexNode.pre.next = indexNode.next
        del indexNode
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

'''
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]

'''        
        
      
def main():
    
    obj = MyLinkedList() 
    print(obj)
    
    val = 1
    print( obj.addAtHead(val) )
    
    val = 3
    print( obj.addAtTail(val) )
    
    index = 1
    val = 2
    print( obj.addAtIndex(index,val) )
    
    index = 1
    print( obj.get(index) )
    
    index = 1
    print( obj.deleteAtIndex(index) )
    
    print( obj.get(index) )
    
if __name__ == '__main__':
    main()