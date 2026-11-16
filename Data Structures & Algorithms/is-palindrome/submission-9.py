class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [char for char in s.lower() if char.isalnum()]
        l,r = 0, len(word)-1
        while l < r:
            if word[l] != word[r]:
                return False

            l += 1
            r -= 1
        
        return True