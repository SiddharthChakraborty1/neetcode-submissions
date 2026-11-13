class Solution:
    
    
    def twoSum(self, arr: list, target: int):
        l = 0
        r = len(arr) - 1
        
        while l < r:
            total = arr[l] + arr[r]
            if total > target:
                r -= 1
            
            elif total < target:
                l += 1
            
            elif total == target:
                return [l+1, r+1]
        
        return None

        
            