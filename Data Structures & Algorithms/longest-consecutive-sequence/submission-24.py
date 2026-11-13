class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        max_length = 0

        if not nums: return 0

        for num in nums:
            if (num - 1) not in nums:
                length = 1
                while (num + length) in nums:
                    length += 1
                max_length = max(length, max_length)

        return max_length