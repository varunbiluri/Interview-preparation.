class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        low = prices[0]
        
        for price in prices:
            low = min(low, price)
            result = max(result, price - low)
        
        return result