# ======================================================
# EVALUATE DIVISION (LeetCode 399)
# ======================================================

# Problem:
# You are given equations like a / b = 2.0 and queries like a / c.
# Return the answers to all queries. If the answer cannot be determined,
# return -1.0.
#
# Input:
# equations = [["a","b"],["b","c"]]
# values = [2.0, 3.0]
# queries = [["a","c"],["b","a"],["a","e"]]


# ------------------------------------------------------
# 1️⃣ Brute Force (Try All Paths Recursively)
# ------------------------------------------------------

class BruteForceSolution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, target, visited):
            if src == target:
                return 1.0

            visited.add(src)

            for nei, val in graph[src]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1.0:
                        return res * val

            return -1.0

        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(a, b, set()))

        return result


# ------------------------------------------------------
# 2️⃣ DFS (Clean Graph Traversal)
# ------------------------------------------------------

class DFSSolution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(src, target, visited):
            if src not in graph or target not in graph:
                return -1.0
            if src == target:
                return 1.0

            visited.add(src)

            for nei in graph[src]:
                if nei in visited:
                    continue
                res = dfs(nei, target, visited)
                if res != -1.0:
                    return res * graph[src][nei]

            return -1.0

        return [dfs(a, b, set()) for a, b in queries]


# ------------------------------------------------------
# 3️⃣ BFS (Shortest Path Style)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1.0

            queue = deque([(src, 1.0)])
            visited = set([src])

            while queue:
                node, value = queue.popleft()

                if node == target:
                    return value

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, value * graph[node][nei]))

            return -1.0

        return [bfs(a, b) for a, b in queries]


# ------------------------------------------------------
# 4️⃣ Union-Find (Weighted Graph)
# ------------------------------------------------------

class UnionFindSolution:
    def calcEquation(self, equations, values, queries):
        parent = {}
        weight = {}

        def find(x):
            if parent[x] != x:
                orig = parent[x]
                parent[x] = find(parent[x])
                weight[x] *= weight[orig]
            return parent[x]

        def union(x, y, value):
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
            if y not in parent:
                parent[y] = y
                weight[y] = 1.0

            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                parent[rootX] = rootY
                weight[rootX] = weight[y] * value / weight[x]

        # Build Union-Find
        for (a, b), val in zip(equations, values):
            union(a, b, val)

        def isConnected(x, y):
            if x not in parent or y not in parent:
                return -1.0

            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                return -1.0

            return weight[x] / weight[y]

        return [isConnected(a, b) for a, b in queries]


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Union-Find with Weights)
# ------------------------------------------------------

class OptimalSolution:
    def calcEquation(self, equations, values, queries):
        parent = {}
        weight = {}

        def find(x):
            if parent[x] != x:
                orig_parent = parent[x]
                parent[x] = find(parent[x])
                weight[x] *= weight[orig_parent]
            return parent[x]

        def union(x, y, val):
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
            if y not in parent:
                parent[y] = y
                weight[y] = 1.0

            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                parent[rootX] = rootY
                weight[rootX] = weight[y] * val / weight[x]

        # Build graph
        for (a, b), val in zip(equations, values):
            union(a, b, val)

        result = []

        for a, b in queries:
            if a not in parent or b not in parent:
                result.append(-1.0)
                continue

            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                result.append(-1.0)
            else:
                result.append(weight[a] / weight[b])

        return result
