# ======================================================
# BEST TIME TO BUY AND SELL STOCK II - ALL APPROACHES
# ======================================================

# Problem (LeetCode 122):
# You may buy and sell the stock multiple times.
# However, you must sell the stock before buying again.


# ------------------------------------------------------
# 1️⃣ Brute Force (Recursion)
# ------------------------------------------------------

class RecursionSolution:
    def maxProfit(self, prices):

        def dfs(i, holding):
            if i == len(prices):
                return 0

            if holding:
                sell = prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                return max(sell, skip)
            else:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)
                return max(buy, skip)

        return dfs(0, False)


# ------------------------------------------------------
# 2️⃣ Memoization (Top Down DP)
# ------------------------------------------------------

class MemoizationSolution:
    def maxProfit(self, prices):
        memo = {}

        def dfs(i, holding):
            if i == len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                sell = prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                memo[(i, holding)] = max(sell, skip)
            else:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)
                memo[(i, holding)] = max(buy, skip)

            return memo[(i, holding)]

        return dfs(0, False)


# ------------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# ------------------------------------------------------

class TabulationSolution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            dp[i][1] = max(prices[i] + dp[i+1][0], dp[i+1][1])
            dp[i][0] = max(-prices[i] + dp[i+1][1], dp[i+1][0])

        return dp[0][0]


# ------------------------------------------------------
# 4️⃣ Space Optimized DP
# ------------------------------------------------------

class SpaceOptimizedSolution:
    def maxProfit(self, prices):
        ahead = [0,0]

        for i in range(len(prices)-1, -1, -1):
            curr = [0,0]
            curr[1] = max(prices[i] + ahead[0], ahead[1])
            curr[0] = max(-prices[i] + ahead[1], ahead[0])
            ahead = curr

        return ahead[0]


# ------------------------------------------------------
# 5️⃣ Greedy (Optimal Solution) ⭐
# ------------------------------------------------------

class GreedySolution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
