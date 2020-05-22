//
//  937. Reorder Data in Log Files.cpp
//  cpp_lambda
//
//  Created by Xujian CHEN on 5/21/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        
        // lambda function
        // find first ' ', if the the next char is alphabet, then it is LetterLog
        auto isLetterLog = [](const string& str){
            long i = str.find(' ');
            return isalpha(str[i+1]);
        };
        
        // stable_partition, partition the vector according to lambda function isLetterLog's return.
        // it return the iterator pointing to the first item that is false from isLetterLog.
        auto it = stable_partition(logs.begin(), logs.end(), isLetterLog);
        
        // lambda function
        // if sub_a is equal to sub_b, compare a and b. Otherwise, compare sub_a and sub_b.
        auto subOrWhole = [](string& a, string& b){
            string sub_a = string(a.begin()+a.find(' '), a.end());
            string sub_b = string(b.begin()+b.find(' '), b.end());
            return (sub_a == sub_b) ? a < b : sub_a < sub_b;
            
        };
        
        // sort the letter logs partition in the logs
        sort(logs.begin(), it, subOrWhole);
        
        return logs;
        
    }
};
