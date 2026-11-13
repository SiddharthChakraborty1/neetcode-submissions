class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq_s1 = {}
        for char in s1:
            if char in freq_s1:
                freq_s1[char] += 1
            else:
                freq_s1[char] = 1
        
        substring_length = len(s1)
        left, right = 0, 0
        freq_s2 = {}
        while right < len(s2):
            current_char = s2[right]
            if right - left + 1 > substring_length:
                if s2[left] in freq_s2:
                    if freq_s2[s2[left]] - 1 == 0:
                        freq_s2.pop(s2[left])
                    else:
                        freq_s2[s2[left]] -=1
                left += 1

            if current_char in freq_s2:
                freq_s2[current_char] +=1
            else:
                freq_s2[current_char] = 1

            if freq_s1 == freq_s2:
                return True
            
            right += 1

        return False


