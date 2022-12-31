"""
PROBLEM:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

EXAMPLE 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

EXAMPLE 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
 
CONSTRAINTS:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            else:
                maxProfit = max(prices[i] - buyPrice, maxProfit)
        
        return maxProfit


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    print("================================== CASE 1 ==================================")
    prices = [7, 1, 5, 3, 6, 4]
    result = solution.maxProfit(prices)
    print(f"Prices     = {prices}")
    print(f"Max Profit = {result}")
    print()

    # CASE 2
    print("================================== CASE 2 ==================================")
    prices = [7, 6, 4, 3, 1]
    result = solution.maxProfit(prices)
    print(f"Prices     = {prices}")
    print(f"Max Profit = {result}")
    print()

    # CASE 3
    print("================================== CASE 3 ==================================")
    prices = [2, 4, 1]
    result = solution.maxProfit(prices)
    print(f"Prices     = {prices}")
    print(f"Max Profit = {result}")
    print()
