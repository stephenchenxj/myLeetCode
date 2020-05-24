//
//  main.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/23/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

#include <iostream>

using namespace std;
class MyHashMap {
    struct Node{
        int key;
        int value;
        Node* next;
        Node(int k, int val):key(k), value(val), next(NULL){}
        Node(){}
    };
    
    const static int SIZE = 10001;
    Node* pArray[SIZE];
    
    int hash(int key){
        return key%SIZE;
    };
    
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        for(int i = 0; i < SIZE; ++i){
            pArray[i] = NULL;
        }
        //pArray = new Node[SIZE];
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int index = hash(key);
        Node* node = pArray[index]; //&array[index];
        while (node != NULL){
            if(node->key == key){
                node->value = value;
                return;
            }
            node = node->next;
        }
        
        Node* newHead= new Node(key, value);
        newHead->next = pArray[index];
        pArray[index] = newHead;
        
        
        //Node newNode = Node(key, value); // have to use new to create the Node dynamically. //Otherwise, the address of this newNode will remain the same.
        //newNode.next = pArray[index];
        //pArray[index] = &newNode;
    }
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int index = hash(key);
        Node* node = pArray[index];  //&array[index];
        while (node != NULL){
            if(node->key == key){
                return node->value;
            }
            node = node->next;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int index = hash(key);
        Node* node = pArray[index];  //&array[index];
        while (node != NULL){
            if(node->key == key){
                node->value = -1;
                return;
            }
            node = node->next;
        }
    }
};



int main(void){
    MyHashMap map = MyHashMap();
    map.put(1,1);
    map.put(20003,2);
    map.put(10002,3);
    int a;
    a = map.get(1);
    cout << a << endl;
    a = map.get(20003);
    cout << a << endl;
    a = map.get(10002);
    cout << a << endl;
    

    
}
