# ======================================================
# BINARY TREE LEVEL ORDER TRAVERSAL (LeetCode 102)
# ======================================================

# Problem:
# Given the root of a binary tree, return the level order
# traversal of its nodes' values (i.e., from left to right,
# level by level).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Height + Print Level)
# ------------------------------------------------------

class BruteForceSolution:
    def levelOrder(self, root):
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def getLevel(node, level, res):
            if not node:
                return
            if level == 1:
                res.append(node.val)
            else:
                getLevel(node.left, level - 1, res)
                getLevel(node.right, level - 1, res)

        h = height(root)
        result = []

        for i in range(1, h + 1):
            level = []
            getLevel(root, i, level)
            result.append(level)

        return result


# ------------------------------------------------------
# 2️⃣ BFS (Queue - Classic Level Order)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

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

            result.append(level)

        return result


# ------------------------------------------------------
# 3️⃣ DFS (Using Depth Tracking)
# ------------------------------------------------------

class DFSSolution:
    def levelOrder(self, root):
        result = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(result):
                result.append([])

            result[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class IterativeDFSSolution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node:
                if depth == len(result):
                    result.append([])

                result[depth].append(node.val)

                # Push right first so left is processed first
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))

        return result


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Clean BFS)
# ------------------------------------------------------

class OptimalSolution:
    def levelOrder(self, root):
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result




