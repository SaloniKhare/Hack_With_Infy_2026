# ======================================================
# SPIRAL MATRIX - ALL APPROACHES
# ======================================================

# Problem (LeetCode 54):
# Given an m x n matrix, return all elements of the matrix
# in spiral order.


# ------------------------------------------------------
# 1️⃣ Simulation using Visited Matrix
# ------------------------------------------------------

class VisitedMatrixSolution:
    def spiralOrder(self, matrix):

        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])

        visited = [[False]*cols for _ in range(rows)]

        # directions: right, down, left, up
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        dir_idx = 0
        r = c = 0

        result = []

        for _ in range(rows * cols):

            result.append(matrix[r][c])
            visited[r][c] = True

            nr = r + directions[dir_idx][0]
            nc = c + directions[dir_idx][1]

            if (0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]):
                r, c = nr, nc
            else:
                dir_idx = (dir_idx + 1) % 4
                r += directions[dir_idx][0]
                c += directions[dir_idx][1]

        return result


# ------------------------------------------------------
# 2️⃣ Boundary Traversal (Optimal)
# ------------------------------------------------------

class BoundarySolution:
    def spiralOrder(self, matrix):

        if not matrix:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        result = []

        while top <= bottom and left <= right:

            # left → right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # top → bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # right → left
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # bottom → top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def spiralOrder(self, matrix):

        if not matrix:
            return []

        # top row
        top = matrix[0]

        # remaining matrix
        rest = [row[1:-1] for row in matrix[1:-1]]

        # right column
        right = [row[-1] for row in matrix[1:]]

        # bottom row (reversed)
        bottom = matrix[-1][::-1] if len(matrix) > 1 else []

        # left column (reversed)
        left = [row[0] for row in matrix[-2:0:-1]]

        return top + right + bottom + left + self.spiralOrder(rest)

