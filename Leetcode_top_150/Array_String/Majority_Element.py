# ======================================================
# MAJORITY ELEMENT - ALL APPROACHES
# ======================================================

# Problem (LeetCode 169):
# Given an array nums of size n, return the majority element.
# Majority element = element that appears more than n//2 times.


# ------------------------------------------------------
# 1️⃣ Brute Force (Count Each Element)
# ------------------------------------------------------

class BruteForceSolution:
    def majorityElement(self, nums):
        n = len(nums)

        for num in nums:
            if nums.count(num) > n // 2:
                return num


# ------------------------------------------------------
# 2️⃣ Hash Map / Dictionary
# ------------------------------------------------------

class HashMapSolution:
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if freq[num] > len(nums) // 2:
                return num


# ------------------------------------------------------
# 3️⃣ Sorting Approach
# ------------------------------------------------------

class SortingSolution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


# ------------------------------------------------------
# 4️⃣ Divide and Conquer
# ------------------------------------------------------

class DivideConquerSolution:
    def majorityElement(self, nums):

        def majority(l, r):
            if l == r:
                return nums[l]

            mid = (l + r) // 2

            left = majority(l, mid)
            right = majority(mid + 1, r)

            if left == right:
                return left

            left_count = nums[l:r+1].count(left)
            right_count = nums[l:r+1].count(right)

            return left if left_count > right_count else right

        return majority(0, len(nums) - 1)


# ------------------------------------------------------
# 5️⃣ Boyer-Moore Voting Algorithm ⭐ Optimal
# ------------------------------------------------------

class BoyerMooreSolution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
