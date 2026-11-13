class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            ">": "<",
            "}": "{"
        }
        stack = []
        opening = pairs.values()
        closing = pairs.keys()
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    stack.append(char)
        
        return not bool(len(stack))
        