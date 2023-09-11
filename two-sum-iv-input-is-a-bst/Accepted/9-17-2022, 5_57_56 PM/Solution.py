// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        
        q = [root]
        m = {}
        array = []
        while q:
            k = len(q)
            for i in range(k):
                root = q.pop(0)
                if root:
                    array.append(root.val)
                    m[root.val] = len(array)-1
                    q.append(root.left)
                    q.append(root.right)
                    
        for i,elem in enumerate(array):
            if target-elem in m and m[target-elem] != i:
                return True
        
        return False
        