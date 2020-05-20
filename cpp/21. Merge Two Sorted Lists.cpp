//
//  21. Merge Two Sorted Lists.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/20/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//
/*
21. Merge Two Sorted Lists
Easy

3858

565

Add to List

Share
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
Accepted
948,745
Submissions
1,809,522
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode * head = nullptr;
        ListNode * preNode = nullptr;
        
        while(l1!=nullptr & l2!=nullptr)
        {
            if(l1->val <= l2->val){
                if (head == nullptr){
                    head = l1;
                    preNode = head;
                }else{
                    preNode->next = l1;
                    preNode = l1;
                }
                l1= l1->next;
            }else{
                if (head == nullptr){
                    head = l2;
                    preNode = head;
                }else{
                    preNode->next = l2;
                    preNode = l2;
                }
                l2 = l2->next;
            }
        }
        
        if(l1!=nullptr){
            if (head == nullptr){
                head = l1;
                preNode = head;
            }else{
                preNode->next = l1;
            }
            
        }
        if(l2!=nullptr){
            if (head == nullptr){
                head = l2;
                preNode = head;
            }else{
                preNode->next = l2;
            }
        }
        
        return head;
    }
};


class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode dummy(0);
        ListNode *tail = &dummy;
        
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }

        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};
