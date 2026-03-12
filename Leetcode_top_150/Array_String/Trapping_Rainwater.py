# ======================================================
# TRAPPING RAIN WATER - ALL APPROACHES
# ======================================================

# Problem (LeetCode 42):
# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water
# it can trap after raining.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def trap(self, height):
        n = len(height)
        water = 0

        for i in range(n):
            left_max = max(height[:i+1])
            right_max = max(height[i:])

            water += min(left_max, right_max) - height[i]

        return water


# ------------------------------------------------------
# 2️⃣ Prefix & Suffix Arrays
# ------------------------------------------------------

class PrefixSuffixSolution:
    def trap(self, height):
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water


# ------------------------------------------------------
# 3️⃣ Dynamic Programming (Single Pass Precompute)
# ------------------------------------------------------

class DPSolution:
    def trap(self, height):
        n = len(height)

        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - height[i]

        return res


# ------------------------------------------------------
# 4️⃣ Monotonic Stack
# ------------------------------------------------------

class StackSolution:
    def trap(self, height):
        stack = []
        water = 0

        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[bottom]

                water += distance * bounded_height

            stack.append(i)

        return water


# ------------------------------------------------------
# 5️⃣ Two Pointer (Optimal) ⭐
# ------------------------------------------------------

class TwoPointerSolution:
    def trap(self, height):

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
