class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_mapper = {}
        for num in nums:
            if num in frequency_mapper:
                frequency_mapper[num] = frequency_mapper[num] +1
                return True
            else:
                frequency_mapper[num] = 1
        
        return False

        
         