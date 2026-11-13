class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # so the idea  is that first we will use the slow and fast pointer approach
        # to make sure slow pointer ends up somewhere inside the cycle
        # Then we will again start one from zero and one from start
        # then once the slow and slow2 pointer become equal that means the duplicate numbner is there
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # when we do this, we ensure slow has come inside the cycle
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        # Once the above become equal, this means that slow is now at the duplicate element
        return slow 