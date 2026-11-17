from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in mapper:
                mapper[key].append(word)
            else:
                mapper[key] = [word]
        
        return [v for v in mapper.values()]