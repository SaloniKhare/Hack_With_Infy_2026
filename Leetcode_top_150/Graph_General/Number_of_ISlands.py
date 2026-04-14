# ======================================================
# NUMBER OF ISLANDS (LeetCode 200)
# ======================================================

# Problem:
# Given an m x n 2D grid grid where '1's represent land
# and '0's represent water, return the number of islands.
# An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically.

# ------------------------------------------------------
# 1️⃣ Brute Force (Repeated Scan)
# ------------------------------------------------------

class BruteForceSolution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


# ------------------------------------------------------
# 2️⃣ DFS (Recursive Flood Fill)
# ------------------------------------------------------

class DFSSolution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == '0'):
                return

            grid[r][c] = '0'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands


# ------------------------------------------------------
# 3️⃣ BFS (Queue)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    queue = deque([(i, j)])

                    while queue:
                        r, c = queue.popleft()

                        if (r < 0 or c < 0 or
                            r >= rows or c >= cols or
                            grid[r][c] == '0'):
                            continue

                        grid[r][c] = '0'

                        queue.append((r+1, c))
                        queue.append((r-1, c))
                        queue.append((r, c+1))
                        queue.append((r, c-1))

        return islands


# ------------------------------------------------------
# 4️⃣ Union-Find (Disjoint Set)
# ------------------------------------------------------

class UnionFindSolution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

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

        # Initialize
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    parent[(r, c)] = (r, c)
                    rank[(r, c)] = 0

        directions = [(1, 0), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < rows and nc < cols and
                            grid[nr][nc] == '1'):
                            union((r, c), (nr, nc))

        roots = set()
        for cell in parent:
            roots.add(find(cell))

        return len(roots)


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (DFS / BFS Flood Fill)
# ------------------------------------------------------

class OptimalSolution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == '0'):
                return

            grid[r][c] = '0'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count




