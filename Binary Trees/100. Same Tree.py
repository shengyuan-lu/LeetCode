# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)
    
    def helper(self, p, q) -> bool:
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p != None and q != None:
            if p.val == q.val:
                return self.helper(p.left, q.left) and self.helper(p.right, q.right)
            else:
                return False
