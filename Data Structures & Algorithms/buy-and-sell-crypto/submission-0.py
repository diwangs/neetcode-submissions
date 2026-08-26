class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        bottom = float('inf')
        for idx, price in enumerate(prices):
            if idx == 0:
                bottom = price
            else:
                if price < bottom:
                    bottom = price
                if price - bottom > maxDiff:
                    maxDiff = price - bottom
        return maxDiff