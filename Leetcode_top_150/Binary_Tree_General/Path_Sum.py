# ======================================================
# PATH SUM (LeetCode 112)
# ======================================================

# Problem:
# Given the root of a binary tree and an integer targetSum,
# return True if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store All Root-to-Leaf Paths)
# ------------------------------------------------------

class BruteForceSolution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        paths = []

        def dfs(node, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                paths.append(sum(path))

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, [])

        return targetSum in paths


# ------------------------------------------------------
# 2️⃣ Recursive DFS (Subtract Target)
# ------------------------------------------------------

class RecursiveSolution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # Leaf node
        if not root.left and not root.right:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))


# ------------------------------------------------------
# 3️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class DFSSolution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True

            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return False


# ------------------------------------------------------
# 4️⃣ BFS (Queue Level Order)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            node, curr_sum = queue.popleft()

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True

            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))

        return False


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Clean DFS)
# ------------------------------------------------------

class OptimalSolution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))



