class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        
        for num in nums:
            if num == 0 and zero_count < 1:
                zero_count += 1
                continue
            if num == 0 and zero_count > 0:
                zero_count += 1
                product = 0
                break
            else:
                product *= num
        
        if product == 0:
            return [0]*len(nums)

        if zero_count == 1:
            return [0 if num != 0 else product for num in nums]
        
        return [int(product/num) for num in nums]

        