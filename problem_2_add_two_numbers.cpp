/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* root = new ListNode(0);
        ListNode* curr = root;
        
        ListNode* p_l1 = l1;
        ListNode* p_l2 = l2;
        
        int carry = 0;
        
        while (p_l1 || p_l2) {
            int x = (p_l1 != NULL) ? p_l1->val : 0;
            int y = (p_l2 != NULL) ? p_l2->val : 0;
            int sum = x + y + carry;
            
            carry = sum/10;
            curr->val = sum%10;
            
            if (p_l1 != NULL) {
                p_l1 = p_l1->next;
            }
            if (p_l2 != NULL) {
                p_l2 = p_l2->next;
            }
            if (p_l1 || p_l2) {
                curr->next = new ListNode(0);
                curr = curr->next;
            }
        }
        if (carry == 1) {
            curr->next = new ListNode(1);
        }
        return root;
    }
};