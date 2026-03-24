# ======================================================
# MINIMUM NUMBER OF ARROWS TO BURST BALLOONS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 452):
# You are given an array of balloon intervals points where:
# points[i] = [start, end]
# An arrow can burst all balloons whose intervals overlap at that point.
# Return the minimum number of arrows required.
#
# Example:
# Input: [[10,16],[2,8],[1,6],[7,12]]
# Output: 2


# ------------------------------------------------------
# 1️⃣ Brute Force (Try Every Overlap)
# ------------------------------------------------------

class BruteForceSolution:
    def findMinArrowShots(self, points):

        if not points:
            return 0

        points.sort()
        arrows = 0

        while points:
            start, end = points.pop(0)
            arrows += 1

            temp = []
            for s, e in points:
                if s > end or e < start:
                    temp.append([s, e])
                else:
                    start = max(start, s)
                    end = min(end, e)

            points = temp

        return arrows


# ------------------------------------------------------
# 2️⃣ Greedy (Sort by End) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def findMinArrowShots(self, points):

        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:

            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows


# ------------------------------------------------------
# 3️⃣ Greedy (Sort by Start)
# ------------------------------------------------------

class StartBasedSolution:
    def findMinArrowShots(self, points):

        if not points:
            return 0

        points.sort()
        arrows = 1
        end = points[0][1]

        for i in range(1, len(points)):

            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                arrows += 1
                end = points[i][1]

        return arrows


# ------------------------------------------------------
# 4️⃣ Using Merge Intervals Concept
# ------------------------------------------------------

class MergeLikeSolution:
    def findMinArrowShots(self, points):

        if not points:
            return 0

        points.sort()
        merged = []

        for interval in points:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = min(merged[-1][1], interval[1])

        return len(merged)


# ------------------------------------------------------
# 5️⃣ Stack Based Approach
# ------------------------------------------------------

class StackSolution:
    def findMinArrowShots(self, points):

        if not points:
            return 0

        points.sort()
        stack = [points[0]]

        for interval in points[1:]:

            if stack[-1][1] >= interval[0]:
                stack[-1][1] = min(stack[-1][1], interval[1])
            else:
                stack.append(interval)

        return len(stack)


# ------------------------------------------------------
# 6️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def findMinArrowShots(self, points):

        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 0
        end = float('-inf')

        for s, e in points:
            if s > end:
                arrows += 1
                end = e

        return arrows
