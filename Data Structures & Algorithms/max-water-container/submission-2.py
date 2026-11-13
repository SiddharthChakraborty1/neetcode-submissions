class Solution:
    
    def maxArea(self, nums):
        
        max_vol = 0
        l, r = 0, len(nums)-1
        while l < r:
            length = r - l
            height = nums[r] if nums[r] < nums[l] else nums[l]
            vol = length*height
            if vol > max_vol:
                max_vol = vol
            
            if nums[l] > nums[r]:
                r -= 1
            else:
                l += 1
        
        return max_vol
