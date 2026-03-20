# ======================================================
# WORD PATTERN - ALL APPROACHES
# ======================================================

# Problem (LeetCode 290):
# Given a pattern and a string s, check if s follows the same pattern.
#
# Example:
# pattern = "abba"
# s = "dog cat cat dog" → True
#
# Each character in pattern maps to exactly one word,
# and no two characters map to the same word (bijection).


# ------------------------------------------------------
# 1️⃣ Brute Force (Check Mapping + Reverse Mapping)
# ------------------------------------------------------

class BruteForceSolution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            for j in range(i + 1, len(pattern)):

                if (pattern[i] == pattern[j] and words[i] != words[j]) or \
                   (pattern[i] != pattern[j] and words[i] == words[j]):
                    return False

        return True


# ------------------------------------------------------
# 2️⃣ HashMap + Set (One Direction + Check Duplicate)
# ------------------------------------------------------

class HashMapSetSolution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        used_words = set()

        for p, w in zip(pattern, words):

            if p not in mapping:
                if w in used_words:
                    return False

                mapping[p] = w
                used_words.add(w)

            else:
                if mapping[p] != w:
                    return False

        return True


# ------------------------------------------------------
# 3️⃣ Two HashMaps (Bidirectional Mapping)
# ------------------------------------------------------

class TwoMapSolution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for p, w in zip(pattern, words):

            if (p in p_to_w and p_to_w[p] != w) or \
               (w in w_to_p and w_to_p[w] != p):
                return False

            p_to_w[p] = w
            w_to_p[w] = p

        return True


# ------------------------------------------------------
# 4️⃣ Pythonic Trick (Pattern Matching via Indexing)
# ------------------------------------------------------

class PythonicSolution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        return list(map(pattern.index, pattern)) == list(map(words.index, words))
