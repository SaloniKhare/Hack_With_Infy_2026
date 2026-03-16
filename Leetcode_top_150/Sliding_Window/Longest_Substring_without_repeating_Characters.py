# ======================================================
# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ALL APPROACHES
# ======================================================

# Problem:
# Given a string s, return the length of the longest substring
# without repeating characters.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        ans = 0

        for i in range(n):

            seen = set()

            for j in range(i, n):

                if s[j] in seen:
                    break

                seen.add(s[j])
                ans = max(ans, j - i + 1)

        return ans


# ------------------------------------------------------
# 2️⃣ Sliding Window (Frequency Map)
# ------------------------------------------------------

class SlidingWindowFreqSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        di = {}
        l = 0
        ans = 0

        for r in range(len(s)):

            di[s[r]] = di.get(s[r], 0) + 1

            while di[s[r]] > 1:
                di[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans


# ------------------------------------------------------
# 3️⃣ Sliding Window (Set)
# ------------------------------------------------------

class SlidingWindowSetSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        ans = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            ans = max(ans, r - l + 1)

        return ans


# ------------------------------------------------------
# 4️⃣ Sliding Window (HashMap Last Index - Optimal)
# ------------------------------------------------------

class SlidingWindowIndexSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last = {}
        l = 0
        ans = 0

        for r, ch in enumerate(s):

            if ch in last and last[ch] >= l:
                l = last[ch] + 1

            last[ch] = r
            ans = max(ans, r - l + 1)

        return ans


# ------------------------------------------------------
# 5️⃣ ASCII Array Optimization
# ------------------------------------------------------

class ASCIISolution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last = [-1] * 128
        l = 0
        ans = 0

        for r in range(len(s)):

            l = max(l, last[ord(s[r])] + 1)

            last[ord(s[r])] = r

            ans = max(ans, r - l + 1)

        return ans
