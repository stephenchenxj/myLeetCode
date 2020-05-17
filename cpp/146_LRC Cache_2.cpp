//
//  146_LRC Cache_2.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/16/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

#include <unordered_map>
#include <list>
#include <iostream>
using namespace std;
class LRUCache {
private:
    int cap_;
    list<pair<int,int>> cache_; // list of pairs. For each pair, first: key, second: value
    unordered_map<int, list<pair<int,int>>::iterator> m_; // map, first: key, second: iterator to access cache_'s node with first= key
public:
    LRUCache(int capacity){
        cap_ = capacity;
    }
    int get(int key){
        auto it = m_.find(key);//search m_, if key exists.
        if(it == m_.cend()) return -1; // could not find key
        
        //find the key in m_. it->second is the iterator to access cache_ pair (key, value)
        cache_.splice(cache_.cbegin(),cache_, it->second); // move this pair to the front of the list cache_
        return it->second->second; // return the value. it is the iterator in m_, it->second is the iterator of cache_. it->second->second is the string value of pair<int,string> in cache_.
    }
    void put(int key, int value){
        auto it = m_.find(key); //search m_, if key exists.
        if(it != m_.cend()){ //if found
            it->second->second = value; //update its value in the cache_
            cache_.splice(cache_.cbegin(), cache_, it->second); // move this pair to the front of the list cache_
            return;
        }
        //key not found. Means we need to create a new pair in the cache_, and record its iterator in the m_
        if(cache_.size() == cap_){ // full. Need to pop least recently used item
            auto it2pop = cache_.back(); // get the pair of the least recently used item from the back of the list
            m_.erase(it2pop.first); // this pair's first is the key. erase it from m_
            cache_.pop_back(); //pop_back it from the cache_ too.
        }
        
        cache_.emplace_front(key, value); //emplace a new pair at the front of the list cache_
        m_[key] = cache_.begin(); //create map item, record the key, and its iterator in cache_.
    }
};


int main(void){

    
    
    
    LRUCache cache =  LRUCache( 2 );
    
    int rslt = 0;

    cache.put(1, 1);
    cache.put(2, 2);
    rslt = cache.get(1);       // returns 1
    cout<<rslt<<endl;
    cache.put(3, 3);    // evicts key 2
    rslt = cache.get(2);       // returns -1 (not found)
    cout<<rslt<<endl;
    cache.put(4, 4);    // evicts key 1
    rslt = cache.get(1);       // returns -1 (not found)
    cout<<rslt<<endl;
    rslt = cache.get(3);       // returns 3
    cout<<rslt<<endl;
    rslt = cache.get(4);       // returns 4
    cout<<rslt<<endl;

    
    return 1;
    
}
