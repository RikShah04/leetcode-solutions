"""
Problem: Leetcode 121 Best Time to Buy and Sell Stock

Intuition: A single day's max profit would simply be its price minus the min price seen so far.
           To find the overall max profit, we track the min value seen so far, and in each iteration over the price array
           we compute the day's max profit, then see if it is better than the best profit seen so far,
           then update the min if the current day's price is lower. We compute profit before updating the min so that
           the min always reflects a day strictly before (or equal to) the current one, keeping buy before sell.

Time Complexity: O(n) where n is the length of the array, we iterate over each element once.

Space Complexity: O(1), only one variable outside of result is tracked

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        profit = 0

        for price in prices:
            profit = max(profit, price - currMin)
            currMin = min(currMin, price)
        return profit