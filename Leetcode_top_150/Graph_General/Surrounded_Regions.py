# ======================================================
# SURROUNDED REGIONS (LeetCode 130)
# ======================================================

# Problem:
# Given an m x n board containing 'X' and 'O',
# capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's
# in that surrounded region.
# Boundary-connected 'O's should NOT be flipped.


# ------------------------------------------------------
# 1️⃣ Brute Force (Check Each Region Individually)
# ------------------------------------------------------

class BruteForceSolution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, region):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != 'O'):
                return True

            board[r][c] = '#'
            region.append((r, c))

            up = dfs(r-1, c, region)
            down = dfs(r+1, c, region)
            left = dfs(r, c-1, region)
            right = dfs(r, c+1, region)

            return up and down and left and right

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    region = []
                    if dfs(i, j, region):
                        for r, c in region:
                            board[r][c] = 'X'
                    else:
                        for r, c in region:
                            board[r][c] = 'O'


# ------------------------------------------------------
# 2️⃣ DFS from Boundary (Mark Safe Cells)
# ------------------------------------------------------

class DFSSolution:
    def solve(self, board):
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != 'O'):
                return

            board[r][c] = '#'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Step 1: mark boundary-connected O's
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # Step 2: flip surrounded O → X, restore # → O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


# ------------------------------------------------------
# 3️⃣ BFS from Boundary
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def solve(self, board):
        if not board:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        # Add boundary O's
        for i in range(rows):
            for j in [0, cols - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        for j in range(cols):
            for i in [0, rows - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        # BFS marking safe cells
        while queue:
            r, c = queue.popleft()

            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != 'O'):
                continue

            board[r][c] = '#'

            queue.append((r+1, c))
            queue.append((r-1, c))
            queue.append((r, c+1))
            queue.append((r, c-1))

        # Flip & restore
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


# ------------------------------------------------------
# 4️⃣ Union-Find (Disjoint Set)
# ------------------------------------------------------

class UnionFindSolution:
    def solve(self, board):
        if not board:
            return

        rows, cols = len(board), len(board[0])
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        dummy = (-1, -1)

        # Initialize
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    parent[(i, j)] = (i, j)
                    rank[(i, j)] = 0

        parent[dummy] = dummy
        rank[dummy] = 0

        # Union operations
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i in [0, rows - 1] or j in [0, cols - 1]:
                        union((i, j), dummy)

                    for dx, dy in [(1, 0), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if (0 <= ni < rows and 0 <= nj < cols and
                            board[ni][nj] == 'O'):
                            union((i, j), (ni, nj))

        # Flip cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and find((i, j)) != find(dummy):
                    board[i][j] = 'X'


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Boundary DFS)
# ------------------------------------------------------

class OptimalSolution:
    def solve(self, board):
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != 'O'):
                return

            board[r][c] = '#'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Mark boundary-connected regions
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # Flip and restore
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'




