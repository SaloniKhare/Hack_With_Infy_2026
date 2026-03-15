# ======================================================
# VALID PALINDROME - ALL APPROACHES
# ======================================================

# Problem (LeetCode 125):
# Given a string s, return True if it is a palindrome
# considering only alphanumeric characters and ignoring cases.


# ------------------------------------------------------
# 1️⃣ Brute Force (Filter + Reverse)
# ------------------------------------------------------

class BruteForceSolution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""

        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()

        return filtered == filtered[::-1]


# ------------------------------------------------------
# 2️⃣ Using List Builder
# ------------------------------------------------------

class ListBuilderSolution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())

        return chars == chars[::-1]


# ------------------------------------------------------
# 3️⃣ Two Pointer (Most Common Interview Solution) ⭐
# ------------------------------------------------------

class TwoPointerSolution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# ------------------------------------------------------
# 4️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]


# ------------------------------------------------------
# 5️⃣ Regex Based
# ------------------------------------------------------

import re

class RegexSolution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]
