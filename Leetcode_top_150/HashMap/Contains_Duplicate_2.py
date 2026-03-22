# ======================================================
# CONTAINS DUPLICATE II - ALL APPROACHES
# ======================================================

# Problem (LeetCode 219):
# Given an array nums and an integer k,
# return True if there are two distinct indices i and j
# such that nums[i] == nums[j] and abs(i - j) <= k.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def containsNearbyDuplicate(self, nums, k):

        n = len(nums)

        for i in range(n):
            for j in range(i+1, min(i+k+1, n)):
                if nums[i] == nums[j]:
                    return True

        return False


# ------------------------------------------------------
# 2️⃣ HashMap (Store Last Seen Index)
# ------------------------------------------------------

class HashMapSolution:
    def containsNearbyDuplicate(self, nums, k):

        index_map = {}

        for i, num in enumerate(nums):

            if num in index_map:
                if i - index_map[num] <= k:
                    return True

            index_map[num] = i

        return False


# ------------------------------------------------------
# 3️⃣ Sliding Window with Set
# ------------------------------------------------------

class SlidingWindowSolution:
    def containsNearbyDuplicate(self, nums, k):

        window = set()

        for i in range(len(nums)):

            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False
