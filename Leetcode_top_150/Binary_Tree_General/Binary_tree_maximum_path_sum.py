# ======================================================
# BINARY TREE MAXIMUM PATH SUM (LeetCode 124)
# ======================================================

# Problem:
# A path in a binary tree is any sequence of nodes from
# some starting node to any node in the tree along the
# parent-child connections.
# The path must contain at least one node and does not
# need to go through the root.
# Return the maximum path sum.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Check All Paths - Inefficient)
# ------------------------------------------------------

class BruteForceSolution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def get_paths(node):
            if not node:
                return []

            left_paths = get_paths(node.left)
            right_paths = get_paths(node.right)

            all_paths = [node.val]

            for val in left_paths:
                all_paths.append(node.val + val)
            for val in right_paths:
                all_paths.append(node.val + val)

            # Update global max
            for val in all_paths:
                self.max_sum = max(self.max_sum, val)

            for l in left_paths:
                for r in right_paths:
                    self.max_sum = max(self.max_sum, l + node.val + r)

            return all_paths

        get_paths(root)
        return self.max_sum


# ------------------------------------------------------
# 2️⃣ Recursive DFS (Track Max Path)
# ------------------------------------------------------

class RecursiveSolution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Ignore negative paths
            left = max(left, 0)
            right = max(right, 0)

            # Path passing through node
            current = node.val + left + right
            self.max_sum = max(self.max_sum, current)

            # Return max single path
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum


# ------------------------------------------------------
# 3️⃣ Iterative (Postorder using Stack)
# ------------------------------------------------------

class IterativeSolution:
    def maxPathSum(self, root):
        if not root:
            return 0

        stack = [(root, False)]
        dp = {}
        max_sum = float('-inf')

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left = max(dp.get(node.left, 0), 0)
                right = max(dp.get(node.right, 0), 0)

                max_sum = max(max_sum, node.val + left + right)
                dp[node] = node.val + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return max_sum


# ------------------------------------------------------
# 4️⃣ Optimized DFS (Return Gain)
# ------------------------------------------------------

class OptimizedSolution:
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def gain(node):
            if not node:
                return 0

            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)

            # Max path using this node as root
            self.ans = max(self.ans, node.val + left_gain + right_gain)

            # Return best single branch
            return node.val + max(left_gain, right_gain)

        gain(root)
        return self.ans


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Clean & Most Asked)
# ------------------------------------------------------

class OptimalSolution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute left & right gains
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Update global maximum (path through node)
            self.max_sum = max(self.max_sum, node.val + left + right)

            # Return max gain for parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum




