
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = {}
        freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        window_size = len(s1)
        l, r = 0, 0
        while r < len(s2):
            freq[s2[r]] = freq.get(s2[r], 0) + 1
            if r-l+1 > window_size:
                freq[s2[l]] = freq.get(s2[l]) - 1
                l += 1
            
            if r-l+1 == window_size:
                if all([s1_freq.get(char) == freq.get(char) for char in s1_freq]):
                    return True

            r += 1
        
        return False


