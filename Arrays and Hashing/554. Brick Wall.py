class Solution:
    
    def leastBricks(self, wall: List[List[int]]) -> int:
        # [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
        
        # Step 1: calculate the cut through point
        # [[1,3,5,6], [3,4,6], [1,4,6] ...] the not cut through point, but 0 and width of wall doesn't count
        
        dic = dict()
        
        width_of_wall = sum(wall[0])
        
        for i in range(0, len(wall)):
            
            prev_total = 0
            
            for j in range(0, len(wall[i])):
                wall[i][j] += prev_total
                
                if wall[i][j] != width_of_wall:
                    
                    if wall[i][j] in dic.keys():
                        dic[wall[i][j]] += 1
                    else:
                        dic[wall[i][j]] = 1

                    prev_total = wall[i][j]
                
        # 0 and width_of_wall is not included
        
        max_val = 0
        max_key = 0
        
        for i, (k,v) in enumerate(dic.items()):
            if v > max_val:
               max_val = v
                
        
        return len(wall) - max_val
