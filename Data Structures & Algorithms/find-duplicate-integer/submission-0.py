class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0
        slow = nums[idx]
        fast = nums[nums[idx]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

            
    