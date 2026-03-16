# ======================================================
# SUBSTRING WITH CONCATENATION OF ALL WORDS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 30):
# Given a string s and an array of strings words, where each word
# has the same length, return all starting indices of substring(s)
# that is a concatenation of each word in words exactly once
# and without any intervening characters.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

from collections import Counter

class BruteForceSolution:
    def findSubstring(self, s: str, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)

        word_count = Counter(words)
        res = []

        for i in range(len(s) - total_len + 1):

            seen = Counter()

            for j in range(len(words)):

                start = i + j * word_len
                word = s[start:start + word_len]

                if word not in word_count:
                    break

                seen[word] += 1

                if seen[word] > word_count[word]:
                    break

            if seen == word_count:
                res.append(i)

        return res


# ------------------------------------------------------
# 2️⃣ Sliding Window (HashMap)
# ------------------------------------------------------

from collections import Counter, defaultdict

class SlidingWindowSolution:
    def findSubstring(self, s: str, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_map = Counter(words)
        res = []

        for i in range(word_len):

            left = i
            curr = defaultdict(int)
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):

                word = s[j:j + word_len]

                if word in word_map:

                    curr[word] += 1
                    count += 1

                    while curr[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        res.append(left)

                else:
                    curr.clear()
                    count = 0
                    left = j + word_len

        return res


# ------------------------------------------------------
# 3️⃣ Optimized Sliding Window
# (Same logic but reduced recomputation)
# ------------------------------------------------------

class OptimizedSlidingWindowSolution:
    def findSubstring(self, s: str, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        k = len(words)
        total_len = word_len * k

        from collections import Counter

        word_count = Counter(words)
        res = []

        for i in range(word_len):

            left = i
            window = {}
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                if word in word_count:

                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > word_count[word]:

                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == k:
                        res.append(left)

                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return res
