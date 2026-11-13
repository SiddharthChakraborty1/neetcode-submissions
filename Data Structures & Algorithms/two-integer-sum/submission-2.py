class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            var = nums[i]
            if var in mapper:
                return [mapper[var], i]

            mapper[target-var] = i