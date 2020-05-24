//
//  155. Min Stack.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/24/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 155. Min Stack
 Easy

 3156

 304

 Add to List

 Share
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

 push(x) -- Push element x onto stack.
 pop() -- Removes the element on top of the stack.
 top() -- Get the top element.
 getMin() -- Retrieve the minimum element in the stack.
  

 Example 1:

 Input
 ["MinStack","push","push","push","getMin","pop","top","getMin"]
 [[],[-2],[0],[-3],[],[],[],[]]

 Output
 [null,null,null,null,-3,null,0,-2]

 Explanation
 MinStack minStack = new MinStack();
 minStack.push(-2);
 minStack.push(0);
 minStack.push(-3);
 minStack.getMin(); // return -3
 minStack.pop();
 minStack.top();    // return 0
 minStack.getMin(); // return -2
  

 Constraints:

 Methods pop, top and getMin operations will always be called on non-empty stacks.
 Accepted
 529,240
 Submissions
 1,214,581
 */

#include <iostream>
#include <vector>

using namespace std;

class MinStack {
    vector<int> data;
    vector<int> mins;
    //int m;
public:
    /** initialize your data structure here. */
    MinStack() {
        mins.push_back(INT_MAX);
        //m = INT_MAX;
    }
    
    void push(int x) {
        /*
        if(m>x){
            m = x;
            cout<<m<<endl;
        }
        mins.push_back(m);
        */
        if (mins.back()>x){
            mins.push_back(x);
        }else{
            mins.push_back(mins.back());
        }
        
        
        data.push_back(x);
    }
    
    void pop() {
        data.pop_back();
        mins.pop_back();
    }
    
    int top() {
        return data.back();
    }
    
    int getMin() {
        return mins.back();
    }
};
 


/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
int main(){
    
    MinStack* obj = new MinStack();
    int a;
    obj->push(2147483646);
    obj->push(2147483646);
    obj->push(21474836467);
    a = obj->top();
    cout<<a<<endl;
    obj->pop();
    a = obj->getMin();
    cout<<a<<endl;
    obj->pop();
    a = obj->getMin();
    cout<<a<<endl;
    obj->pop();
    obj->push(21474836467);
    a = obj->top();
    cout<<a<<endl;
    a = obj->getMin();
    cout<<a<<endl;
    obj->push(-21474836468);
    a = obj->top();
    cout<<a<<endl;
    a = obj->getMin();
    cout<<a<<endl;
    obj->pop();
    a = obj->getMin();
    cout<<a<<endl;
    
    return 0;
    
}
