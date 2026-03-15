# ======================================================
# 3SUM - ALL APPROACHES
# ======================================================

# Problem (LeetCode 15):
# Given an integer array nums, return all unique triplets
# [nums[i], nums[j], nums[k]] such that:
#
# nums[i] + nums[j] + nums[k] == 0
#
# The solution set must not contain duplicate triplets.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def threeSum(self, nums):

        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):

                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)

        return list(result)


# ------------------------------------------------------
# 2️⃣ Hash Set (Fix One Element)
# ------------------------------------------------------

class HashSetSolution:
    def threeSum(self, nums):

        n = len(nums)
        result = set()

        for i in range(n):

            seen = set()

            for j in range(i+1, n):

                complement = -nums[i] - nums[j]

                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(triplet)

                seen.add(nums[j])

        return list(result)


# ------------------------------------------------------
# 3️⃣ Sorting + Two Pointer (Optimal)
# ------------------------------------------------------

class TwoPointerSolution:
    def threeSum(self, nums):

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):

            # Skip duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return result
