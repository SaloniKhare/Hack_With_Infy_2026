# ======================================================
# CLONE GRAPH (LeetCode 133)
# ======================================================

# Problem:
# Given a reference of a node in a connected undirected graph,
# return a deep copy (clone) of the graph.
#
# Each node contains:
# - val (int)
# - neighbors (list of Node)


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ------------------------------------------------------
# 1️⃣ Brute Force (DFS without Map - Not Correct for Cycles)
# ------------------------------------------------------

class BruteForceSolution:
    def cloneGraph(self, node):
        if not node:
            return None

        new_node = Node(node.val)

        for nei in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(nei))

        return new_node


# ------------------------------------------------------
# 2️⃣ DFS with HashMap (Visited Map)
# ------------------------------------------------------

class DFSSolution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            copy = Node(curr.val)
            visited[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)


# ------------------------------------------------------
# 3️⃣ BFS (Queue + Map)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)

                visited[curr].neighbors.append(visited[nei])

        return visited[node]


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class IterativeDFSSolution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()

            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    stack.append(nei)

                visited[curr].neighbors.append(visited[nei])

        return visited[node]


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (DFS with Map - Most Asked)
# ------------------------------------------------------

class OptimalSolution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            clone = Node(curr.val)
            visited[curr] = clone

            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
