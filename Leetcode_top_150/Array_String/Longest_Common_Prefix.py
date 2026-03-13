# ======================================================
# LONGEST COMMON PREFIX - ALL APPROACHES
# ======================================================

# Problem (LeetCode 14):
# Write a function to find the longest common prefix
# string amongst an array of strings.


# ------------------------------------------------------
# 1️⃣ Brute Force (Character by Character)
# ------------------------------------------------------

class BruteForceSolution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != char:
                    return prefix

            prefix += char

        return prefix


# ------------------------------------------------------
# 2️⃣ Horizontal Scanning
# ------------------------------------------------------

class HorizontalScanningSolution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# ------------------------------------------------------
# 3️⃣ Vertical Scanning ⭐
# ------------------------------------------------------

class VerticalScanningSolution:
    def longestCommonPrefix(self, strs):

        for i in range(len(strs[0])):

            char = strs[0][i]

            for word in strs:
                if i == len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]


# ------------------------------------------------------
# 4️⃣ Divide and Conquer
# ------------------------------------------------------

class DivideConquerSolution:

    def longestCommonPrefix(self, strs):
        return self.lcp(strs, 0, len(strs)-1)

    def lcp(self, strs, left, right):

        if left == right:
            return strs[left]

        mid = (left + right) // 2

        lcp_left = self.lcp(strs, left, mid)
        lcp_right = self.lcp(strs, mid + 1, right)

        return self.commonPrefix(lcp_left, lcp_right)

    def commonPrefix(self, left, right):

        length = min(len(left), len(right))

        for i in range(length):
            if left[i] != right[i]:
                return left[:i]

        return left[:length]


# ------------------------------------------------------
# 5️⃣ Binary Search on Prefix Length
# ------------------------------------------------------

class BinarySearchSolution:

    def longestCommonPrefix(self, strs):

        min_len = min(len(s) for s in strs)

        low = 1
        high = min_len

        while low <= high:

            mid = (low + high) // 2

            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:(low + high)//2]

    def isCommonPrefix(self, strs, length):

        prefix = strs[0][:length]

        for s in strs:
            if not s.startswith(prefix):
                return False

        return True

# ------------------------------------------------------
# 5️⃣ Sorting
# ------------------------------------------------------
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = sorted(strs)
        a, b = x[0], x[-1]
        ans = ""
        print(x)

        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                return ans
            ans += a[i]

        return ans
