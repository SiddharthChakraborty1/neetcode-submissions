class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        max_profit = 0
        start = 0
        end = start+1
        while end < len(prices):
            profit = prices[end] - prices[start]
            max_profit = max(max_profit, profit)
            if profit <= 0:
                start = end
                end = end + 1
                continue
            
            end += 1
        
        return max_profit

