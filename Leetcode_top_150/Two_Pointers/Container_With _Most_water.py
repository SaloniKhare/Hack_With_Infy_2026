# ======================================================
# CONTAINER WITH MOST WATER - ALL APPROACHES
# ======================================================

# Problem (LeetCode 11):
# Given n non-negative integers height[i] where each represents
# a vertical line, find two lines that together with the x-axis
# form a container such that the container contains the most water.
#
# Formula:
# area = min(height[left], height[right]) * (right - left)


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def maxArea(self, height):

        n = len(height)
        max_water = 0

        for i in range(n):
            for j in range(i + 1, n):

                width = j - i
                h = min(height[i], height[j])
                area = width * h

                max_water = max(max_water, area)

        return max_water


# ------------------------------------------------------
# 2️⃣ Optimized Brute Force (Small Pruning)
# ------------------------------------------------------

class OptimizedBruteForceSolution:
    def maxArea(self, height):

        n = len(height)
        max_water = 0

        for i in range(n):

            for j in range(n - 1, i, -1):

                width = j - i
                h = min(height[i], height[j])
                area = width * h

                max_water = max(max_water, area)

        return max_water


# ------------------------------------------------------
# 3️⃣ Two Pointer (Optimal Solution)
# ------------------------------------------------------

class TwoPointerSolution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:

            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_water = max(max_water, area)

            # Move the smaller height pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
