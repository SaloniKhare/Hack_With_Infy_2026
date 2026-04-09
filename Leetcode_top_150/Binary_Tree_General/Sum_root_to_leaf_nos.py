# ======================================================
# SUM ROOT TO LEAF NUMBERS (LeetCode 129)
# ======================================================

# Problem:
# Given the root of a binary tree where each node contains
# a digit (0-9), each root-to-leaf path represents a number.
# Return the total sum of all root-to-leaf numbers.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store All Numbers as Strings)
# ------------------------------------------------------

class BruteForceSolution:
    def sumNumbers(self, root):
        if not root:
            return 0

        nums = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                nums.append(int(path))

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return sum(nums)


# ------------------------------------------------------
# 2️⃣ Better Approach (Carry Integer Value)
# ------------------------------------------------------

class BetterSolution:
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0

            current = current * 10 + node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


# ------------------------------------------------------
# 3️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class DFSSolution:
    def sumNumbers(self, root):
        if not root:
            return 0

        stack = [(root, root.val)]
        total = 0

        while stack:
            node, num = stack.pop()

            if not node.left and not node.right:
                total += num

            if node.right:
                stack.append((node.right, num * 10 + node.right.val))
            if node.left:
                stack.append((node.left, num * 10 + node.left.val))

        return total


# ------------------------------------------------------
# 4️⃣ BFS (Queue)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def sumNumbers(self, root):
        if not root:
            return 0

        queue = deque([(root, root.val)])
        total = 0

        while queue:
            node, num = queue.popleft()

            if not node.left and not node.right:
                total += num

            if node.left:
                queue.append((node.left, num * 10 + node.left.val))
            if node.right:
                queue.append((node.right, num * 10 + node.right.val))

        return total


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Clean DFS)
# ------------------------------------------------------

class OptimalSolution:
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0

            current = current * 10 + node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
