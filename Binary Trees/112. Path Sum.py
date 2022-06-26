# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        else:
            return self.check_value(root, 0, targetSum)
    
    def check_value(self, root, current_val, targetSum) -> bool:
        if root == None:
            return current_val == targetSum
        elif root and (root.left == None and root.right == None):
            return root.val + current_val == targetSum
        elif root and (root.left != None and root.right == None):
            return self.check_value(root.left, root.val + current_val, targetSum)
        elif root and (root.left == None and root.right != None):
            return self.check_value(root.right, root.val + current_val, targetSum)
        else:
            return self.check_value(root.left, root.val + current_val, targetSum) or self.check_value(root.right, root.val + current_val, targetSum)
