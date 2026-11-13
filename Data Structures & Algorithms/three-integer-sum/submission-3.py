from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_set = set()
        nums.sort()
        total_length = len(nums)
        for i in range(total_length):
            j = i+1
            k = total_length-1
            while j < k:
                current_sum = nums[j] + nums[k] + nums[i]
                if current_sum  == 0:
                    triplet_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k-=1
                elif current_sum > 0:
                    k -= 1
                elif current_sum < 0:
                    j += 1
                

        return list(triplet_set)

