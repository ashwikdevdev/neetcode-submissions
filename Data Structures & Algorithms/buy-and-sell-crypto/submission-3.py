class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        max_profit = 0
        buy = prices[0]

        # Start the loop directly from the second element
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price - buy > max_profit: # 'elif' saves a check if a new minimum buy price was just found
                max_profit = price - buy

        return max_profit
