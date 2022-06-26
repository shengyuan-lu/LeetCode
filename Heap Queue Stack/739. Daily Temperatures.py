class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        
        ans = [0] * len(temperatures)
        
        for current_index in range(0, len(temperatures)):
            
            while len(stack) != 0:
                if stack[-1][0] < temperatures[current_index]:
                    temp, old_index = stack.pop()
                    ans[old_index] = current_index - old_index
                else:
                    break
            
            stack.append((temperatures[current_index], current_index))
                
    
        return ans
