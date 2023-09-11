// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def pr(node, maxim, minim):
            if not node:
                return maxim - minim
            
            maxim = max(maxim, node.val)
            minim = min(minim, node.val)
            
            left = pr(node.left, maxim, minim)
            right = pr(node.right, maxim, minim)
            
            return max(left, right)
        
        return pr(root, root.val, root.val)