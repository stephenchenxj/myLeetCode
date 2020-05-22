//
//  937. Reorder Data in Log Files.cpp
//  cpp_lambda
//
//  Created by Xujian CHEN on 5/21/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//
/*
 937. Reorder Data in Log Files
 Easy

 521

 1619

 Add to List

 Share
 You have an array of logs.  Each log is a space delimited string of words.

 For each log, the first word in each log is an alphanumeric identifier.  Then, either:

 Each word after the identifier will consist only of lowercase letters, or;
 Each word after the identifier will consist only of digits.
 We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

 Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

 Return the final order of the logs.

  

 Example 1:

 Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
 Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
  

 Constraints:

 0 <= logs.length <= 100
 3 <= logs[i].length <= 100
 logs[i] is guaranteed to have an identifier, and a word after the identifier.
 Accepted
 104,489
 Submissions
 193,674
 
 */

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
