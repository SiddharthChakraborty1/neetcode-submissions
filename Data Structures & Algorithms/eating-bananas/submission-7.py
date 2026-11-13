import math
class Solution:
        def minEatingSpeed(self, piles: List[int], h: int) -> int:
                # left pointer will be 0
                # right pointer will be the legth of piles
                # for every mid value of the banana eating rate, calculate the actual time taken
                # Check if the time taken is smaller than the given hours
                # then return
                # since the logic to calculate time is going to be repeated, add it into a function
                # or we can just add it in the code

                left, right = 1, max(piles)
                result = right
                while left <= right:
                        mid = (left + right)//2
                        time_taken = self.get_hours(piles, mid)
                        if time_taken <= h:
                                result =mid
                                right = mid -1
        
                        else:
                                left = mid+ 1
        
                return result

                                
        
        def get_hours(self, piles, k):
                return sum(math.ceil(pile/k) for pile in piles)


# Note there is a catch, this can be the case that the calculated mid might work, but a value
# smaller than mid might also work. So make sure to understand the problem correctly before writing a solution