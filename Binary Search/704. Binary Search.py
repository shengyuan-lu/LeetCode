import math

class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        return self.search_helper(nums, 0, len(nums)-1, target)
    
    
    def search_helper(self, nums, left_index, right_index, target) -> int:
        
        if left_index > right_index:
            return -1
        else:
            mid_index = (left_index + right_index) // 2
            
            if nums[mid_index] == target:
                return mid_index
            
            elif nums[mid_index] < target: # we need to search to the right
                return self.search_helper(nums, mid_index + 1, right_index, target)
            
            elif nums[mid_index] > target: # we need to search to the left
                return self.search_helper(nums, left_index, mid_index - 1, target)
