class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        
        for i in range(0, len(nums)):
            if target-nums[i] in dic.keys():
                return [i, dic[target-nums[i]]]
            else:
                dic[nums[i]] = i
