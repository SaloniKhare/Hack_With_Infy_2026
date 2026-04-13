# ======================================================
# MINIMUM ABSOLUTE DIFFERENCE IN BST (LeetCode 530)
# ======================================================

# Problem:
# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between
# values of any two different nodes in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store All Values + Compare)
# ------------------------------------------------------

class BruteForceSolution:
    def getMinimumDifference(self, root):
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        min_diff = float('inf')
        n = len(values)

        for i in range(n):
            for j in range(i + 1, n):
                min_diff = min(min_diff, abs(values[i] - values[j]))

        return min_diff


# ------------------------------------------------------
# 2️⃣ Better (Sort + Adjacent Difference)
# ------------------------------------------------------

class BetterSolution:
    def getMinimumDifference(self, root):
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        min_diff = float('inf')

        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return min_diff


# ------------------------------------------------------
# 3️⃣ DFS with Tracking Previous Node
# ------------------------------------------------------

class DFSSolution:
    def getMinimumDifference(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff


# ------------------------------------------------------
# 4️⃣ Iterative Inorder (Stack)
# ------------------------------------------------------

class IterativeSolution:
    def getMinimumDifference(self, root):
        stack = []
        curr = root
        prev = None
        min_diff = float('inf')

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, curr.val - prev)

            prev = curr.val
            curr = curr.right

        return min_diff


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Inorder Traversal)
# ------------------------------------------------------

class OptimalSolution:
    def getMinimumDifference(self, root):
        self.prev = None
        self.ans = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.ans
