from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[left] <= nums[mid]: # This means the left part of the array is sorted
                    if nums[left] <= target and nums[mid] >= target:
                        # search in the left part
                        right = mid - 1
                    else:
                        # search in the right part
                        left = mid + 1
                    pass
                else: # this means the right part of the array is sorted
                    if nums[mid] <= target and target <= nums[right]:
                        # search in the right part of the array
                        left = mid + 1
                    else:
                        # search in the left part of the array
                        right = mid - 1
        
        return -1