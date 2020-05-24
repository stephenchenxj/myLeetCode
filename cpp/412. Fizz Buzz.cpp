/*
 412. Fizz Buzz
Easy

818

1112

Add to List

Share
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
Accepted
317,076
Submissions
513,387
*/

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> rslt;
        for(int i = 1; i<n+1; ++i){
            if(i%3 == 0 && i%5 == 0){
                rslt.push_back("FizzBuzz");
            }
            else if(i%3 == 0){
                rslt.push_back("Fizz");
            }
            else if(i%5 == 0){
                rslt.push_back("Buzz");
            }
            else
                rslt.push_back(to_string(i));
        }
        
        
        return rslt;
        
    }
};
