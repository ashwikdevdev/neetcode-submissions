class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current = 0
        buy = prices[0]

        for price in prices:
            if price < buy:
                buy = price
            current = price - buy
            if max_profit < current:
                max_profit = current

        return max_profit