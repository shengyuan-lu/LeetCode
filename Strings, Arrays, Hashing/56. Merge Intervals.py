class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sorted_intervals_by_start_time = sorted(intervals, key=lambda x: x[0])
        
        rtr_lst = list()
        temp_interval = list()
        
        for interval in sorted_intervals_by_start_time:
            if len(temp_interval) == 0:
                temp_interval = interval
            
            elif interval[1] <= temp_interval[1]:
                continue
             
            elif interval[0] >= temp_interval[0] and interval[0] <= temp_interval[1]:
                temp_interval[1] = interval[1]
                
            else:
                rtr_lst.append(temp_interval)
                temp_interval = interval
     
    
        if len(temp_interval) != 0:
            rtr_lst.append(temp_interval)
        
        return rtr_lst
