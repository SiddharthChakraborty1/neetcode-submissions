class Solution:
    
    def dailyTemperatures(self, temperatures):
        
        stack = []
        results = [0 for i in range(len(temperatures))]
        
        i = 0
        while i < len(temperatures):
            if not stack:
                stack.append((i, temperatures[i]))
            else:
                while stack and stack[-1][1] < temperatures[i]:
                    popped_index, _ = stack.pop()
                    results[popped_index] = i - popped_index

                stack.append((i, temperatures[i]))
            
            i += 1
        
        return results