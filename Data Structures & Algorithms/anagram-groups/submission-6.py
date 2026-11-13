from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for word in strs:
            sorted_word = sorted(word)
            if tuple(sorted_word) in mapper:
                mapper[tuple(sorted_word)].append(word)
            else:
                mapper[tuple(sorted_word)] = [word]
        
        return [v for k, v in mapper.items()]