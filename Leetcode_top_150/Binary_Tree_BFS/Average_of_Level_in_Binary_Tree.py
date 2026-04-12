# ======================================================
# AVERAGE OF LEVELS IN BINARY TREE (LeetCode 637)
# ======================================================

# Problem:
# Given the root of a binary tree, return the average value
# of the nodes on each level in the form of an array.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store Levels Separately)
# ------------------------------------------------------

from collections import deque

class BruteForceSolution:
    def averageOfLevels(self, root):
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

            levels.append(sum(level) / len(level))

        return levels


# ------------------------------------------------------
# 2️⃣ BFS (Track Sum & Count)
# ------------------------------------------------------

class BFSSolution:
    def averageOfLevels(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / size)

        return result


# ------------------------------------------------------
# 3️⃣ DFS (Store Sum & Count per Level)
# ------------------------------------------------------

class DFSSolution:
    def averageOfLevels(self, root):
        sums = []
        counts = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(sums):
                sums.append(0)
                counts.append(0)

            sums[depth] += node.val
            counts[depth] += 1

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return [sums[i] / counts[i] for i in range(len(sums))]


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class IterativeDFSSolution:
    def averageOfLevels(self, root):
        if not root:
            return []

        sums = []
        counts = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node:
                if depth == len(sums):
                    sums.append(0)
                    counts.append(0)

                sums[depth] += node.val
                counts[depth] += 1

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [sums[i] / counts[i] for i in range(len(sums))]


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Clean BFS)
# ------------------------------------------------------

class OptimalSolution:
    def averageOfLevels(self, root):
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        result = []

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / size)

        return result





