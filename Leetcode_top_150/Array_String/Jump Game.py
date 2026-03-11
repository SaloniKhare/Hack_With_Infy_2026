# ======================================================
# JUMP GAME - ALL APPROACHES
# ======================================================

# Problem (LeetCode 55):
# Given an array nums where nums[i] represents the
# maximum jump length from that position,
# determine if you can reach the last index.


# ------------------------------------------------------
# 1️⃣ Brute Force (Recursion)
# ------------------------------------------------------

class RecursionSolution:
    def canJump(self, nums):

        def dfs(index):
            if index >= len(nums) - 1:
                return True

            max_jump = nums[index]

            for step in range(1, max_jump + 1):
                if dfs(index + step):
                    return True

            return False

        return dfs(0)


# ------------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# ------------------------------------------------------

class MemoizationSolution:
    def canJump(self, nums):
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if i in memo:
                return memo[i]

            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)


# ------------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# ------------------------------------------------------

class TabulationSolution:
    def canJump(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = True

        return dp[n - 1]


# ------------------------------------------------------
# 4️⃣ Greedy (Forward Reach Tracking) ⭐ Optimal
# ------------------------------------------------------

class GreedySolution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True


# ------------------------------------------------------
# 5️⃣ Greedy (Backward Goal Post)
# ------------------------------------------------------

class BackwardGreedySolution:
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
