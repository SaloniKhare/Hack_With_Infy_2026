# ======================================================
# LONGEST CONSECUTIVE SEQUENCE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 128):
# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
#
# Must solve in O(n) time.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def longestConsecutive(self, nums):

        longest = 0

        for num in nums:

            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

        return longest


# ------------------------------------------------------
# 2️⃣ Sorting
# ------------------------------------------------------

class SortingSolution:
    def longestConsecutive(self, nums):

        if not nums:
            return 0

        nums.sort()

        longest = 1
        curr = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]:
                continue

            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1

        return max(longest, curr)


# ------------------------------------------------------
# 3️⃣ HashSet (Optimal)
# ------------------------------------------------------

class HashSetSolution:
    def longestConsecutive(self, nums):

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # start of sequence
            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

