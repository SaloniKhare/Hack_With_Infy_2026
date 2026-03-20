# ======================================================
# RANSOM NOTE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 383):
# Given two strings ransomNote and magazine,
# return True if ransomNote can be constructed using letters
# from magazine.
#
# Each letter in magazine can only be used once.


# ------------------------------------------------------
# 1️⃣ Brute Force (Remove Characters)
# ------------------------------------------------------

class BruteForceSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag = list(magazine)

        for ch in ransomNote:
            if ch in mag:
                mag.remove(ch)
            else:
                return False

        return True


# ------------------------------------------------------
# 2️⃣ HashMap (Frequency Count)
# ------------------------------------------------------

from collections import Counter

class HashMapSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = Counter(magazine)

        for ch in ransomNote:
            if count[ch] == 0:
                return False
            count[ch] -= 1

        return True


# ------------------------------------------------------
# 3️⃣ Using Counter Subtraction (Pythonic)
# ------------------------------------------------------

from collections import Counter

class CounterSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return not (Counter(ransomNote) - Counter(magazine))


# ------------------------------------------------------
# 4️⃣ Array (Optimized for lowercase letters)
# ------------------------------------------------------

class ArraySolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = [0] * 26

        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True
