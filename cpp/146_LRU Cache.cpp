//
//  146_LRU Cache.cpp
//  xcode_debug
//
//  Created by Xujian CHEN on 5/10/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//
#include <iostream>
#include <map>
#include <vector>
using namespace std;

class LRUCache {
    vector <int> keys;
    int len;
    int cap;
    std::map<int, int> cache;
    
public:
    LRUCache(int capacity) {
        cap = capacity;
        len = 0;
    }
    
    int get(int key) {
        std::map<int,int>::iterator it;
        it = cache.find(key);
        if (it != cache.end()){
            keys.erase(std::remove(keys.begin(), keys.end(), key), keys.end());
            keys.push_back(key);
            
            return cache[key];
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (len < cap){
            std::map<int, int>::iterator it = cache.find(key);
            if (it != cache.end())
                it->second = value;
            else
                cache.insert(std::pair<int,int>(key, value));
            len ++;
        }
        else{
            //cache.insert(std::pair<int,int>(key, value));
            std::map<int, int>::iterator it = cache.find(key);
            if (it != cache.end()){
                it->second = value;
                keys.erase(std::remove(keys.begin(), keys.end(), key), keys.end());
            }
            
            else{
                int k2del = keys.front();
                keys.erase(keys.begin());
                cache.erase(k2del);
                cache.insert(std::pair<int,int>(key, value));
            }
        }
        keys.push_back(key);
        
    }
};



/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

int main(){
    LRUCache* obj = new LRUCache(2);
    obj->get(2);
    obj->put(2,6);
    obj->get(1);
    obj->put(1,5);
    obj->put(1,2);
    int param_1 = obj->get(1);
    param_1 = obj->get(2);
    cout << param_1;

}
