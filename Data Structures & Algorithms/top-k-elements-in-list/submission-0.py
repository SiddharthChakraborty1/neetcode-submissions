class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasher = {}
        for num in nums:
            if num in hasher:
                hasher[num] += 1
            else:
                hasher[num] = 1
        
        counter =[[] for i in range(len(nums) +1)]
        
        for num, count in hasher.items():
            counter[count].append(num)
        
        res = []
        for i in range(len(counter)-1, 0, -1):
            for num in counter[i]:
                res.append(num)
                if len(res) == k:
                    return res

            
            
            

        

        
        
        