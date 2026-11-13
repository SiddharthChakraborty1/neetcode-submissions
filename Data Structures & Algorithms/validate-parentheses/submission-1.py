class Solution:
    
    def isValid(self, brackets: str):
        stack = []
        bracket_pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
            ">": "<"
        }
        opening_brackets = bracket_pairs.values()
        closing_brackets = bracket_pairs.keys()
        
        for bracket in brackets:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets:
                if stack and stack[-1] == bracket_pairs.get(bracket):
                    stack.pop()
                else:
                    stack.append(bracket)
        
        return len(stack) == 0
