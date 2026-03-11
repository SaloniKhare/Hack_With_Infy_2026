# ======================================================
# REMOVE ELEMENT - ALL APPROACHES
# ======================================================

# Problem (LeetCode 27):
# Remove all occurrences of val in-place and return
# the number of remaining elements.
# The order of elements may change.


# ------------------------------------------------------
# 1️⃣ Brute Force (Using New Array)
# ------------------------------------------------------

class BruteForceSolution:
    def removeElement(self, nums, val):
        arr = []

        for num in nums:
            if num != val:
                arr.append(num)

        for i in range(len(arr)):
            nums[i] = arr[i]

        return len(arr)


# ------------------------------------------------------
# 2️⃣ Two Pointer (Forward Write Pointer)
# ------------------------------------------------------

class TwoPointerSolution:
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# ------------------------------------------------------
# 3️⃣ Two Pointer (Swap With Last)
# ------------------------------------------------------

class SwapWithEndSolution:
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n


# ------------------------------------------------------
# 4️⃣ Pythonic Solution
# ------------------------------------------------------

class PythonicSolution:
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)
