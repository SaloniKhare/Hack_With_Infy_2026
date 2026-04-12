# ======================================================
# BINARY TREE RIGHT SIDE VIEW (LeetCode 199)
# ======================================================

# Problem:
# Given the root of a binary tree, imagine yourself standing
# on the right side of it, return the values of the nodes
# you can see ordered from top to bottom.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Level Order + Store All Levels)
# ------------------------------------------------------

from collections import deque

class BruteForceSolution:
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return [lvl[-1] for lvl in levels]


# ------------------------------------------------------
# 2️⃣ BFS (Track Last Node in Each Level)
# ------------------------------------------------------

class BFSSolution:
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i == size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# ------------------------------------------------------
# 3️⃣ DFS (Right First Traversal)
# ------------------------------------------------------

class DFSSolution:
    def rightSideView(self, root):
        result = []

        def dfs(node, depth):
            if not node:
                return

            # First node at this depth
            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class IterativeDFSSolution:
    def rightSideView(self, root):
        if not root:
            return []

        stack = [(root, 0)]
        result = []

        while stack:
            node, depth = stack.pop()

            if node:
                if depth == len(result):
                    result.append(node.val)

                # Push left first so right is processed first
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return result


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (DFS Right-First)
# ------------------------------------------------------

class OptimalSolution:
    def rightSideView(self, root):
        result = []

        def dfs(node, level):
            if not node:
                return

            # First node encountered at this level
            if level == len(result):
                result.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result
