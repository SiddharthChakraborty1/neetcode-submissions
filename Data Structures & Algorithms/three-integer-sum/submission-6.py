from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        total_length = len(nums)
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            j = i+1
            k = total_length-1
            while j < k:
                current_sum = nums[j] + nums[k] + a
                if current_sum  == 0:
                    res.append((a, nums[j], nums[k]))
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif current_sum > 0:
                    k -= 1
                elif current_sum < 0:
                    j += 1
                

        return res

