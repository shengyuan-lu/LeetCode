# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_max_depth(root, 0)
    
    
    def find_max_depth(self, root, current_depth) -> int:
        if root == None:
            return current_depth
        else:
            return max(self.find_max_depth(root.left, current_depth+1), self.find_max_depth(root.right, current_depth+1))
