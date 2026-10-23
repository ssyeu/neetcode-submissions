class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = []
        while i < len(prices) - 1: 
            j = len(prices) - 1
            while j > i:
                profit.append(prices[j] - prices[i])
                j -= 1
            i += 1
        if profit and max(profit) > 0:
            return max(profit)
        else:
            return 0
        