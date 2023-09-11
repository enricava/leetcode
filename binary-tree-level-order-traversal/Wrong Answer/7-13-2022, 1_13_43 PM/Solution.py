// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        q = [root]
        levelorder = []
        while q:
            l = len(q)
            level = []
            while l > 0:
                n = q.pop(0)
                l -= 1
                level.append(n.val)
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
            levelorder.append(level)
        
        return levelorder
            
            