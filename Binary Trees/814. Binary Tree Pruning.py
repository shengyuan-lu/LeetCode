# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> Optional[TreeNode]:
        
        # post order, take a look at left, right, than the root
        
        self.prune_tree_helper(root, root.left, True)
        self.prune_tree_helper(root, root.right, False)
            
        if root.left == None and root.right == None:
            if root.val == 0:
                root = None

        return root
        
        
    def prune_tree_helper(self, parent: TreeNode, current: Optional[TreeNode], isLeft):
        
        # check if leaf node, if 0 -> remove, if 1 -> not remove
        
        if current: # if not leaf node -> recursion     
            self.prune_tree_helper(current, current.left, True)
            self.prune_tree_helper(current, current.right, False)
            
            if current.left == None and current.right == None: # Leaf node confirmed
                if current.val == 0: # remove it
                    if isLeft:
                        parent.left = None
                    else:
                        parent.right = None
