class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Understand
        # Same number/kind of letter, but diff order
        # Empty string? probably return true
        # String of different length = false
        
        if len(s) != len(t):
            return False
        else:
            lst_s = [0] * 26
            lst_t = [0] * 26
            
            for character in s:
                lst_s[ord(character)-ord('a')] += 1
            
            for character in t:
                lst_t[ord(character)-ord('a')] += 1
                
            for i in range(0, 26):
                if lst_s[i] != lst_t[i]:
                    return False
        
            return True
