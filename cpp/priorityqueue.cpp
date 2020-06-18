//
//  sort_hashmap_priorityqueue_vector.cpp
//  leetcode
//
//  Created by xujian chen on 6/13/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

// http://www.cplusplus.com/reference/queue/priority_queue/
// std::priority_queue
// template <class T, class Container = vector<T>, class Compare = less<typename Container::value_type> > class priority_queue;

//T
//Type of the elements.
//Aliased as member type priority_queue::value_type.

//Container
//Type of the internal underlying container object where the elements are stored.
//Its value_type shall be T.
//Aliased as member type priority_queue::container_type.

//Compare
//A binary predicate that takes two elements (of type T) as arguments and returns a bool.
//The expression comp(a,b), where comp is an object of this type and a and b are elements in the container,
//shall return true if a is considered to go before b in the strict weak ordering the function defines.
//The priority_queue uses this function to maintain the elements sorted in a way that preserves heap properties
//(i.e., that the element popped is the last according to this strict weak ordering).
//This can be a function pointer or a function object, and defaults to less<T>, which returns the same as
//applying the less-than operator (a<b).


#include <iostream>
#include <vector>
#include <queue>        // std::priority_queue
#include <unordered_map>
#include <string>
#include <sstream>

//can't define a function inside the main() function. So put compFunc here.
bool compFunc (const std::pair<std::string, int>&left, const std::pair<std::string, int>& right  ){
    if(left.second == right.second) return left.first < right.first;
    return left.second > right.second;
};



int main(void){
    // data contains the text to process. We want to find the frequence of the words.
    std::string data{"My doggy picked up all my mail I love my doggy"};
    
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
    
    std::cout<<"Display the hash table: \n";
    for( auto const& p: wordsCount )
      std::cout << p.first << " appears " << p.second << "\n";
    
    
    
    
    
    
    class CompFunctor {
    public:
        bool operator() (std::pair<std::string, int>& a, std::pair<std::string, int>& b ) {
            //std::cout<<"in () function \n";
            if(a.second == b.second) return a.first < b.first;
            return a.second > b.second;
        };
    };
    
    // it is fine to define a lambda expression(function) in the main() function.
    //std::function<bool(const std::pair<std::string, int>&, const std::pair<std::string, int>&)> compLambda = [](const std::pair<std::string, int>&left, const std::pair<std::string, int>& right  ) // this is actual type of the compLambda function.
    auto compLambda = [](const std::pair<std::string, int>&left, const std::pair<std::string, int>& right) // normally just use auto for lambda function.
    {
        if(left.second == right.second) return left.first < right.first;
        return left.second > right.second;
    };
    
    std::priority_queue<std::pair<std::string, int>, std::vector<std::pair<std::string, int>>, CompFunctor> pq1;
    std::priority_queue<std::pair<std::string, int>, std::vector<std::pair<std::string, int>>, std::function<decltype(compFunc)>> pq2(compFunc);
    //std::priority_queue<std::pair<std::string, int>, std::vector<std::pair<std::string, int>>, std::function<bool(const std::pair<std::string, int>&, const std::pair<std::string, int>&)>> pq3(compLambda);
    std::priority_queue<std::pair<std::string, int>, std::vector<std::pair<std::string, int>>, decltype(compLambda)> pq3(compLambda); //A lambda is an object (hence why we're referring to it as a functor, rather than a function) so has a type and can be stored.
    
    
    for (auto it = wordsCount.begin(); it != wordsCount.end(); ++ it){ // traverse the word-frequency hash table.
        pq1.push(*it); // push it to the priority queue.
        pq2.push(*it);
        pq3.push(*it);
    }
    
    std::cout << "Method 1: \n";
    while(!pq1.empty()){
        auto item = pq1.top();
        std::cout<< (item.first) << " : " << item.second << '\n';
        pq1.pop();
    }
    std::cout << "Method 2: \n";
    while(!pq2.empty()){
        auto item = pq2.top();
        std::cout<< (item.first) << " : " << item.second << '\n';
        pq2.pop();
    }
    std::cout << "Method 3: \n";
    while(!pq3.empty()){
        auto item = pq3.top();
        std::cout<< (item.first) << " : " << item.second << '\n';
        pq3.pop();
    }
        
    
    return 0;
}
