# ======================================================
# ROMAN TO INTEGER - ALL APPROACHES
# ======================================================

# Problem (LeetCode 13):
# Convert a Roman numeral string into an integer.

# Roman values:
# I=1, V=5, X=10, L=50, C=100, D=500, M=1000

# Special cases:
# IV=4, IX=9
# XL=40, XC=90
# CD=400, CM=900


# ------------------------------------------------------
# 1️⃣ Brute Force (Check Special Pairs First)
# ------------------------------------------------------

class BruteForceSolution:
    def romanToInt(self, s: str) -> int:

        values = {
            "I":1, "V":5, "X":10, "L":50,
            "C":100, "D":500, "M":1000
        }

        special = {
            "IV":4, "IX":9,
            "XL":40, "XC":90,
            "CD":400, "CM":900
        }

        i = 0
        total = 0

        while i < len(s):

            if i + 1 < len(s) and s[i:i+2] in special:
                total += special[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1

        return total


# ------------------------------------------------------
# 2️⃣ Left to Right Comparison
# ------------------------------------------------------

class LeftToRightSolution:
    def romanToInt(self, s: str) -> int:

        values = {
            "I":1, "V":5, "X":10, "L":50,
            "C":100, "D":500, "M":1000
        }

        total = 0

        for i in range(len(s)-1):

            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        total += values[s[-1]]

        return total


# ------------------------------------------------------
# 3️⃣ Right to Left Scan
# ------------------------------------------------------

class RightToLeftSolution:
    def romanToInt(self, s: str):

        values = {
            "I":1, "V":5, "X":10, "L":50,
            "C":100, "D":500, "M":1000
        }

        total = 0
        prev = 0

        for ch in reversed(s):

            curr = values[ch]

            if curr < prev:
                total -= curr
            else:
                total += curr

            prev = curr

        return total


# ------------------------------------------------------
# 4️⃣ Stack Based Approach
# ------------------------------------------------------

class StackSolution:
    def romanToInt(self, s: str):

        values = {
            "I":1, "V":5, "X":10, "L":50,
            "C":100, "D":500, "M":1000
        }

        stack = []

        for ch in s:
            val = values[ch]

            if stack and val > stack[-1]:
                stack[-1] = val - stack[-1]
            else:
                stack.append(val)

        return sum(stack)


# ------------------------------------------------------
# 5️⃣ Optimized Dictionary Lookahead ⭐
# ------------------------------------------------------

class OptimalSolution:
    def romanToInt(self, s: str):

        values = {
            "I":1, "V":5, "X":10, "L":50,
            "C":100, "D":500, "M":1000
        }

        result = 0

        for i in range(len(s)):

            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]

        return result
