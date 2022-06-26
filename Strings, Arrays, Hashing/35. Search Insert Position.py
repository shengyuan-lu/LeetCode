import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)

    def helper(self, nums, left_index, right_index, target) -> int:
        
        mid_index = math.floor((right_index - left_index / 2))
        
        if left_index == len(nums):
            return len(nums)
        
        elif right_index < 0:
            return 0
        
        elif right_index - left_index < 0:
            return left_index
        
        elif nums[mid_index] == target:
            return mid_index
        
        elif nums[mid_index] < target:
            return self.helper(nums, mid_index+1, right_index, target)
        
        elif nums[mid_index] > target:
            return self.helper(nums, left_index, mid_index-1, target)
