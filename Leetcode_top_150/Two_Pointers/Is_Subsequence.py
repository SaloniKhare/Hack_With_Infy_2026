# ======================================================
# IS SUBSEQUENCE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 392):
# Given two strings s and t, return True if s is a subsequence of t.
# A subsequence means characters appear in the same order but
# not necessarily consecutively.


# ------------------------------------------------------
# 1️⃣ Brute Force (Two Pointer)
# ------------------------------------------------------

class BruteForceSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# ------------------------------------------------------
# 2️⃣ Greedy Single Pointer
# ------------------------------------------------------

class GreedySolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0

        for char in t:
            if idx < len(s) and s[idx] == char:
                idx += 1

        return idx == len(s)


# ------------------------------------------------------
# 3️⃣ Using Python Iterator
# ------------------------------------------------------

class IteratorSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(c in it for c in s)


# ------------------------------------------------------
# 4️⃣ Dynamic Programming (LCS Based)
# ------------------------------------------------------

class DPSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n] == m


# ------------------------------------------------------
# 5️⃣ Binary Search + Preprocessing (Advanced)
# Useful when many queries of s are checked against same t
# ------------------------------------------------------

import bisect
from collections import defaultdict

class BinarySearchSolution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pos = defaultdict(list)

        for i, ch in enumerate(t):
            pos[ch].append(i)

        curr = -1

        for ch in s:
            if ch not in pos:
                return False

            idx = bisect.bisect_right(pos[ch], curr)

            if idx == len(pos[ch]):
                return False

            curr = pos[ch][idx]

        return True
