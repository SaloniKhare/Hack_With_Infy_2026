# ======================================================
# MINIMUM SIZE SUBARRAY SUM - ALL APPROACHES
# ======================================================

# Problem (LeetCode 209):
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is >= target.
# If there is no such subarray, return 0.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def minSubArrayLen(self, target, nums):

        n = len(nums)
        min_len = float('inf')

        for i in range(n):

            current_sum = 0

            for j in range(i, n):

                current_sum += nums[j]

                if current_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break

        return 0 if min_len == float('inf') else min_len


# ------------------------------------------------------
# 3️⃣ Sliding Window (Optimal)
# ------------------------------------------------------

class SlidingWindowSolution:
    def minSubArrayLen(self, target, nums):

        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:

                min_len = min(min_len, right - left + 1)

                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

print(SlidingWindowSolution().minSubArrayLen(target, nums))
