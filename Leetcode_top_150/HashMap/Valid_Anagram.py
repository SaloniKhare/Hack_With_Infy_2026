# ======================================================
# VALID ANAGRAM - ALL APPROACHES
# ======================================================

# Problem (LeetCode 242):
# Given two strings s and t, return True if t is an anagram of s.
# An anagram means both strings have same characters with same frequency.


# ------------------------------------------------------
# 1️⃣ Brute Force (Sort and Compare)
# ------------------------------------------------------

class BruteForceSolution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)


# ------------------------------------------------------
# 2️⃣ HashMap (Frequency Count)
# ------------------------------------------------------

from collections import Counter

class HashMapSolution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = Counter(s)

        for ch in t:
            if count[ch] == 0:
                return False
            count[ch] -= 1

        return True


# ------------------------------------------------------
# 3️⃣ Counter Direct Comparison
# ------------------------------------------------------

from collections import Counter

class CounterSolution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)


# ------------------------------------------------------
# 4️⃣ Array (Optimized for lowercase letters)
# ------------------------------------------------------

class ArraySolution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            idx = ord(ch) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True
