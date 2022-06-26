import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        
        if len(nums) == 0:
            return 0
        else:
            prev_poped = heapq.heappop(nums)
            
            max_seq = 1
            
            current_seq = 1

            for i in range(0, len(nums)):
                next_pop = heapq.heappop(nums)
                
                if next_pop - prev_poped == 1:
                    current_seq += 1
                elif next_pop - prev_poped == 0:
                    current_seq += 0
                else:
                    current_seq = 1
                    
                if current_seq > max_seq:
                    max_seq = current_seq
                
                prev_poped = next_pop
                    
            return max_seq
