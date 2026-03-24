# ======================================================
# MERGE INTERVALS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 56):
# Given an array of intervals where intervals[i] = [start, end],
# merge all overlapping intervals and return non-overlapping intervals.
#
# Example:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]


# ------------------------------------------------------
# 1️⃣ Brute Force (Compare Every Pair)
# ------------------------------------------------------

class BruteForceSolution:
    def merge(self, intervals):

        intervals.sort()
        n = len(intervals)

        for i in range(n):
            for j in range(i + 1, n):

                if intervals[i][1] >= intervals[j][0]:
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    intervals[j] = [-1, -1]

        result = []
        for interval in intervals:
            if interval != [-1, -1]:
                result.append(interval)

        return result


# ------------------------------------------------------
# 2️⃣ Optimal Sorting + Greedy (Most Important)
# ------------------------------------------------------

class OptimalSolution:
    def merge(self, intervals):

        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:

            last_end = result[-1][1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result


# ------------------------------------------------------
# 3️⃣ Using Stack
# ------------------------------------------------------

class StackSolution:
    def merge(self, intervals):

        intervals.sort()
        stack = [intervals[0]]

        for interval in intervals[1:]:

            if stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)

        return stack


# ------------------------------------------------------
# 4️⃣ In-Place Merging
# ------------------------------------------------------

class InPlaceSolution:
    def merge(self, intervals):

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
# 5️⃣ Using Separate Start & End Arrays
# ------------------------------------------------------

class SeparateArraySolution:
    def merge(self, intervals):

        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        result = []
        n = len(intervals)
        start = starts[0]

        for i in range(1, n):
            if starts[i] > ends[i - 1]:
                result.append([start, ends[i - 1]])
                start = starts[i]

        result.append([start, ends[-1]])

        return result


# ------------------------------------------------------
# 6️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def merge(self, intervals):

        intervals.sort()
        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result


# ------------------------------------------------------
# Example
# ------------------------------------------------------

intervals = [[1,3],[2,6],[8,10],[15,18]]

print("BruteForce:", BruteForceSolution().merge(intervals))
print("Optimal:", OptimalSolution().merge(intervals))
print("Stack:", StackSolution().merge(intervals))
print("InPlace:", InPlaceSolution().merge(intervals))
print("SeparateArray:", SeparateArraySolution().merge(intervals))
print("Pythonic:", PythonicSolution().merge(intervals))
