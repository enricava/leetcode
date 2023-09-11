// https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            level = []
            remaining = len(q)
            while remaining:
                nxt = q.popleft()
                level.append(nxt.val)
                q.extend(nxt.children)
                remaining -=1
            result.append(level)
        return result