# ======================================================
# INSERT INTERVAL - ALL APPROACHES
# ======================================================

# Problem (LeetCode 57):
# You are given a list of non-overlapping intervals sorted by start time.
# Insert a new interval and merge if necessary.
#
# Example:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]


# ------------------------------------------------------
# 1️⃣ Brute Force (Insert + Sort + Merge)
# ------------------------------------------------------

class BruteForceSolution:
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        intervals.sort()

        result = [intervals[0]]

        for start, end in intervals[1:]:

            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result


# ------------------------------------------------------
# 2️⃣ Optimal Single Pass (Most Important)
# ------------------------------------------------------

class OptimalSolution:
    def insert(self, intervals, newInterval):

        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Step 3: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# ------------------------------------------------------
# 3️⃣ Using Stack
# ------------------------------------------------------

class StackSolution:
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        intervals.sort()

        stack = [intervals[0]]

        for interval in intervals[1:]:

            if stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)

        return stack


# ------------------------------------------------------
# 4️⃣ In-Place Modification
# ------------------------------------------------------

class InPlaceSolution:
    def insert(self, intervals, newInterval):

        intervals.append(newInterval)
        intervals.sort()

        index = 0

        for i in range(1, len(intervals)):

            if intervals[index][1] >= intervals[i][0]:
                intervals[index][1] = max(intervals[index][1], intervals[i][1])
            else:
                index += 1
                intervals[index] = intervals[i]

        return intervals[:index + 1]


# ------------------------------------------------------
# 5️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def insert(self, intervals, newInterval):

        intervals += [newInterval]
        intervals.sort()

        result = []

        for interval in intervals:

            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result


# ------------------------------------------------------
# 6️⃣ Binary Search Optimization (Advanced)
# ------------------------------------------------------

import bisect

class BinarySearchSolution:
    def insert(self, intervals, newInterval):

        starts = [i[0] for i in intervals]
        idx = bisect.bisect_left(starts, newInterval[0])

        intervals.insert(idx, newInterval)

        # Merge like normal
        result = [intervals[0]]

        for start, end in intervals[1:]:

            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result


# ------------------------------------------------------
# Example
# ------------------------------------------------------

intervals = [[1,3],[6,9]]
newInterval = [2,5]

print("BruteForce:", BruteForceSolution().insert(intervals.copy(), newInterval.copy()))
print("Optimal:", OptimalSolution().insert(intervals.copy(), newInterval.copy()))
print("Stack:", StackSolution().insert(intervals.copy(), newInterval.copy()))
print("InPlace:", InPlaceSolution().insert(intervals.copy(), newInterval.copy()))
print("Pythonic:", PythonicSolution().insert(intervals.copy(), newInterval.copy()))
print("BinarySearch:", BinarySearchSolution().insert(intervals.copy(), newInterval.copy()))
