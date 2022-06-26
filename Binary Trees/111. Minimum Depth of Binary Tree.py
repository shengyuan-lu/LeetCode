# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.min_depth_helper(root, 0)
    

    def min_depth_helper(self, root: Optional[TreeNode], currentDepth) -> int:
        
        # check if leaf node, if leaf node, return depth
        
        if root == None: # root node = 0, or dummy node
            return currentDepth
        elif root and (root.left == None and root.right == None): # leaf node confirmed
            return currentDepth + 1
        elif root.left == None and root.right != None:
            return self.min_depth_helper(root.right, currentDepth+1)
        elif root.left != None and root.right == None:
            return self.min_depth_helper(root.left, currentDepth+1)
        else:
            return min(self.min_depth_helper(root.left, currentDepth+1), self.min_depth_helper(root.right, currentDepth+1))
