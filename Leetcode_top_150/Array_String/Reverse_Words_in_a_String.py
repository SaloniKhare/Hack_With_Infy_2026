# ======================================================
# REVERSE WORDS IN A STRING - ALL APPROACHES
# ======================================================

# Problem (LeetCode 151):
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The output should not contain leading or trailing spaces
# and words should be separated by a single space.


# ------------------------------------------------------
# 1️⃣ Brute Force (Split + Reverse)
# ------------------------------------------------------

class SplitReverseSolution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)


# ------------------------------------------------------
# 2️⃣ Pythonic One-Liner
# ------------------------------------------------------

class PythonicSolution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# ------------------------------------------------------
# 3️⃣ Using Stack
# ------------------------------------------------------

class StackSolution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        stack = []

        for word in words:
            stack.append(word)

        result = []

        while stack:
            result.append(stack.pop())

        return " ".join(result)


# ------------------------------------------------------
# 4️⃣ Two Pointer (Manual Parsing)
# ------------------------------------------------------

class TwoPointerSolution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)

        while i < n:
            while i < n and s[i] == " ":
                i += 1

            start = i

            while i < n and s[i] != " ":
                i += 1

            if start < i:
                words.append(s[start:i])

        words.reverse()
        return " ".join(words)


# ------------------------------------------------------
# 5️⃣ In-place Style (Reverse Entire String)
# ------------------------------------------------------

class ReverseTechniqueSolution:
    def reverseWords(self, s: str) -> str:
        s = list(s.strip())

        # helper function
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # reverse whole string
        reverse(0, len(s) - 1)

        start = 0

        for end in range(len(s) + 1):
            if end == len(s) or s[end] == " ":
                reverse(start, end - 1)
                start = end + 1

        return " ".join("".join(s).split())
