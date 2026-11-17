class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tracker = {

        }
        for num in nums:
            if num in count_tracker:
                count_tracker[num]+=1
            else:
                count_tracker[num] = 1
        
        result = [[] for _ in range(max(count_tracker.values())+1)]
        for num, frequency in count_tracker.items():
            result[frequency].append(num)
        
        output = []
        for i in range(len(result)-1, -1, -1):
            for val in result[i]:
                output.append(val)
                if len(output) == k:
                    return output


        

        