# ======================================================
# MAXIMUM SUBARRAY (LeetCode 53)
# ======================================================

# Problem:
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.


# ------------------------------------------------------
# 1️⃣ Brute Force (Check All Subarrays)
# ------------------------------------------------------

class BruteForceSolution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            for j in range(i, n):
                current_sum = sum(nums[i:j+1])
                max_sum = max(max_sum, current_sum)

        return max_sum


# ------------------------------------------------------
# 2️⃣ Better Approach (Prefix Sum)
# ------------------------------------------------------

class PrefixSumSolution:
    def maxSubArray(self, nums):
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        max_sum = float('-inf')

        for i in range(n):
            for j in range(i, n):
                current_sum = prefix[j+1] - prefix[i]
                max_sum = max(max_sum, current_sum)

        return max_sum


# ------------------------------------------------------
# 3️⃣ Dynamic Programming (Tabulation)
# ------------------------------------------------------

class DPSolution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum


# ------------------------------------------------------
# 4️⃣ Kadane’s Algorithm ⭐ (Optimal)
# ------------------------------------------------------

class KadaneSolution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


# ------------------------------------------------------
# 5️⃣ Follow-up: Return Subarray (Indices)
# ------------------------------------------------------

class KadaneWithIndices:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        start = end = temp_start = 0

        for i in range(1, len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                temp_start = i
            else:
                current_sum += nums[i]

            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i

        return max_sum, nums[start:end+1]
