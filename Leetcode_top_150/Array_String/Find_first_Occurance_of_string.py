# ======================================================
# FIND INDEX OF FIRST OCCURRENCE IN A STRING - ALL APPROACHES
# ======================================================

# Problem (LeetCode 28):
# Given two strings haystack and needle,
# return the index of the first occurrence of needle in haystack.
# If needle is not part of haystack, return -1.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1


# ------------------------------------------------------
# 2️⃣ Two Pointer Comparison
# ------------------------------------------------------

class TwoPointerSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1


# ------------------------------------------------------
# 3️⃣ Python Built-in (Simplest)
# ------------------------------------------------------

class BuiltInSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# ------------------------------------------------------
# 4️⃣ Rabin-Karp (Rolling Hash)
# ------------------------------------------------------

class RabinKarpSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        base = 26
        mod = 10**9 + 7

        needle_hash = 0
        window_hash = 0
        power = 1

        for i in range(m):
            needle_hash = (needle_hash * base + ord(needle[i])) % mod
            window_hash = (window_hash * base + ord(haystack[i])) % mod
            if i > 0:
                power = (power * base) % mod

        for i in range(n - m + 1):

            if needle_hash == window_hash:
                if haystack[i:i+m] == needle:
                    return i

            if i + m < n:
                window_hash = (
                    (window_hash - ord(haystack[i]) * power) * base
                    + ord(haystack[i + m])
                ) % mod

        return -1


# ------------------------------------------------------
# 5️⃣ KMP Algorithm (Optimal)
# ------------------------------------------------------

class KMPSolution:
    def strStr(self, haystack: str, needle: str) -> int:

        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        if not needle:
            return 0

        lps = build_lps(needle)

        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j

            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
