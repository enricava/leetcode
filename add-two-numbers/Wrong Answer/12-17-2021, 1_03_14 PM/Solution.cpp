// https://leetcode.com/problems/add-two-numbers

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
    ListNode* addThreeNumbers(ListNode* l1, ListNode* l2, int c) {
        ListNode * result = new ListNode();
        int a = 0, b = 0;
        if(l1 == nullptr && l2 == nullptr) return nullptr;
        if(l1 != nullptr){
            a = l1->val;
            l1 = l1->next;
        }
        if(l2 != nullptr){
            b = l2->val;
            l2 = l2->next;
        }
        int res = a+b+c;
        if(a+b+c >= 10){
            result->val = res%10;
            result->next = addThreeNumbers(l1,l2,1);
        }
        else {
            result->val = res;
            result->next = addThreeNumbers(l1,l2,0);
        }
        return result;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addThreeNumbers(l1,l2, 0);
    }
};