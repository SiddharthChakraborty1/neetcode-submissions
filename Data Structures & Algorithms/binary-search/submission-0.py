from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)

    def binary_search(self, nums, target, left=0, right=None):
        if right is None:
            right = len(nums) - 1
        
        if left > right:
            return -1
        
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, target, left, mid-1)
        else:
            return self.binary_search(nums, target, mid+1, right)
    