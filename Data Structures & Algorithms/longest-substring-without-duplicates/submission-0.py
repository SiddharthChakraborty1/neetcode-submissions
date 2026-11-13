class Solution:

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        left = 0
        max_len = 0
        char_index_mapper = defaultdict()
        for right in range(len(s)):
            if s[right] in char_index_mapper and char_index_mapper[s[right]] >= left:
                left = char_index_mapper[s[right]] + 1
            
            char_index_mapper[s[right]] = right
            max_len = max((right-left+1), max_len)
        
        return max_len                
