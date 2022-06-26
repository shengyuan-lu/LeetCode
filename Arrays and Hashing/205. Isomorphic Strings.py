class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_pair_dict_a = dict()
        char_pair_dict_b = dict()
        
        len_s = len(s)
        
        len_t = len(t)
        
        if len_s != len_t:
            return False
        else:
            for i in range(0, len_s):
                if s[i] not in char_pair_dict_a.keys():
                    char_pair_dict_a[s[i]] = t[i]
                else:
                    if t[i] != char_pair_dict_a[s[i]]:
                        return False
            
            for i in range(0, len_t):
                if t[i] not in char_pair_dict_b.keys():
                    char_pair_dict_b[t[i]] = s[i]
                else:
                    if s[i] != char_pair_dict_b[t[i]]:
                        return False
                    
        return True
