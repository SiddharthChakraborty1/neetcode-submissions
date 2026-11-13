from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for word in strs:
            if tuple(sorted(word)) in mapper:
                mapper[tuple(sorted(word))].append(word)
            else:
                mapper[tuple(sorted(word))] = [word]
        
        return [v for k, v in mapper.items()]