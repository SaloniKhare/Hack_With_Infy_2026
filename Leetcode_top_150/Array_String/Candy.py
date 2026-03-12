# ======================================================
# CANDY - ALL APPROACHES
# ======================================================

# Problem (LeetCode 135):
# There are n children standing in a line.
# Each child has a rating.
# Rules:
# 1. Each child must have at least 1 candy.
# 2. Children with higher rating than neighbors must get more candies.
# Return the minimum candies required.


# ------------------------------------------------------
# 1️⃣ Brute Force (Iterative Adjustment)
# ------------------------------------------------------

class BruteForceSolution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        changed = True

        while changed:
            changed = False

            for i in range(n):
                if i > 0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1
                    changed = True

                if i < n-1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
                    changed = True

        return sum(candies)


# ------------------------------------------------------
# 2️⃣ Two Arrays (Left and Right Pass)
# ------------------------------------------------------

class TwoArraySolution:
    def candy(self, ratings):
        n = len(ratings)

        left = [1] * n
        right = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1

        # Right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1

        total = 0
        for i in range(n):
            total += max(left[i], right[i])

        return total


# ------------------------------------------------------
# 3️⃣ Single Array (Two Pass Greedy)
# ------------------------------------------------------

class SingleArraySolution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        # Left → Right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Right → Left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)


# ------------------------------------------------------
# 4️⃣ Optimal Greedy (Constant Space)
# ------------------------------------------------------

class GreedyOptimalSolution:
    def candy(self, ratings):
        n = len(ratings)

        up = 0
        down = 0
        peak = 0
        candies = 1

        for i in range(1, n):

            if ratings[i] > ratings[i-1]:
                up += 1
                peak = up
                down = 0
                candies += 1 + up

            elif ratings[i] == ratings[i-1]:
                up = down = peak = 0
                candies += 1

            else:
                up = 0
                down += 1
                candies += 1 + down
                if down > peak:
                    candies += 1

        return candies
