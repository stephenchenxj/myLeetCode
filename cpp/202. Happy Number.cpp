//
//  202. Happy Number.cpp
//  cpp_lambda
//
//  Created by Xujian CHEN on 5/22/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//
/*
 202. Happy Number
 Easy

 1943

 409

 Add to List

 Share
 Write an algorithm to determine if a number n is "happy".

 A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

 Return True if n is a happy number, and False if not.

 Example:

 Input: 19
 Output: true
 Explanation:
 12 + 92 = 82
 82 + 22 = 68
 62 + 82 = 100
 12 + 02 + 02 = 1
 Accepted
 488,753
 Submissions
 978,642
 */

class Solution {
private:
    bool helper(int& n, unordered_map<int, bool>& visited){
        if(n == 1) return true;
        
        if (visited[n] == true) return false;
        
        visited[n] = true;
        int m = 0;
        while(n){
            m += pow((n%10),2);
            n /= 10;
        }
        return helper(m, visited);
        
    }
public:
    bool isHappy(int n) {
        
        unordered_map<int, bool> visited;
        
        return helper(n, visited);
    }
};
