class Solution:

    def encode(self, strs):
        encoded_string = ""
        for word in strs:
            encoded_string+= f"{len(word)}#{word}"
        
        return encoded_string

    def decode(self, s):
        i = 0
        all_strings = []
        while i < len(s):
            current_number = ""
            while s[i] != "#":
                current_number += s[i]
                i += 1
        
            current_number = int(current_number)
            current_string = ""
            j = i +1
            while j <= i + current_number:
                current_string += s[j]
                j += 1
        
            all_strings.append(current_string)
            i = j
        
        return all_strings

