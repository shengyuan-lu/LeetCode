import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # store the closest points (heap, or priority queue)
        
        # the associatoin betwen the euclidean distance and points
        
        # O(nlogn)
        
        heap = list()
        
        for pt in points: # O(n)
            x, y = pt
            
            distance = math.sqrt(math.pow(x,2) + math.pow(y,2))
            
            heap.append((distance, x, y))
            
        heapq.heapify(heap) # O(n)
            
        return_lst = list()
        
        for i in range(0, k): #O(k) k <= n, still O(n)
            
            if len(heap) != 0:
                _, x, y = heapq.heappop(heap)
                l = list()

                l.append(x)
                l.append(y)

                return_lst.append(l)
            
            
        return return_lst
