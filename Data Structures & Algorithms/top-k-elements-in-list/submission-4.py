from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tracker = Counter(nums)
        result = [[] for i in range(max(count_tracker.values())+1)]
        for number, frequency in count_tracker.items():
            result[frequency].append(number)
        
        data = []
        for frequency in range(len(result)-1, 0 , -1):
            for num in result[frequency]:
                data.append(num)
            
            if len(data) == k:
                return data
        