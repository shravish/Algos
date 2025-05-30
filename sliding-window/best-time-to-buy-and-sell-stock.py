def maxProfit(prices):
    if not prices:
        return 0
    min_profit = float('inf')
    max_profit = 0
    for price in prices:
        min_profit = min(min_profit, price)
        profit = price - min_profit
        max_profit = max(max_profit, profit)
    return max_profit
prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", maxProfit(prices))
# Output: Maximum Profit: 5
