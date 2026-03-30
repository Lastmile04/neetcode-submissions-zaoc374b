class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for n in prices:
            min_price = min(min_price, n)
            profit = n - min_price
            max_profit = max(profit, max_profit)
        return max_profit