# ======================================================
# ROTATE IMAGE (90° CLOCKWISE) - ALL APPROACHES
# ======================================================

# Problem (LeetCode 48):
# Given an n x n 2D matrix, rotate the image by 90 degrees (clockwise).
# You must do it in-place.


# ------------------------------------------------------
# 1️⃣ Using Extra Matrix (Brute Force)
# ------------------------------------------------------

class ExtraMatrixSolution:
    def rotate(self, matrix):

        n = len(matrix)

        res = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                res[j][n - 1 - i] = matrix[i][j]

        # copy back
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]


# ------------------------------------------------------
# 2️⃣ Transpose + Reverse (Optimal)
# ------------------------------------------------------

class OptimalSolution:
    def rotate(self, matrix):

        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# ------------------------------------------------------
# 3️⃣ Layer-by-Layer Rotation (In-place)
# ------------------------------------------------------

class LayerRotationSolution:
    def rotate(self, matrix):

        n = len(matrix)

        left = 0
        right = n - 1

        while left < right:

            for i in range(right - left):

                top = left
                bottom = right

                # save top-left
                temp = matrix[top][left + i]

                # bottom-left → top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom-right → bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top-right → bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # temp → top-right
                matrix[top + i][right] = temp

            left += 1
            right -= 1

