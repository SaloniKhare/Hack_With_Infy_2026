# ======================================================
# BINARY TREE ZIGZAG LEVEL ORDER TRAVERSAL (LeetCode 103)
# ======================================================

# Problem:
# Given the root of a binary tree, return the zigzag level
# order traversal of its nodes' values.
# (i.e., left to right, then right to left, alternating)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Reverse Alternate Levels)
# ------------------------------------------------------

from collections import deque

class BruteForceSolution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

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

            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right

        return result


# ------------------------------------------------------
# 2️⃣ BFS (Using Deque for Efficient Insert)
# ------------------------------------------------------

class DequeSolution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            size = len(queue)
            level = deque()

            for _ in range(size):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result


# ------------------------------------------------------
# 3️⃣ DFS (Using Depth Tracking)
# ------------------------------------------------------

class DFSSolution:
    def zigzagLevelOrder(self, root):
        result = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(result):
                result.append(deque())

            if depth % 2 == 0:
                result[depth].append(node.val)
            else:
                result[depth].appendleft(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return [list(level) for level in result]


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class IterativeDFSSolution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node:
                if depth == len(result):
                    result.append(deque())

                if depth % 2 == 0:
                    result[depth].append(node.val)
                else:
                    result[depth].appendleft(node.val)

                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))

        return [list(level) for level in result]


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Clean BFS + Direction Flag)
# ------------------------------------------------------

class OptimalSolution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            level = deque()

            for _ in range(len(queue)):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result
