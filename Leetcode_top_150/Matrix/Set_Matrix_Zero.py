# ======================================================
# SET MATRIX ZEROES - ALL APPROACHES
# ======================================================

# Problem (LeetCode 73):
# Given an m x n matrix, if an element is 0,
# set its entire row and column to 0.
# Do it in-place.


# ------------------------------------------------------
# 1️⃣ Brute Force (Mark then Update)
# ------------------------------------------------------

class BruteForceSolution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        mark = []

        # Find all zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    mark.append((i, j))

        # Set rows and columns to zero
        for r, c in mark:
            for j in range(cols):
                matrix[r][j] = 0
            for i in range(rows):
                matrix[i][c] = 0


# ------------------------------------------------------
# 2️⃣ Better (Using Row & Column Arrays)
# ------------------------------------------------------

class BetterSolution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        row_zero = [False] * rows
        col_zero = [False] * cols

        # Mark rows and columns
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True

        # Update matrix
        for i in range(rows):
            for j in range(cols):
                if row_zero[i] or col_zero[j]:
                    matrix[i][j] = 0


# ------------------------------------------------------
# 3️⃣ Optimal (Using First Row & Column as Markers)
# ------------------------------------------------------

class OptimalSolution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Use first row & column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update inner matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Update first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        # Update first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

