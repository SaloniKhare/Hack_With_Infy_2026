# ======================================================
# BEST TIME TO BUY AND SELL STOCK (LeetCode 121)
# ======================================================

# Problem:
# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.
# You want to maximize profit by choosing ONE day to buy
# and ONE later day to sell.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit


# ------------------------------------------------------
# 2️⃣ Prefix Minimum (Track Minimum Price)
# ------------------------------------------------------

class PrefixMinSolution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


# ------------------------------------------------------
# 3️⃣ Dynamic Programming
# ------------------------------------------------------

class DPSolution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price)

        return dp[-1]


# ------------------------------------------------------
# 4️⃣ Kadane’s Algorithm (Transform to Max Subarray)
# ------------------------------------------------------

class KadaneSolution:
    def maxProfit(self, prices):
        max_profit = 0
        current = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            current = max(0, current + diff)
            max_profit = max(max_profit, current)

        return max_profit


# ------------------------------------------------------
# 5️⃣ Optimal Greedy ⭐
# ------------------------------------------------------

class GreedySolution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
