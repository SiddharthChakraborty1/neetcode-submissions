class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = [0]*26
        a2 = [0]*26
        for char in s:
            a1[ord(char) - ord('a')] +=1
        
        for char in t:
            a2[ord(char) - ord('a')] += 1
        
        return a1 == a2

        