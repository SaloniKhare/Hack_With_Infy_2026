# ======================================================
# MAXIMUM SUM CIRCULAR SUBARRAY (LeetCode 918)
# ======================================================

# Problem:
# Given a circular integer array nums (i.e., the next element
# of nums[n-1] is nums[0]), return the maximum possible sum
# of a non-empty subarray.


# ------------------------------------------------------
# 1️⃣ Brute Force (Try All Circular Subarrays)
# ------------------------------------------------------

class BruteForceSolution:
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            current_sum = 0
            for j in range(n):
                current_sum += nums[(i + j) % n]
                max_sum = max(max_sum, current_sum)

        return max_sum


# ------------------------------------------------------
# 2️⃣ Better Approach (Extend Array)
# ------------------------------------------------------

class ExtendedArraySolution:
    def maxSubarraySumCircular(self, nums):
        arr = nums + nums
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            current_sum = 0
            for j in range(i, i + n):
                current_sum += arr[j]
                max_sum = max(max_sum, current_sum)

        return max_sum


# ------------------------------------------------------
# 3️⃣ Kadane for Max Subarray (Non-Circular)
# ------------------------------------------------------

class KadaneNormal:
    def kadane(self, nums):
        current = max_sum = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            max_sum = max(max_sum, current)

        return max_sum


# ------------------------------------------------------
# 4️⃣ Kadane for Min Subarray
# ------------------------------------------------------

class KadaneMin:
    def kadane_min(self, nums):
        current = min_sum = nums[0]

        for i in range(1, len(nums)):
            current = min(nums[i], current + nums[i])
            min_sum = min(min_sum, current)

        return min_sum


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Kadane + Circular Trick)
# ------------------------------------------------------

class OptimalSolution:
    def maxSubarraySumCircular(self, nums):
        total_sum = sum(nums)

        # Standard Kadane (max subarray)
        current_max = max_sum = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_sum = max(max_sum, current_max)

        # Kadane for min subarray
        current_min = min_sum = nums[0]
        for i in range(1, len(nums)):
            current_min = min(nums[i], current_min + nums[i])
            min_sum = min(min_sum, current_min)

        # Edge case: all elements are negative
        if max_sum < 0:
            return max_sum

        # Circular max = total_sum - min_subarray
        return max(max_sum, total_sum - min_sum)


