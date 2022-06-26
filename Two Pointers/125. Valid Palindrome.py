class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
        
        if len(lst) == 0:
            return True
        
        half_length = len(lst) // 2
        
        for i in range(0, half_length):
            if lst[i] != lst[-i-1]:
                return False
            
        return True
