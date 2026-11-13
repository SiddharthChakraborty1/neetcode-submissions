class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hasher:
                return [hasher[remainder], i]
            else:
                hasher[nums[i]] = i
        
        