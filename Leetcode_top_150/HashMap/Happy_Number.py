# ======================================================
# HAPPY NUMBER - ALL APPROACHES
# ======================================================

# Problem (LeetCode 202):
# A number is happy if:
# - Replace number with sum of squares of its digits
# - Repeat process
# - If it becomes 1 → happy
# - If it loops → not happy


# ------------------------------------------------------
# Helper Function
# ------------------------------------------------------

def get_next(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


# ------------------------------------------------------
# 1️⃣ Brute Force (Limit Iterations)
# ------------------------------------------------------

class BruteForceSolution:
    def isHappy(self, n: int) -> bool:

        for _ in range(100):  # arbitrary limit
            if n == 1:
                return True
            n = get_next(n)

        return False


# ------------------------------------------------------
# 2️⃣ HashSet (Detect Cycle)
# ------------------------------------------------------

class HashSetSolution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)
            n = get_next(n)

        return True


# ------------------------------------------------------
# 3️⃣ Floyd Cycle Detection (Fast & Slow Pointer)
# ------------------------------------------------------

class FloydCycleSolution:
    def isHappy(self, n: int) -> bool:

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:

            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


# ------------------------------------------------------
# Example
# ------------------------------------------------------

n = 19

print(BruteForceSolution().isHappy(n))
print(HashSetSolution().isHappy(n))
print(FloydCycleSolution().isHappy(n))
