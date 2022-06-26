# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root and (root.left == None and root.right == None): # single node
            return True
        else:
            return self.compare(root.left, root.right)
    
    
    def compare(self, left, right) -> bool:
        
        if left == None and right == None:
            return True
        elif (left == None and right != None) or (left != None and right == None):
            return False
        elif left != None and right != None:
            if left.val == right.val:
                return self.compare(left.left, right.right) and self.compare(left.right, right.left)
            else:
                return False
