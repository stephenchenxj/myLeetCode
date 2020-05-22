//
//  206. Reverse Linked List.cpp
//  cpp_lambda
//
//  Created by Xujian CHEN on 5/22/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 206. Reverse Linked List
 Easy

 4108

 84

 Add to List

 Share
 Reverse a singly linked list.

 Example:

 Input: 1->2->3->4->5->NULL
 Output: 5->4->3->2->1->NULL
 Follow up:

 A linked list can be reversed either iteratively or recursively. Could you implement both?

 Accepted
 934,009
 Submissions
 1,527,557
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* leftNode = nullptr;
        ListNode* currentNode = head;
        ListNode* rightNode = nullptr;
        
        while((currentNode) ){
            rightNode = currentNode->next;
            currentNode->next = leftNode;
            leftNode = currentNode;
            currentNode = rightNode;
        }
        return leftNode;
        
    }
};
