# ======================================================
# JUMP GAME II - ALL APPROACHES
# ======================================================

# Problem (LeetCode 45):
# Given nums where nums[i] is the maximum jump length
# from that position, return the minimum number of
# jumps required to reach the last index.


# ------------------------------------------------------
# 1️⃣ Brute Force (Recursion)
# ------------------------------------------------------

class RecursionSolution:
    def jump(self, nums):

        def dfs(i):
            if i >= len(nums) - 1:
                return 0

            ans = float('inf')

            for step in range(1, nums[i] + 1):
                ans = min(ans, 1 + dfs(i + step))

            return ans

        return dfs(0)


# ------------------------------------------------------
# 2️⃣ Memoization (Top Down DP)
# ------------------------------------------------------

class MemoizationSolution:
    def jump(self, nums):
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0

            if i in memo:
                return memo[i]

            ans = float('inf')

            for step in range(1, nums[i] + 1):
                ans = min(ans, 1 + dfs(i + step))

            memo[i] = ans
            return ans

        return dfs(0)


# ------------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# ------------------------------------------------------

class TabulationSolution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]


# ------------------------------------------------------
# 4️⃣ Greedy (Level BFS Style)
# ------------------------------------------------------

class GreedyLevelSolution:
    def jump(self, nums):
        jumps = 0
        left = right = 0

        while right < len(nums) - 1:
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            jumps += 1

        return jumps


# ------------------------------------------------------
# 5️⃣ Optimal Greedy ⭐
# ------------------------------------------------------

class GreedyOptimalSolution:
    def jump(self, nums):
        jumps = 0
        farthest = 0
        end = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest

        return jumps
