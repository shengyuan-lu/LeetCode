class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        right_ptr = len(numbers) - 1
        
        for i in range(0, len(numbers)):
            remaining = target - numbers[i]
            
            while True:
                right_num = numbers[right_ptr]
                
                if right_num == remaining:
                    return [i+1 , right_ptr+1]
                elif right_num < remaining:
                    break
                else:
                    right_ptr -= 1
