//
//  346_Moving Average from Data Stream.cpp
//  xcode_debug
//
//  Created by Xujian CHEN on 5/9/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

#include <iostream>
using namespace std;

class MovingAverage {
private:
    int filter_size;
    int cnt;
    int * data;
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        filter_size = size;
        data = new int [size];
    }

    double next(int val) {
        double rslt = 0;
        if (cnt < filter_size){
            data[cnt] = val;
            cnt ++;
            for (int i = 0; i < cnt; ++i){
                rslt += double(data[i])/(cnt);
            }
        }
        else{
            data[cnt%filter_size] = val;
            cnt ++;
            for (int i = 0; i < filter_size; ++i){
                rslt += double(data[i])/(filter_size);
            }

        }


        return rslt;
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
int main()
{
    MovingAverage* obj = new MovingAverage(3);
    double param_1 = obj->next(1);
    cout<< "param_1: " << param_1 << endl;
    param_1 = obj->next(2);
    cout<< "param_1: " << param_1 << endl;
    param_1 = obj->next(3);
    cout<< "param_1: " << param_1 << endl;
    param_1 = obj->next(4);
    cout<< "param_1: " << param_1 << endl;
}
