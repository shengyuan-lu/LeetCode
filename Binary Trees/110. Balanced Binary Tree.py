# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: # no node
            return True
        elif root != None and (root.left == None and root.right == None):
            return True
        elif abs(self.find_max_height(root.left, 0) - self.find_max_height(root.right, 0)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
            
            
    def find_max_height(self, root, height) -> int:
        if root == None:
            return height
        else:
            return max(self.find_max_height(root.left, height + 1), self.find_max_height(root.right, height + 1))
