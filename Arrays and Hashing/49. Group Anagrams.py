class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each word, establish a anagram profile
        # dict string (anagram profile):list
        # compare the anagram profile, if known, add to the set, if not, establish a new anagram profile
        
        hash_table = dict()
        
        for string in strs:
            ana_profile = ''.join(sorted(string))
            
            if ana_profile in hash_table.keys():
                hash_table[ana_profile].append(string)
            else:
                hash_table[ana_profile] = list()
                hash_table[ana_profile].append(string)
        
        rtr_list = list()
        
        for i, (k, v) in enumerate(hash_table.items()):
            rtr_list.append(v)
        
        return rtr_list
