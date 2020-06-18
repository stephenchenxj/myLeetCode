//
//  sort_hashmap_priorityqueue_vector.cpp
//  leetcode
//
//  Created by xujian chen on 6/13/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>        // std::priority_queue
#include <unordered_map>
#include <string>
#include <sstream>



int main(void){
    // data contains the text to process. We want to find the frequence of the words.
    std::string data{"My doggy ate my essay He picked up all my mail He cleaned my dirty closet and dusted with his tail I love my doggy"};
    
    // convert string to lower case
    std::for_each(data.begin(), data.end(), [](char & c) {
        c = ::tolower(c);
    });
    
    
    std::stringstream ss(data); // Insert the string into a stream
    std::vector<std::string> words; // Create vector to hold our words
    std::string buf;                 // Have a buffer string
    while (ss >> buf)
        words.push_back(buf);
    
    // a natural way is to use a hash table to record how many times each word appears
    std::unordered_map<std::string, int> wordsCount;
    for (std::string buf : words){
        ++wordsCount[buf];
    }
    
    //display the hash table
    for( auto const& p: wordsCount )
      std::cout << p.first << " appears " << p.second << '\n';
    
    //display the hash table method 2
    for (auto it = wordsCount.begin(); it != wordsCount.end(); ++ it)
        std::cout<<it->first << " appears " << it->second << " time(s)" << '\n';
    
    //display the hash table method 3
    std::for_each(wordsCount.begin(), wordsCount.end(), [](const std::pair<std::string, int>& w_c){ std::cout<< w_c.first << " appears " << w_c.second << " times \n"; } );
    
    std::vector<std::string> keys;
    keys.reserve (wordsCount.size());
    std::cout<< "\nSort the words by word's alphabetical order\n";
    for (auto& it : wordsCount) {
        keys.push_back(it.first);
    }
    std::sort (keys.begin(), keys.end());
    for (auto& key : keys) {
        std::cout << key << ' ' << wordsCount[key] << '\n';
    }
    
    std::cout<< "\nSort the words by word's frequency \n";
    // can't sort un_orderedmap, so, need to create a vector of std::pair<std::string, int>, then sort this vector
    std::vector<std::pair<std::string, int>> elems(wordsCount.begin(), wordsCount.end());
    // Using lambda expression, sort this vector by frequency. If the frequence is the same, sort in key's alphabetical order
    std::sort(elems.begin(), elems.end(), [](const std::pair<std::string, int>& left, const std::pair<std::string, int>& right){
        if (left.second == right.second) return left.first < right.first;
        return left.second > right.second;});
    for (auto& elem : elems) {
        std::cout << elem.first << " appears " << elem.second << " time(s) \n" ;
    }
    
    // if you only care about the top frequency words, it's no need to create the entire vector. In stead, just keep the k-th top frequency words in a priority queue.
    int k = 3; // suppose we only want to find top 3 words.
    std::cout<< "\nFind the top kth highest frequency words\n";
    // lambda function that compare left and right. Need to keep the smallest item on top, if reach the capacity, pop the smallest item from the top.
    typedef std::function<bool(const std::pair<std::string, int>&, const std::pair<std::string, int>&)> Compare;
    Compare cmp = [](const std::pair<std::string, int>&left, const std::pair<std::string, int>& right){
            if(left.second == right.second) return left.first < right.first;
            return left.second > right.second;
        };
    std::priority_queue<std::pair<std::string, int>, std::vector<std::pair<std::string, int>>, Compare> pq(cmp);
    
    
    for (auto it = wordsCount.begin(); it != wordsCount.end(); ++ it){ // traverse the word-frequency hash table.
        pq.push(*it); // push it to the priority queue.
        if (pq.size() > k) pq.pop(); // if the priority queue reach the capacity, pop the smallest item from the top
    }
    
    std::vector<std::string> result_keys;
    while(!pq.empty()){
        auto item = pq.top();
        result_keys.push_back(item.first);
        pq.pop();
    }
    
    //because the highest frequent word is popped the last from the priority queue, need to traverse the vector using reverse_interator.
    for(auto it = result_keys.rbegin(); it != result_keys.rend(); ++it){
        std::cout<< *it << " appears " << wordsCount[*it] << " times\n";
    }
    
    
    
        
    
    return 0;
}
