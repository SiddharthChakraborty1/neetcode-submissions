class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = int((l+r)/2)
            if l==r:
                return nums[l]
            elif nums[mid]>nums[r]:
                l=mid+1
                continue
            elif nums[mid]<nums[r]:
                r = mid
                continue
        