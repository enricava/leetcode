// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root)[1]
    
    def balanced(self, root):
        if not root:
            return 0, True
        
        l = self.balanced(root.left)
        r = self.balanced(root.right)
        
        return 1 + max(l[0],r[0]) , l[1] and r[1] and abs(l[0]-r[0]) <= 1