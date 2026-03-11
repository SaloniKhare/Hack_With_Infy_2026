# ======================================================
# MERGE SORTED ARRAY - ALL APPROACHES
# ======================================================

# Problem (LeetCode 88):
# nums1 has size m + n where first m elements are valid
# nums2 has n elements
# Merge nums2 into nums1 as one sorted array.


# ------------------------------------------------------
# 1️⃣ Brute Force (Concatenate + Sort)
# ------------------------------------------------------

class BruteForceSolution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m] + nums2
        nums1.sort()


# ------------------------------------------------------
# 2️⃣ Extra Array (Two Pointer)
# ------------------------------------------------------

class ExtraArraySolution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        merged = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1

        nums1[:] = merged


# ------------------------------------------------------
# 3️⃣ Optimal Two Pointer (From End) ⭐
# ------------------------------------------------------

class TwoPointerOptimalSolution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# ------------------------------------------------------
# 4️⃣ Using Python Built-in Merge
# ------------------------------------------------------

class BuiltInSolution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
