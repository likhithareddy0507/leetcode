/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // Create a dummy node to simplify result list creation
    struct ListNode dummy;
    struct ListNode* current = &dummy;
    dummy.next = NULL;
    
    int carry = 0;  // Initialize carry to 0
    
    // Traverse both linked lists
    while (l1 || l2 || carry) {
        int sum = carry;  // Start with the carry
        
        // Add the value from the first list, if available
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        
        // Add the value from the second list, if available
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        // Calculate the new carry and the current digit
        carry = sum / 10;
        int digit = sum % 10;
        
        // Create a new node for the current digit and append it to the result
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = digit;
        newNode->next = NULL;
        current->next = newNode;
        current = newNode;
    }
    
    return dummy.next;  // Return the head of the resulting linked list
}