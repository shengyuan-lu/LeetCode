class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]: 
        result = list()
        
        min_heap = list()
        
        len_1 = len(nums1)
        
        len_2 = len(nums2)
        
        for i in range(min(k, len_2)):
            total = nums1[0] + nums2[i]
            min_heap.append((total, 0, i))
                            
        
        heapq.heapify(min_heap)
                            
        while k != 0 and len(min_heap) != 0:
            _, a, b = heapq.heappop(min_heap)
            result.append([nums1[a], nums2[b]])
            
            k -= 1
                            
            if a + 1 < len_1:
                total = nums1[a+1] + nums2[b]
                heapq.heappush(min_heap, (total, a+1, b))
            
        return result
