# ======================================================
# GROUP ANAGRAMS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 49):
# Given an array of strings strs, group the anagrams together.
#
# Example:
# Input: ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]


# ------------------------------------------------------
# 1️⃣ Brute Force (Compare Each Pair)
# ------------------------------------------------------

class BruteForceSolution:
    def groupAnagrams(self, strs):

        def is_anagram(a, b):
            return sorted(a) == sorted(b)

        visited = [False] * len(strs)
        result = []

        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j] and is_anagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            result.append(group)

        return result


# ------------------------------------------------------
# 2️⃣ Sorting as Key
# ------------------------------------------------------

from collections import defaultdict

class SortingSolution:
    def groupAnagrams(self, strs):

        anagram_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())


# ------------------------------------------------------
# 3️⃣ Frequency Count as Key (Optimal)
# ------------------------------------------------------

from collections import defaultdict

class FrequencySolution:
    def groupAnagrams(self, strs):

        anagram_map = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)
            anagram_map[key].append(word)

        return list(anagram_map.values())


# ------------------------------------------------------
# 4️⃣ Counter as Key (Pythonic)
# ------------------------------------------------------

from collections import defaultdict, Counter

class CounterSolution:
    def groupAnagrams(self, strs):

        anagram_map = defaultdict(list)

        for word in strs:
            key = tuple(Counter(word).items())
            anagram_map[key].append(word)

        return list(anagram_map.values())


# ------------------------------------------------------
# Example
# ------------------------------------------------------

strs = ["eat","tea","tan","ate","nat","bat"]

print(BruteForceSolution().groupAnagrams(strs))
print(SortingSolution().groupAnagrams(strs))
print(FrequencySolution().groupAnagrams(strs))
print(CounterSolution().groupAnagrams(strs))
