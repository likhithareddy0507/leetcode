/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// Helper function to check if two trees are mirror images of each other
bool isMirror(struct TreeNode* t1, struct TreeNode* t2) {
    if (!t1 && !t2) return true; // Both nodes are null
    if (!t1 || !t2) return false; // One node is null, the other is not
    return (t1->val == t2->val) &&
           isMirror(t1->left, t2->right) &&
           isMirror(t1->right, t2->left);
}

// Main function to check if the tree is symmetric
bool isSymmetric(struct TreeNode* root) {
    if (!root) return true; // An empty tree is symmetric
    return isMirror(root->left, root->right);
}