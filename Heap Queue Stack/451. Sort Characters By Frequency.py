class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = dict()
        
        for c in s:
            if ord(c) in freq_dict.keys():
                freq_dict[ord(c)] += 1
            else:
                freq_dict[ord(c)] = 1
                
        res_str = ''
        
        srted = sorted(list(freq_dict.items()), key = lambda x:-x[1])
        
        print(srted)
        
        for element in srted:
            res_str += chr(element[0])*element[1]
            
        return res_str
        
