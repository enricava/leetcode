// https://leetcode.com/problems/construct-string-from-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ''
        
        sol = '{}'.format(root.val)
        
        if not root.left and not root.right:
            return sol
        
        if not root.right:
            return sol + '({})'.format(self.tree2str(root.left))
        
        return sol + '({})({})'.format(self.tree2str(root.left), self.tree2str(root.right))