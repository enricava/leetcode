// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        ok = True
        if root.left:
            ok = ok and root.left.val < root.val and self.isValidBST(root.left)
        
        if root.right:
            ok = ok and root.right.val > root.val and self.isValidBST(root.right)
            
        return ok
            