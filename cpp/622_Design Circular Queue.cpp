//
//  622_Design Circular Queue.cpp
//  xcode_debug
//
//  Created by Xujian CHEN on 5/9/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//


#include <iostream>

using namespace std;

class MyCircularQueue {
private:
    int * array;
    int head = 0;
    int tail = -1;
    int size = 0;
    int len = 0;

public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        array = new int[k];
        this->size = k;
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (this->isFull()){
            return false;
        }
        if (this->tail < this->size-1){
            this->tail ++;
            this->len ++;
            this->array[this->tail] = value;
        }
        else if (this->tail == this->size-1){
            this->tail = 0;
            this->len ++;
            this->array[this->tail] = value;
        }
        return true;
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (this->isEmpty()){
            return false;
        }
        if (this->head < this->size-1){
            this->head ++;
            this->len --;
        }
        else if (this->head == this->size-1){
            this->head = 0;
            this->len --;
        }
        return true;

    }

    /** Get the front item from the queue. */
    int Front() {
        if (this->isEmpty()){
            return -1;
        }
        return this->array[this->head];
    }

    /** Get the last item from the queue. */
    int Rear() {
        if (this->isEmpty()){
            return -1;
        }
        return this->array[this->tail];
    }

    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return (this->len == 0);
    }

    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return (this->len == this->size);
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */

int main()
{
    MyCircularQueue* obj = new MyCircularQueue(5);
    bool param_1 = obj->enQueue(1);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(2);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(3);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(4);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(5);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(6);
    cout<< param_1 << endl;
    int param_3 = obj->Front();
    cout<< "Front is: " << param_3 << endl;
    int param_4 = obj->Rear();
    cout<< "Rear is: " << param_4 << endl;

    cout<< "De Queue status: " ;
    bool param_2 = obj->deQueue();
    cout<< param_2 << endl;
    param_3 = obj->Front();
    cout<< "Front is: " << param_3 << endl;
    param_4 = obj->Rear();
    cout<< "Rear is: " << param_4 << endl;

    cout<< "De Queue status: " ;
    param_2 = obj->deQueue();
    cout<< param_2 << endl;
    param_3 = obj->Front();
    cout<< "Front is: " << param_3 << endl;
    param_4 = obj->Rear();
    cout<< "Rear is: " << param_4 << endl;

    param_1 = obj->enQueue(7);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(8);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(9);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(10);
    cout<< param_1 << endl;
    param_1 = obj->enQueue(11);

    param_3 = obj->Front();
    cout<< "Front is: " << param_3 << endl;
    param_4 = obj->Rear();
    cout<< "Rear is: " << param_4 << endl;
    bool param_5 = obj->isEmpty();
    bool param_6 = obj->isFull();
}
