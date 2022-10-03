# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity O(N) Space complexity O(1)
        mini = 10**4
        profit = 0
        
        for price in prices:
            if price < mini:
                mini = price
            profit = max(profit, price - mini)
        return profit
