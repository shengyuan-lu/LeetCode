class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l_result_lst = [1]*len(nums) # stores value 0 ... i - 1 (exclude i)
        r_result_lst = [1]*len(nums) # stores value i + 1 ... end (exclude i)
        
        l_result = 1
        
        for i in range(0, len(nums)):
            l_result_lst[i] = l_result
            l_result *= nums[i]
            
        r_result = 1
        
        for i in range(len(nums)-1, -1, -1):
            r_result_lst[i] = r_result
            r_result *= nums[i]
            
        ans = [l_result_lst[i]*r_result_lst[i] for i in range(len(nums))]

        return ans
