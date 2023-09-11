// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hp(root, targetSum):
            if not root and targetSum == 0:
                return True
            elif not root:
                return False

            return hp(root.left, targetSum - root.val) or hp(root.right, targetSum - root.val)
        
        if not root and targetSum == 0:
                return False
            
        return hp(root, targetSum)