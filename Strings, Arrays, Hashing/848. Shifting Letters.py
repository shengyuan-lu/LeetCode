class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        shifts = list(reversed(shifts))
        
        # re-calculating shift amount
        for i in range(1, len(shifts)):
            shifts[i] = shifts[i] + shifts[i-1]
            
        shifts = list(reversed(shifts))
        
        rtr_str = ''
        
        for i, ch in enumerate(s):
            rtr_str += self.shift_helper(ch, shifts[i])
        
        return rtr_str
    
    
    def shift_helper(self, character, shift_amount) -> str:
        
        new_ord = (ord(character) - ord('a')) + shift_amount
        
        if new_ord > 26:
            new_ord = (new_ord % 26) + ord('a')
        else:
            new_ord += ord('a')
            
        return chr(new_ord)
