# ======================================================
# SUMMARY RANGES - ALL APPROACHES
# ======================================================

# Problem (LeetCode 228):
# Given a sorted unique integer array nums,
# return the smallest list of ranges that cover all numbers.
#
# Example:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]


# ------------------------------------------------------
# 1️⃣ Brute Force (Check Each Range)
# ------------------------------------------------------

class BruteForceSolution:
    def summaryRanges(self, nums):

        result = []
        n = len(nums)
        i = 0

        while i < n:

            j = i

            while j + 1 < n and nums[j+1] == nums[j] + 1:
                j += 1

            if i == j:
                result.append(str(nums[i]))
            else:
                result.append(f"{nums[i]}->{nums[j]}")

            i = j + 1

        return result


# ------------------------------------------------------
# 2️⃣ Two Pointer (Cleaner)
# ------------------------------------------------------

class TwoPointerSolution:
    def summaryRanges(self, nums):

        result = []

        start = 0

        for i in range(len(nums)):

            # end of range
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:

                if start == i:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i]}")

                start = i + 1

        return result


# ------------------------------------------------------
# 3️⃣ Iterative with Tracking Variables
# ------------------------------------------------------

class IterativeSolution:
    def summaryRanges(self, nums):

        result = []

        if not nums:
            return result

        start = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):

            if nums[i] != prev + 1:
                if start == prev:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{prev}")

                start = nums[i]

            prev = nums[i]

        # last range
        if start == prev:
            result.append(str(start))
        else:
            result.append(f"{start}->{prev}")

        return result


# ------------------------------------------------------
# Example
# ------------------------------------------------------

nums = [0,1,2,4,5,7]

print(BruteForceSolution().summaryRanges(nums))
print(TwoPointerSolution().summaryRanges(nums))
print(IterativeSolution().summaryRanges(nums))
