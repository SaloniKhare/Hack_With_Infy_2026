# ======================================================
# TWO SUM (SORTED ARRAY) - ALL APPROACHES
# ======================================================

# Problem:
# Given a sorted array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# Each input has exactly one solution.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def twoSum(self, nums, target):

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]


# ------------------------------------------------------
# 2️⃣ Binary Search
# ------------------------------------------------------

class BinarySearchSolution:

    def binary_search(self, nums, left, right, target):

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1


    def twoSum(self, nums, target):

        n = len(nums)

        for i in range(n):

            complement = target - nums[i]

            idx = self.binary_search(nums, i + 1, n - 1, complement)

            if idx != -1:
                return [i, idx]

        return [-1, -1]


# ------------------------------------------------------
# 3️⃣ Hash Map
# ------------------------------------------------------

class HashMapSolution:

    def twoSum(self, nums, target):

        hashmap = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i

        return [-1, -1]


# ------------------------------------------------------
# 4️⃣ Two Pointer (Optimal for Sorted Array)
# ------------------------------------------------------

class TwoPointerSolution:

    def twoSum(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left < right:

            s = nums[left] + nums[right]

            if s == target:
                return [left, right]

            elif s < target:
                left += 1

            else:
                right -= 1

        return [-1, -1]


# ------------------------------------------------------
# 5️⃣ Two Pointer (Return 1-Indexed Answer - LeetCode 167)
# ------------------------------------------------------

class TwoPointerLeetCodeSolution:

    def twoSum(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left < right:

            s = nums[left] + nums[right]

            if s == target:
                return [left + 1, right + 1]

            elif s < target:
                left += 1

            else:
                right -= 1
