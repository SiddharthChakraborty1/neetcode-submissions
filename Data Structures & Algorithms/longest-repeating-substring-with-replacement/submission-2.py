class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len = 0
        max_freq = 0
        freq = {}
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            if(right - left + 1) - max_freq <= k:
                # valid window
                # freq[s[right]] = freq.get(s[right], 0) + 1
                # max_freq = max(max_freq, freq[s[right]])
                max_len = max(max_len, right - left + 1)
            else:
                # not a valid window
                # we will move left
                freq[s[left]]-=1
                left += 1
            
            right += 1
        
        return max_len
