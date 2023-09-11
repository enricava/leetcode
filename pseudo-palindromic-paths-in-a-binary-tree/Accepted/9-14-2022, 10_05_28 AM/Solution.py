// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.curr = {}
        
        def put(self, k):
            if k not in self.curr:
                self.curr[k] = 1
            else:
                self.curr[k] += 1
                
        def pop(self, k):
            if self.curr[k] == 1:
                del self.curr[k]
            else:
                self.curr[k] -= 1

        
        def pp(self, root):
            put(self, root.val)
            if not root.left and not root.right:
                odds = 0
                for k in self.curr:
                    if self.curr[k] % 2 != 0:
                        odds +=1
                        if odds == 2:
                            break
                if odds <= 1:
                    self.count += 1
                    
            if root.left:
                pp(self,root.left)
            if root.right:
                pp(self,root.right)
                
            pop(self,root.val)
        
        pp(self, root)
        return self.count