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


# ------------------------------------------------------
# 4️⃣ Union-Find (Advanced)
# ------------------------------------------------------

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if x not in self.parent or y not in self.parent:
            return

        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]


class UnionFindSolution:
    def longestConsecutive(self, nums):

        uf = UnionFind()

        for num in nums:
            uf.add(num)

        for num in nums:
            if num + 1 in uf.parent:
                uf.union(num, num + 1)

        return max(uf.size.values()) if uf.size else 0


# ------------------------------------------------------
# Example
# ------------------------------------------------------

nums = [100,4,200,1,3,2]

print(BruteForceSolution().longestConsecutive(nums))
print(SortingSolution().longestConsecutive(nums))
print(HashSetSolution().longestConsecutive(nums))
print(UnionFindSolution().longestConsecutive(nums))
