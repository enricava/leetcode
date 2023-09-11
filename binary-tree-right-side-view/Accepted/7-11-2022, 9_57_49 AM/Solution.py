// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        side = [root.val]
        q = [root]
        while q:
            l = len(q)
            val = 0
            ok = False
            while l > 0:
                elem = q.pop(0)
                if elem.left:
                    q.append(elem.left)
                    val = elem.left.val
                    ok = True
                if elem.right:
                    q.append(elem.right)
                    val = elem.right.val
                    ok = True
                l -= 1
            if ok:
                side.append(val)
        return side