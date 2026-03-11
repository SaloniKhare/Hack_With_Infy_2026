# ======================================================
# REMOVE DUPLICATES FROM SORTED ARRAY II - ALL APPROACHES
# ======================================================

# Problem (LeetCode 80):
# Given a sorted array nums, remove duplicates in-place
# such that each element appears at most TWICE.
# Return the number of elements kept (k).


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Hash Map)
# ------------------------------------------------------

class BruteForceSolution:
    def removeDuplicates(self, nums):
        from collections import defaultdict

        freq = defaultdict(int)
        arr = []

        for num in nums:
            if freq[num] < 2:
                arr.append(num)
                freq[num] += 1

        for i in range(len(arr)):
            nums[i] = arr[i]

        return len(arr)


# ------------------------------------------------------
# 2️⃣ Extra Array Approach
# ------------------------------------------------------

class ExtraArraySolution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        arr = nums[:2]

        for i in range(2, len(nums)):
            if nums[i] != arr[-2]:
                arr.append(nums[i])

        for i in range(len(arr)):
            nums[i] = arr[i]

        return len(arr)


# ------------------------------------------------------
# 3️⃣ Two Pointer (Optimal) ⭐
# ------------------------------------------------------

class TwoPointerSolution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k


# ------------------------------------------------------
# 4️⃣ Slow-Fast Pointer Variation
# ------------------------------------------------------

class SlowFastPointerSolution:
    def removeDuplicates(self, nums):
        slow = 0

        for num in nums:
            if slow < 2 or num != nums[slow - 2]:
                nums[slow] = num
                slow += 1

        return slow


# ------------------------------------------------------
# 5️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def removeDuplicates(self, nums):
        from collections import Counter

        count = Counter(nums)
        arr = []

        for num in nums:
            if count[num] > 0:
                arr.append(num)
                count[num] -= 1
                if count[num] == max(0, count[num] - 1):
                    count[num] = 0

        nums[:] = arr
        return len(nums)
