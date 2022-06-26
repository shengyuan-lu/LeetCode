# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.satb_helper(nums)
    
    
    # [1,2,3,4,5,6,7]
    # 4 , [1-3], [5-6]
    
    
    def satb_helper(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len(nums) == 0:
            return
        else:
            mid_pt = math.floor(len(nums)/2)

            root = TreeNode(nums[mid_pt])

            left = nums[0 : mid_pt]
            right = nums[mid_pt+1 :]

            root.left = self.satb_helper(left)
            root.right = self.satb_helper(right)

            return root
