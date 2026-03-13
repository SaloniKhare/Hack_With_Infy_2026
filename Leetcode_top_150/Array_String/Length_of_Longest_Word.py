# ======================================================
# LENGTH OF LAST WORD - ALL APPROACHES
# ======================================================

# Problem (LeetCode 58):
# Given a string s consisting of words and spaces,
# return the length of the last word.


# ------------------------------------------------------
# 1️⃣ Brute Force (Split)
# ------------------------------------------------------

class SplitSolution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


# ------------------------------------------------------
# 2️⃣ Trim + Split
# ------------------------------------------------------

class TrimSplitSolution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        return len(words[-1])


# ------------------------------------------------------
# 3️⃣ Reverse Traversal (Two Pointer)
# ------------------------------------------------------

class ReverseTraversalSolution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # count characters
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


# ------------------------------------------------------
# 4️⃣ Single Pass from End ⭐
# ------------------------------------------------------

class OptimalSolution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        found = False

        for i in range(len(s) - 1, -1, -1):

            if s[i] != " ":
                found = True
                length += 1

            elif found:
                break

        return length


# ------------------------------------------------------
# 5️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])
