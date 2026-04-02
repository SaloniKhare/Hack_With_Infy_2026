# ======================================================
# MINIMUM WINDOW SUBSTRING - ALL APPROACHES
# ======================================================

# Problem (LeetCode 76):
# Given strings s and t, return the minimum window substring of s
# such that every character in t (including duplicates) is included.
#
# If no such substring exists, return "".
#
# Example:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"


# ------------------------------------------------------
# 1️⃣ Brute Force (Check All Substrings)
# ------------------------------------------------------

class BruteForceSolution:
    def minWindow(self, s, t):

        from collections import Counter

        def valid(sub, t_count):
            sub_count = Counter(sub)
            for c in t_count:
                if sub_count[c] < t_count[c]:
                    return False
            return True

        t_count = Counter(t)
        n = len(s)
        res = ""

        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if valid(sub, t_count):
                    if res == "" or len(sub) < len(res):
                        res = sub

        return res


# ------------------------------------------------------
# 2️⃣ Sliding Window (Optimal) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def minWindow(self, s, t):

        from collections import Counter

        if not t or not s:
            return ""

        t_count = Counter(t)
        window = {}

        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):

            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            # shrink window
            while have == need:

                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""


# ------------------------------------------------------
# 3️⃣ Using defaultdict
# ------------------------------------------------------

from collections import defaultdict

class DefaultDictSolution:
    def minWindow(self, s, t):

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        window = defaultdict(int)

        have, need = 0, len(t_count)
        res = ""
        min_len = float("inf")

        l = 0

        for r in range(len(s)):

            c = s[r]
            window[c] += 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:

                if (r - l + 1) < min_len:
                    res = s[l:r+1]
                    min_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        return res


# ------------------------------------------------------
# 4️⃣ Optimized with Fixed Array (ASCII)
# ------------------------------------------------------

class ArraySolution:
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        t_count = [0] * 128
        for c in t:
            t_count[ord(c)] += 1

        required = len(t)
        l = 0
        min_len = float("inf")
        start = 0

        for r in range(len(s)):

            if t_count[ord(s[r])] > 0:
                required -= 1

            t_count[ord(s[r])] -= 1

            while required == 0:

                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start = l

                t_count[ord(s[l])] += 1

                if t_count[ord(s[l])] > 0:
                    required += 1

                l += 1

        return "" if min_len == float("inf") else s[start:start + min_len]


# ------------------------------------------------------
# 5️⃣ Pythonic Version
# ------------------------------------------------------

class PythonicSolution:
    def minWindow(self, s, t):

        from collections import Counter

        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):

            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            if missing == 0:

                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:
                    start, end = left, right

                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


# ------------------------------------------------------
# Example
# ------------------------------------------------------

s = "ADOBECODEBANC"
t = "ABC"

print("BruteForce:", BruteForceSolution().minWindow(s, t))
print("Optimal:", OptimalSolution().minWindow(s, t))
print("DefaultDict:", DefaultDictSolution().minWindow(s, t))
print("Array:", ArraySolution().minWindow(s, t))
print("Pythonic:", PythonicSolution().minWindow(s, t))
