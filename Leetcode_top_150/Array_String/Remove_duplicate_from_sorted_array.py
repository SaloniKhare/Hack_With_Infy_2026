# ======================================================
# REMOVE DUPLICATES FROM SORTED ARRAY - ALL APPROACHES
# ======================================================

# Problem (LeetCode 26):
# Given a sorted array nums, remove duplicates in-place
# such that each element appears only once.
# Return the number of unique elements (k).


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Set)
# ------------------------------------------------------

class BruteForceSolution:
    def removeDuplicates(self, nums):
        unique = sorted(set(nums))

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)


# ------------------------------------------------------
# 2️⃣ Extra Array Approach
# ------------------------------------------------------

class ExtraArraySolution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        arr = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                arr.append(nums[i])

        for i in range(len(arr)):
            nums[i] = arr[i]

        return len(arr)


# ------------------------------------------------------
# 3️⃣ Two Pointer (Optimal Solution) ⭐
# ------------------------------------------------------

class TwoPointerSolution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# ------------------------------------------------------
# 4️⃣ Slow-Fast Pointer Variation
# ------------------------------------------------------

class SlowFastPointerSolution:
    def removeDuplicates(self, nums):
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


# ------------------------------------------------------
# 5️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
