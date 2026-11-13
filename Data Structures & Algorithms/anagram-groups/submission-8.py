class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        # for word in strs:
        #     sorted_word = sorted(word)
        #     if tuple(sorted_word) in mapper:
        #         mapper[tuple(sorted_word)].append(word)
        #     else:
        #         mapper[tuple(sorted_word)] = [word]
        
        # return [v for k, v in mapper.items()]
        for word in strs:
            count = [0]*26
            for j in word:
                count[ord(j)-ord('a')] +=1
            
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(word)
        return list(res.values())
                