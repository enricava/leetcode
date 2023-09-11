// https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def pruneSub(root):
            """
            True->ok
            False->remove
            """
            l, r = False, False
            if root.left:
                l = pruneSub(root.left)
            if root.right:
                r = pruneSub(root.right)
                
            if not l:
                root.left = None
            if not r:
                root.right = None
            
            if (root.val != 1 and not l and not r):
                return False
            
            return True
            
        if not pruneSub(root):
            return None
        return root