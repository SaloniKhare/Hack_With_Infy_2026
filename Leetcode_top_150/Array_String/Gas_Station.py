# ======================================================
# GAS STATION - ALL APPROACHES
# ======================================================

# Problem (LeetCode 134):
# There are n gas stations along a circular route.
# gas[i] = gas available at station i
# cost[i] = gas needed to go from station i → i+1
# Return the starting station index if you can travel
# around the circuit once, otherwise return -1.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)

        for start in range(n):
            tank = 0
            completed = True

            for i in range(n):
                idx = (start + i) % n
                tank += gas[idx] - cost[idx]

                if tank < 0:
                    completed = False
                    break

            if completed:
                return start

        return -1


# ------------------------------------------------------
# 2️⃣ Prefix Sum Approach
# ------------------------------------------------------

class PrefixSumSolution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        total = sum(diff)
        if total < 0:
            return -1

        min_sum = float('inf')
        curr = 0
        start = 0

        for i in range(n):
            curr += diff[i]
            if curr < min_sum:
                min_sum = curr
                start = i + 1

        return start % n


# ------------------------------------------------------
# 3️⃣ Greedy (Optimal Solution) ⭐
# ------------------------------------------------------

class GreedySolution:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1


# ------------------------------------------------------
# 4️⃣ Kadane-style Interpretation
# ------------------------------------------------------

class KadaneStyleSolution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total = 0
        curr = 0
        start = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            if curr < 0:
                start = i + 1
                curr = 0

        return start if total >= 0 else -1
